dates = {}
recipes = {}
types = {}
descriptions = {}
ingredients = {}
comments = {}

profile_info = {}

def add_ingredients(recipe_id=None, text=None):
  if recipe_id and text:
    text_list = text.split("\n")
    ingredients[recipe_id] = text_list


def add_instructions(recipe_id=None, text=None):
  if recipe_id and text:
    text_list = text.split("\n")
    instructions_dict = {}
    for i, instruction in enumerate(text_list):
      instructions_dict["Step {}".format(i+1)] = instruction

    instructions[recipe_id] = instructions_dict
