from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/45026b258c99b9f624b6").json()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts = posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


    

if __name__ == "__main__":
     app.run(debug = True)