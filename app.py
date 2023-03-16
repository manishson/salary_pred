from flask import Flask, redirect, render_template, url_for,request
import pickle

app=Flask(__name__)

with open("model.pkl","rb") as file:
    model=pickle.load(file)
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_salary", methods=["POST"])
def get_salary():
    data=request.form
    year_ex=float( data["html_year"])

    predict=model.predict([[year_ex]])

    return render_template("index.html", salary=predict)

if __name__=="__main__":
    app.run(host='0.0.0.0')