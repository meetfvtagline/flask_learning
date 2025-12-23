from flask_wtf import FlaskForm
from wtforms import TextAreaField,IntegerField,SelectField,SubmitField,RadioField,StringField
from wtforms import ValidationError,validators


class ContactForm(FlaskForm):
    name=StringField("Name Of student",[validators.DataRequired("Please Enter You name")])
    gender=RadioField("Gender",choices=[('M','Male'),('F','Female')])
    address=TextAreaField("Address")
    email=StringField("Email",[validators.DataRequired("Please Enter Your Email"),validators.Email("Please Enter Your Email Address")])
    age=IntegerField("Enter Your age:",validators=[validators.DataRequired(), validators.NumberRange(min=1, max=120)])
    language=SelectField('Language',choices=[('cpp','c'),('py','Python')],coerce=str)
    submit=SubmitField("Send")