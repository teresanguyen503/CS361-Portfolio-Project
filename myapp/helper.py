dates = {}
meals = {}
types = {}
descriptions = {}
ingredients = {}
comments = {}


def add_ingredients(recipe_id=None, text=None):
  if recipe_id and text:
    text_list = text.split("\n")
    ingredients[recipe_id] = text_list
