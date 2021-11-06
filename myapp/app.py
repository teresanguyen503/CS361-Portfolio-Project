from flask import Flask, render_template, request, session, redirect, url_for, flash
from helper import dates, recipes, types, descriptions, ingredients, add_ingredients, add_instructions, comments
from forms import RecipeForm, CommentForm
from wtforms.fields.html5 import DateField
import requests
import json
from operator import itemgetter 



url_endpoint = "https://www.indexofsciences.com/index.php/wp-json/wp/v2/posts"
response = requests.get(url_endpoint)
json_result = json.loads(response.content)


app = Flask(__name__, static_folder='myapp/static')
app.config["SECRET_KEY"] = "mysecret"


@app.route("/", methods=["GET", "POST"])
def index(): 
  return render_template("index.html")


@app.route("/mealEntry", methods=["GET", "POST"])
def mealEntry():
  recipe_form = RecipeForm(csrf=False)
  if recipe_form.validate_on_submit and request.method == "POST":
      new_id = len(recipes)+1
      dates[new_id] = recipe_form.date.data
      recipes[new_id] = recipe_form.recipe.data
      types[new_id] = recipe_form.recipe_type.data
      descriptions[new_id] = recipe_form.description.data
      new_ingredients = recipe_form.ingredients.data
    
      add_ingredients(new_id, new_ingredients)
      
      comments[new_id] = []
      flash("You just added to your food diary!")
      return redirect(url_for("mealEntry"))
  return render_template("mealEntry.html", template_form=recipe_form)

@app.route("/recipeDates", methods=["GET", "POST"])
def recipeDates():
  # all_data = zip(dates, recipes, types, descriptions, ingredients, comments, instructions)
  # sort_data = sort_data(all_data)
  return render_template("dates.html", template_recipes=dates)
  # template_rececipes = dates

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm(csrf=False)
  if comment_form.validate_on_submit():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)
  return render_template("recipe.html", template_recipe=recipes[id], template_type=types[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_comments=comments[id], template_form=comment_form)
  # template_instructions=instructions[id]

@app.route("/profile", methods=["GET", "POST"])
def profile():
  # profile_form = ProfileForm(csrf_enabled=False)
  # if profile_form.validate_on_submit():
    
  #   name = profile_form.name.data
  #   date_of_birth = profile_form.date_of_birth.data
  #   weight = profile_form.weight.data
  #   height = profile_form.height.data

   
  #   add_profile(name, date_of_birth, weight, height)
    

  return render_template("profile.html")

@app.route("/nutritionalNews", methods=["GET"])
def nutritionalNews():
  title_list = []
  links_list = []
  for lists in range(len(json_result)):
    title_list.append(json_result[lists]["yoast_head_json"]["title"])
    links_list.append(json_result[lists]["link"])
  title_link_list = zip(title_list, links_list)

  return render_template("news.html", title_link_list=title_link_list, article_title=title_list, article_lists=links_list)



if __name__ == "__main__": 
  app.run(debug=True, port=5000)