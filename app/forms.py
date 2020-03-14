#from app import app, mail
from flask import render_template, request, redirect, url_for, flash 
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email 



class profile(FlaskForm):
    
    FirstName=StringField('First Name',validators=[DataRequired()])

    LastName=StringField("Last Name",validators=[DataRequired()])
    
    Gender=SelectField('Gender',choices=[('M','Male'),('F','Female')])
    
    Email=StringField('Email',validators=[DataRequired(),Email()])
    
    Location=StringField('Location',validators=[DataRequired()]) 
    
    Biography=TextAreaField('Biography',validators=[DataRequired()]) 
    
    ProfilePicture=FileField('ProfilePictures',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])