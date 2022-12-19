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
    return render_template("driver_standings.html")

def edit_tables_page():
    return render_template("edit_tables.html")

def sprint_results_page():
    db = current_app.config["db"]
    spRes = db.getSprintResults()
    return render_template("sprint_results.html",spRes = spRes, methods=["GET", "POST"])