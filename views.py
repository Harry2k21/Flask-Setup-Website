from flask import Blueprint, render_template, request, jsonify, redirect

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Harry", age="20")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)
@views.route("/json")
def get_json():
    return jsonify({'name': 'Harry', 'Strength': 20})

@views.route("/data")
def get_data():
data = request.json
return jsonify(data)
