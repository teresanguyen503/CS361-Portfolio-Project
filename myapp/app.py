from flask import Flask, render_template, request, session 
from helper import recipes, types, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from forms import RecipeForm, CommentForm
from wtforms.fields.html5 import DateField
import requests
import json
from operator import itemgetter 


url_endpoint = "https://www.indexofsciences.com/index.php/wp-json/wp/v2/posts" 
response = requests.get(url_endpoint)
json_result = json.loads(response.content)
print("-------------------------------------------")
# for links in range(len(json_result)):
#   print(json_result[links]['link'])



app = Flask(__name__, static_folder='myapp/static')
app.config["SECRET_KEY"] = "mysecret"


@app.route("/", methods=["GET", "POST"])
def index(): 
  return render_template("index.html")

@app.route("/nutritionalNews", methods=["GET"])
def nutritionalNews():
  links_list = []
  for links in range(len(json_result)):
    links_list.append(json_result[links]["link"])
  return render_template("news.html", article_lists=links_list)

@app.route("/mealEntry", methods=["GET", "POST"])
def mealEntry():
  recipe_form = RecipeForm(csrf_enabled=False)
  if recipe_form.validate_on_submit():
    

    new_id = len(recipes)+1
    recipes[new_id] = recipe_form.recipe.data
    types[new_id] = recipe_form.recipe_type.data
    descriptions[new_id] = recipe_form.description.data
    new_ingredients = recipe_form.ingredients.data
   
    add_ingredients(new_id, new_ingredients)
    
    comments[new_id] = []
  return render_template("mealEntry.html", template_recipes=recipes, template_form=recipe_form)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm(csrf_enabled=False)
  if comment_form.validate_on_submit():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)
  return render_template("recipe.html", template_recipe=recipes[id], template_type=types[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id], template_comments=comments[id], template_form=comment_form)

if __name__ == "__main__": 
  app.run(debug=True)