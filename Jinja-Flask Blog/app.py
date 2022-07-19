from flask import Flask, render_template
import  requests
from post import Post

posts = requests.get("https://api.npoint.io/0c24ac68642fc257b241").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html" , posts=post_objects)


@app.route('/post/<postId>')
def news(postId):
    curretnPost = post_objects[int(postId)-1]

    return render_template("static.html" , art=curretnPost)

if __name__ == "__main__":
    app.run(debug=True)
