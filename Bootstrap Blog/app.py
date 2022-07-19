from flask import Flask, render_template, request
import requests
from post import Post
import smtplib


my_email = "vriim360@gmail.com"
password = "enevbkiuobaptybj"

posts = requests.get("https://api.npoint.io/0c24ac68642fc257b241").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["image"])
    post_objects.append(post_obj)

app = Flask(__name__)

def sendEmail(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure connection, encrypts mail
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="mura.ivan@hotmail.com",
                            msg=f"Subject:Hello\n\n{message}")
        connection.close()


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/postp/<postid>')
def postp(postid):
    curretnPost = post_objects[int(postid)-1]

    return render_template("post.html", arti=curretnPost)


@app.route('/contact',methods=['GET', 'POST'])
def contact():
    aux = True
    if request.method == 'POST':
        name = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["msgt"]
        final_m = f"Hi, {name}\n" \
                  f"We recieved your message from {email}\n" \
                  f"We will be sending you sms messages to {phone}\n" \
                  f"Your messase: \n{message}"
        sendEmail(final_m)
        aux=False
        return render_template("contact.html", form=aux)
    else:
        return render_template("contact.html", form=aux)

# @app.route('/form-entry', methods=["POST"])
# def recieve_data():
#     name = request.form["username"]
#     email = request.form["email"]
#     phone = request.form["phone"]
#     message = request.form["msgt"]
#     print(name)
#     print(email)
#     print(phone)
#     print(message)
#     return "<h1>Message recieved </h1>"


if __name__ == "__main__":
    app.run(debug=True)
