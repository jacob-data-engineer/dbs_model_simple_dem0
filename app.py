from flask import Flask, render_template, request
import joblib

app = Flask(__name__)  ### this is the name of the main file. i.e app.py

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

    @app.route("/prediction",methods=["GET","POST"])
def prediction():
    q = float(request.form.get("q"))
    return(render_template("prediction.html",r=(-50.6*q)+90.2))


if __name__ == "__main__":   ####  this is for local testing
    app.run()