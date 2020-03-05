from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,IntegerField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
import pandas as pd
import numpy as np


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    location = TextField("Enter Location : ")
    carpet_area = IntegerField("Enter the Carpet Area in Sqft : ")
    bedroom = IntegerField("Number Of Bedroom : ")
    bathroom = IntegerField("Number Of Bathroom : ")
    avaliability = TextField("Avaliability(Eg : Dec-20/ Mar-22/ Ready To Move etc) : ")
    conditon =  SelectField("Condition of the property? : ", choices = [("0","Resale"),("1","New")], default = 0)
    super_area = IntegerField("Enter the Super Area in Sqft : ")
    year_built = IntegerField("Year the property was Built or 'Under Construction' : ")
    floor = IntegerField("Number Of Floors : ")
    flooring = SelectField("Type Of Flooring : ", choices = [("Vitrified Tiles","Vitrified Tiles"),("Granite","Granite"),("Marbonite","Marbonite"),
    ("Ceramic","Ceramic"),("Wooden","Wooden"),("Mosaic Tiles","Mosaic Tiles"),("Normal Tiles","Normal Tiles"),("Marble Flooring","Marble Flooring")]
    , default = "Vitrified Tiles")
    furnishing = SelectField("Type Of Furnishing? : ", choices = [("Semi Furnished","Semi Furnished"),("Not Furnished","Not Furnished"),
    ("Fully Furnished","Fully Furnished")], default = "Semi Furnished")
    parking = SelectField("Does the property have a Parking? : ", choices = [("0","No"),("1","Yes")], default = 0)
    pool = SelectField("Does the property have a Pool? : ", choices = [("0","No"),("1","Yes")], default = 0)
    gym = SelectField("Does the property have a Gym? : ", choices = [("0","No"),("1","Yes")], default = 0)
    powerbackup = SelectField("Does the property have Power Backup? : ", choices = [("0","No"),("1","Yes")], default = 0)
    jogging = SelectField("Does the property have a Jogging Track? : ", choices = [("0","No"),("1","Yes")], default = 0)
    clubhouse = SelectField("Does the property have a CLub House? : ", choices = [("0","No"),("1","Yes")], default = 0)
    water_harvesting = SelectField("Does the property have Water Harvesting? : ", choices = [("0","No"),("1","Yes")], default = 0)
    court = SelectField("Does the property have a Court? : ", choices = [("0","No"),("1","Yes")], default = 0)



    submit = SubmitField("PREDICT PRICE")


@app.route('/', methods = ['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['location'] = (form.location.data)
        session['carpet_area'] = (form.carpet_area.data)
        session['bedroom'] = (form.bedroom.data)
        session['bathroom'] = (form.bathroom.data)
        session['avaliability'] = (form.avaliability.data)
        session['conditon'] = (form.conditon.data)
        session['super_area'] = (form.super_area.data)
        session['year_built'] = (form.year_built.data)
        session['floor'] = (form.floor.data)
        session['flooring'] = (form.flooring.data)
        session['furnishing'] = (form.furnishing.data)
        session['parking'] = (form.parking.data)
        session['pool'] = (form.pool.data)
        session['gym'] = (form.gym.data)
        session['powerbackup'] = (form.powerbackup.data)
        session['jogging'] = (form.jogging.data)
        session['clubhouse'] = (form.clubhouse.data)
        session['water_harvesting'] = (form.water_harvesting.data)
        session['court'] = (form.court.data)



        X_O = ([ (session['location']),(session['carpet_area']),(session['bedroom']),(session['bathroom']),
                            (session['avaliability']),
                            int((session['conditon'])),(session['super_area']),(session['year_built']),
                            (session['floor']),(session['flooring']),
                            (session['furnishing']),int((session['parking'])),int((session['pool'])),
                            int((session['gym'])),int((session['powerbackup'])),
                            int((session['jogging'])),int((session['clubhouse'])),int((session['water_harvesting'])),
                            int((session['court'])) ])

        pred = []
        import model
        pred.append(model.Predict(X_O))

        return render_template("predict.html",pred=pred[0])

    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
