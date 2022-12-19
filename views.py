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
    if request.method == "GET":
        sprint_results = db.getSprintResults()
        return render_template("sprint_results.html", sprint_results=sprint_results)
    else:
        sprint_results_ids = request.form.getlist("sprint_results_id")
        for sprint_results_id in sprint_results_ids:
            db.removeSprintResults(sprint_results_id)
        return redirect(url_for("sprint_results_page"))

def update_sprint_results_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("update_spRes.html")

def add_sprint_results_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("add_spRes.html")