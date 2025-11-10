# python app using flask and pymongo

from flask import Flask, request, render_template, redirect, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# connect mongo
connect = MongoClient("mongodb://mongodb:27017")
db = connect["recipe_base"]
posts = db["posts"]

# Test post
if posts.count_documents({}) == 0:
    test = { "title":"TestPost1", "content":"TestContent1"}
    posts.insert_one(test)

@app.route("/", methods=["GET", "POST"])
def index():
    # ---- POST: Add new recipe ----
    if request.method == "POST":
        title = request.form.get("title")
        cuisine = request.form.get("cuisine")
        ingredients = request.form.get("ingredients")
        content = request.form.get("content")
        cals = request.form.get("cals")
        protein = request.form.get("protein")
        carbs = request.form.get("carbs")
        fats = request.form.get("fats")

        if title:
            posts.insert_one({
                "title": title.strip(),
                "cuisine": cuisine.strip() if cuisine else "",
                "ingredients": ingredients.strip() if ingredients else "",
                "content": content.strip() if content else "",
                "cals": cals.strip() if cals else "",
                "protein": protein.strip() if protein else "",
                "carbs": carbs.strip() if carbs else "",
                "fats": fats.strip() if fats else "",
            })

        return redirect("/")

    # ---- GET: search & filter ----
    search_query = request.args.get("q", "").strip()
    min_cals = request.args.get("min_cals")
    max_cals = request.args.get("max_cals")
    min_protein = request.args.get("min_protein")
    max_protein = request.args.get("max_protein")
    min_carbs = request.args.get("min_carbs")
    max_carbs = request.args.get("max_carbs")
    min_fats = request.args.get("min_fats")
    max_fats = request.args.get("max_fats")

    query = {}

    # --- Updated search: only match titles STARTING with query tokens ---
    if search_query:
        tokens = search_query.split()
        regex_conditions = [{"title": {"$regex": rf"^{token}", "$options": "i"}} for token in tokens]
        query["$and"] = regex_conditions

    # --- Filters ---
    expr_conditions = []
    def add_range_condition(field, min_val, max_val):
        if min_val:
            expr_conditions.append({"$gte": [{"$toDouble": f"${field}"}, float(min_val)]})
        if max_val:
            expr_conditions.append({"$lte": [{"$toDouble": f"${field}"}, float(max_val)]})

    add_range_condition("cals", min_cals, max_cals)
    add_range_condition("protein", min_protein, max_protein)
    add_range_condition("carbs", min_carbs, max_carbs)
    add_range_condition("fats", min_fats, max_fats)

    if expr_conditions:
        query["$expr"] = {"$and": expr_conditions}

    # Combine both conditions safely
    if "$and" in query and "$expr" in query:
        query = {"$and": [{"$and": query["$and"]}, {"$expr": query["$expr"]}]}
    elif "$expr" in query:
        query = {"$expr": query["$expr"]}
    elif "$and" in query:
        query = {"$and": query["$and"]}

    posts_list = list(posts.find(query).sort("_id", -1))
    return render_template("index.html", posts=posts_list, query=search_query)


@app.route("/autocomplete")
def autocomplete():
    term = request.args.get("q", "").strip()
    if not term:
        return jsonify([])
    suggestions = posts.find(
        {"title": {"$regex": rf"^{term}", "$options": "i"}}, {"title": 1}
    ).limit(5)
    titles = [s["title"] for s in suggestions]
    return jsonify(titles)


@app.route("/goals", methods=["GET", "POST"])
def goals():
    if request.method == "POST":
        if "reset" in request.form:
            db.goals.delete_many({})
            return redirect("/goals")

        title = request.form.get("title")
        calories = float(request.form.get("calories") or 0)
        protein = float(request.form.get("protein") or 0)
        carbs = float(request.form.get("carbs") or 0)
        fats = float(request.form.get("fats") or 0)

        if title:
            db.goals.insert_one({
                "title": title,
                "calories": calories,
                "protein": protein,
                "carbs": carbs,
                "fats": fats,
                "progress": { "calories": 0, "protein": 0, "carbs": 0, "fats": 0 }
            })
        return redirect("/goals")

    goals_list = list(db.goals.find())

    # Ensure backward compatibility with older goal entries
    for g in goals_list:
        if "progress" not in g:
            g["progress"] = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
        # Also ensure macro fields exist
        for macro in ["calories", "protein", "carbs", "fats"]:
            if macro not in g:
                g[macro] = 0

    return render_template("goals.html", goals=goals_list)



@app.route("/delete_goal/<goal_id>", methods=["POST"])
def delete_goal(goal_id):
    db.goals.delete_one({"_id": ObjectId(goal_id)})
    return redirect("/goals")


@app.route("/add_to_goals", methods=["POST"])
def add_to_goals():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    # Extract macro values from the recipe
    added_cals = float(data.get("cals", 0))
    added_protein = float(data.get("protein", 0))
    added_carbs = float(data.get("carbs", 0))
    added_fats = float(data.get("fats", 0))

    # Update all current goals' progress fields
    goals = db.goals.find()
    for g in goals:
        progress = g.get("progress", {"calories": 0, "protein": 0, "carbs": 0, "fats": 0})
        progress["calories"] += added_cals
        progress["protein"] += added_protein
        progress["carbs"] += added_carbs
        progress["fats"] += added_fats

        db.goals.update_one(
            {"_id": g["_id"]},
            {"$set": {"progress": progress}}
        )

    return jsonify({"message": "Recipe added to goals successfully!"}), 200

@app.route("/debugdb")
def debugdb():
    posts_data = list(posts.find({}, {"title": 1, "cals": 1, "protein": 1, "carbs": 1, "fats": 1}))
    for post in posts_data:
        post["_id"] = str(post["_id"])  # Convert ObjectId to string for JSON
    from flask import jsonify
    return jsonify(posts_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)