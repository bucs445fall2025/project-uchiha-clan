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
        content = request.form.get("content")
        if title and content:
            posts.insert_one({"title": title, "content": content})
        return redirect("/")
    
    postlist = list(posts.find())
    return render_template("index.html", posts=postlist)

# start flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)