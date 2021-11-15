from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField



class MealForm(FlaskForm):
  date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
  meal_categories = [("Breakfast","Breakfast"), ("Lunch","Lunch"), ("Dinner","Dinner"), ("Snack", "Snack")]
  meal =  StringField("Meal", validators=[DataRequired()])
  meal_type = RadioField("Type", choices=meal_categories)
  description = StringField("Description", validators=[DataRequired()])
  ingredients = TextAreaField("Ingredients (**Press 'Enter/Return' to separate ingredients)", validators=[DataRequired()])
  submit = SubmitField("Add Meal")

class CommentForm(FlaskForm):
  comment =  StringField("Comment", validators=[DataRequired()])
  submit = SubmitField("Add Comment")

class DeleteForm(FlaskForm): 
  submit = SubmitField("Delete Entry")