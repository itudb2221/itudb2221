from flask import current_app, render_template
from models import *


def home_page():
    return render_template("home.html")

def drivers_page():
    db = current_app.config["db"]
    drivers = db.get_drivers()
    return render_template("drivers.html", drivers=drivers)

def seasons_page():
    return render_template("seasons.html")

def driver_standings_page():
    db = current_app.config["db"]
    driver_standings = db.get_driver_standings()
    return render_template("driver_standings.html", driver_standings=driver_standings)

def edit_tables_page():
    return render_template("edit_tables.html")