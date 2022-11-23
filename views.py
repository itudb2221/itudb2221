from flask import render_template

def home_page():
    return render_template("home.html")

def drivers_page():
    return render_template("drivers.html")

def seasons_page():
    return render_template("seasons.html")

def driver_standings_page():
    return render_template("driver_standings.html")