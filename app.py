from flask import Flask, render_template, request, redirect, session, jsonify
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = "mobileml"

# LOAD DATA
data = pd.read_csv("mobile_recommendation_system_dataset.csv")

data["price"] = pd.to_numeric(data["price"], errors="coerce")

# ML FEATURE
data["features"] = data["name"]

cv = CountVectorizer()
matrix = cv.fit_transform(data["features"])
similarity = cosine_similarity(matrix)
# USERS & CART
users = {}
cart = []

# ML RECOMMENDATION
def recommend(phone):

    if phone not in data["name"].values:
        return []

    index = data[data["name"] == phone].index[0]

    score = list(enumerate(similarity[index]))
    score = sorted(score, key=lambda x:x[1], reverse=True)[1:6]

    phones = [data.iloc[i[0]].to_dict() for i in score]

    return phones


# LOGIN PAGE
@app.route("/", methods=["GET","POST"])
def login():

    if request.method=="POST":

        username=request.form["username"]
        password=request.form["password"]

        if username in users and users[username]==password:

            session["user"]=username
            return redirect("/dashboard")

    return render_template("index.html", page="login")


# REGISTER
@app.route("/register", methods=["POST"])
def register():

    user=request.form["username"]
    pwd=request.form["password"]

    users[user]=pwd

    return redirect("/")


# LOGOUT
@app.route("/logout")
def logout():

    session.pop("user",None)

    return redirect("/")


# MAIN DASHBOARD
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():

    if "user" not in session:
        return redirect("/")

    phones=[]
    rec=[]
    compare1=None
    compare2=None

    top=data.sort_values(by="ratings",ascending=False).head(5)

    if request.method=="POST":

        action=request.form.get("action")

        # SEARCH
        if action=="search":

            phone=request.form["phone"]

            result=data[data["name"].str.contains(phone,case=False)]

            phones=result.to_dict("records")

            if not result.empty:
                rec=recommend(result.iloc[0]["name"])

        # BUDGET
        if action=="budget":

            budget=int(request.form["budget"])

            phones=data[data["price"]<=budget].to_dict("records")

        # COMPARE
        if action=="compare":

            p1=request.form["phone1"]
            p2=request.form["phone2"]

            r1=data[data["name"].str.contains(p1,case=False)]
            r2=data[data["name"].str.contains(p2,case=False)]

            if not r1.empty:
                compare1=r1.iloc[0].to_dict()

            if not r2.empty:
                compare2=r2.iloc[0].to_dict()

    return render_template(
        "index.html",
        page="dashboard",
        phones=phones,
        rec=rec,
        compare1=compare1,
        compare2=compare2,
        cart=cart,
        top=top.to_dict("records")
    )


# CART
@app.route("/add/<name>")
def add(name):

    item=data[data["name"]==name].iloc[0].to_dict()

    cart.append(item)

    return redirect("/dashboard")


@app.route("/remove/<name>")
def remove(name):

    global cart

    cart=[c for c in cart if c["name"]!=name]

    return redirect("/dashboard")


# AUTO SUGGEST
@app.route("/suggest")
def suggest():

    term=request.args.get("term")

    result=data[data["name"].str.contains(term,case=False)]

    return jsonify(result["name"].head(5).tolist())


# AI ASSISTANT
@app.route("/assistant", methods=["POST"])
def assistant():

    query=request.json["query"]

    result=data[data["name"].str.contains(query,case=False)]

    return jsonify(result.head(5).to_dict("records"))


if __name__=="__main__":
    app.run(debug=True)