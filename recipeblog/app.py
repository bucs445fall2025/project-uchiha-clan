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
    # Grab filter params
    min_cals = request.args.get("min_cals")
    max_cals = request.args.get("max_cals")
    min_protein = request.args.get("min_protein")
    max_protein = request.args.get("max_protein")
    min_carbs = request.args.get("min_carbs")
    max_carbs = request.args.get("max_carbs")
    min_fats = request.args.get("min_fats")
    max_fats = request.args.get("max_fats")

    query = {}
    filters = {
        "cals": (min_cals, max_cals),
        "protein": (min_protein, max_protein),
        "carbs": (min_carbs, max_carbs),
        "fats": (min_fats, max_fats)
    }

    # Build numeric range filters (convert stored strings to numbers safely)
    for field, (min_val, max_val) in filters.items():
        cond = {}
        if min_val:
            cond["$gte"] = float(min_val)
        if max_val:
            cond["$lte"] = float(max_val)
        if cond:
            # Use $expr to convert field strings to numbers during comparison
            query["$expr"] = {
                "$and": [
                    {"$gte": [{"$toDouble": f"${field}"}, cond.get("$gte", float("-inf"))]},
                    {"$lte": [{"$toDouble": f"${field}"}, cond.get("$lte", float("inf"))]}
                ]
            }

    posts_list = list(posts.find(query).sort("_id", -1))

    return render_template("index.html", posts=posts_list)

    

    #postlist = list(posts.find().sort("_id", -1))
    #return render_template("index.html", posts=postlist)

@app.route("/search", methods=["GET"])
def search():
    search_query = request.args.get("q", "").strip()

    # If user typed something, search by title only
    if search_query:
        results = list(posts.find(
            {"title": {"$regex": search_query, "$options": "i"}}
        ).sort("_id", -1))
    else:
        results = []

    # Render the main page template with the filtered posts
    return render_template("index.html", posts=results, query=search_query)


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