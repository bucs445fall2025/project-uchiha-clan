# python app using flask and pymongo

from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

# connect with MongoClient to default mongodb port (27017)
connect = MongoClient("mongodb://mongodb:27017")
db = connect["recipe_base"]
posts = db["posts"]

# Test post
if posts.count_documents({}) == 0:
    test = { "title":"TestPost1", "content":"TestContent1"}
    posts.insert_one(test)

# routing
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        cuisine = request.form.get("cuisine")
        ingredients = request.form.get("ingredients")
        cals = request.form.get("cals")
        protein = request.form.get("protein")
        carbs = request.form.get("carbs")
        fats = request.form.get("fats")
        content = request.form.get("content")

        if title and content:
            post_data = {
                "title": title,
                "cuisine": cuisine,
                "ingredients": ingredients,
                "cals": cals,
                "protein": protein,
                "carbs": carbs,
                "fats": fats,
                "content": content,
            }
            posts.insert_one(post_data)

        return redirect("/")

    postlist = list(posts.find().sort("_id", -1))
    return render_template("index.html", posts=postlist)


@app.route("/goals", methods=["GET", "POST"])
def goals():
    if request.method == "POST":
        goal_text = request.form.get("goal")
        if goal_text:
            db.goals.insert_one({"goal": goal_text})
        return redirect("/goals")

    goals_list = list(db.goals.find())
    return render_template("goals.html", goals=goals_list)


# start flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)