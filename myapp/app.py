from flask import Flask, render_template, request, session, redirect, url_for, flash
from helper import dates, meals, types, descriptions, ingredients, add_ingredients, comments
from forms import MealForm, CommentForm, DeleteForm
from wtforms.fields.html5 import DateField
import requests
import json
from operator import itemgetter 


def getWebScraperData():
  url_endpoint = "http://127.0.0.1:8000/articles"
  response = requests.get(url_endpoint)
  return json.loads(response.content)


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"


@app.route("/", methods=["GET", "POST"])
def index(): 
  return render_template("index.html")


@app.route("/mealEntry", methods=["GET", "POST"])
def mealEntry():
  meal_form = MealForm(csrf=False)
  if meal_form.validate_on_submit and request.method == "POST": 
    new_id = len(meals)+1
    meal_entry_helper_function(new_id, meal_form)
    flash("You just added to your food diary!", "submit")
    return redirect(url_for("mealEntry"))

  return render_template("mealEntry.html", template_form=meal_form)

def meal_entry_helper_function(new_id, meal_form): 
    dates[new_id] = meal_form.date.data
    meals[new_id] = meal_form.meal.data
    types[new_id] = meal_form.meal_type.data
    descriptions[new_id] = meal_form.description.data
    new_ingredients = meal_form.ingredients.data
  
    add_ingredients(new_id, new_ingredients)
    
    comments[new_id] = []
    return

@app.route("/mealDates", methods=["GET", "POST"])
def mealDates():
  sorted_dates = sorted(dates, key=dates.get, reverse=True)
  sorted_dict = {}

  for i in sorted_dates: 
    sorted_dict[i] = dates[i]

  return render_template("dates.html", template_meals=sorted_dict)


@app.route("/meal/<int:id>", methods=["GET", "POST"])
def mealDisplay(id):
  comment_form = CommentForm(csrf=False)
  if comment_form.validate():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)

  delete_form = DeleteForm(csrf=False)
  if bool(delete_form.confirm_category.data) and delete_form.validate(): 
    meal_delete_dislpay_helper_function(id, delete_form)
    return redirect(url_for("mealDates"))

  return render_template("mealDisplay.html", template_meals=meals[id], template_type=types[id],
    template_description=descriptions[id], template_ingredients=ingredients[id], template_comments=comments[id], 
    template_form=comment_form, template_delete=delete_form)

def meal_delete_dislpay_helper_function(id, delete_form): 
  dates.pop(id)
  meals.pop(id)
  types.pop(id)
  descriptions.pop(id)
  ingredients.pop(id)
  comments.pop(id)
  return 

@app.route("/nutritionalNews", methods=["GET"])
def nutritionalNews():
  json_result = getWebScraperData()

  title_list = []
  links_list = []
  description_list = []
  image_list = []
  for lists in json_result["articles"]:
    title_list.append(lists["title"])
    links_list.append(lists["link"])
    description_list.append(lists["description"])
    image_list.append(lists["img_src"])
  data_list = zip(title_list, links_list, description_list, image_list)

  return render_template("news.html", data_list=data_list)
    


if __name__ == "__main__": 
  app.run(debug=True, port=5000)