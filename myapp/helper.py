# dates = {1: "10/30/2021", 2: "10/31/2021"}
# recipes = {1: "Eggs", 2: "Toast"}
# types = {1: "Breakfast", 2: "Breakfast"}
# descriptions = {1: "Egg fried in butter", 2: "Toasted bread spread with butter"}
# ingredients = {1: ["1 pad of butter", "1 Egg", "A pinch of salt"], 2: ["1 pad of salted butter", "1 slice of bread"]}
# comments = {1: ["Yummy!!", "Egg-cellent ;->"], 2: ["Toasty", "What a great recipe!"]}

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

