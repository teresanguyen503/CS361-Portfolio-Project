from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class RecipeForm(FlaskForm):
  date = DateField('Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))

  recipe_categories = [("Breakfast","Breakfast"), ("Lunch","Lunch"), ("Dinner","Dinner"), ("Snack", "Snack")]
  recipe =  StringField("Recipe", validators=[DataRequired()])
  recipe_type = RadioField("Type", choices=recipe_categories)
  description = StringField("Description", validators=[DataRequired()])
  ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
  submit = SubmitField("Add Recipe")

class CommentForm(FlaskForm):
  comment =  StringField("Comment", validators=[DataRequired()])
  submit = SubmitField("Add Comment")