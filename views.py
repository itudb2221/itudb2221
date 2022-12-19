from flask import current_app, render_template, request, redirect, url_for
from models import *
import sqlite3 as sqlite
import traceback

def home_page():
    return render_template("home.html")

# ============ DRIVERS ============ #

def drivers_page():
    db = current_app.config["db"]
    if request.method == "GET":
        drivers = db.get_drivers()
        return render_template("drivers.html", drivers=drivers)
    else:
        driver_ids = request.form.getlist("driver_id")
        for driver_id in driver_ids:
            db.remove_driver(driver_id)
        return redirect(url_for("drivers_page"))
    
def update_driver_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("update_driver.html")
    else:
        driver_id = request.form['driverId']
        attr_names = list()
        attr_values = list()
        if "driverRef" in request.form:
            attr_names.append("driverRef")
            attr_values.append(request.form["driverRef"])
        if "driverNumber" in request.form:
            attr_names.append("driverNumber")
            attr_values.append(request.form["driverNumber"])
        if "code" in request.form:
            attr_names.append("code")
            attr_values.append(request.form["code"])
        if "forename" in request.form:
            attr_names.append("forename")
            attr_values.append(request.form["forename"])
        if "surname" in request.form:
            attr_names.append("surname")
            attr_values.append(request.form["surname"])
        if "dob" in request.form:
            attr_names.append("dob")
            attr_values.append(request.form["dob"])
        if "nationality" in request.form:
            attr_names.append("nationality")
            attr_values.append(request.form["nationality"])
        if "driverUrl" in request.form:
            attr_names.append("driverUrl")
            attr_values.append(request.form["driverUrl"])
        db.update_driver(driver_id, attr_names, attr_values)
        return redirect(url_for("drivers_page"))


def add_driver_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("add_driver.html")
    else:
        try:
            driverRef = request.form["driverRef"]
            driverNumber = request.form["driverNumber"]
            code = request.form["code"]
            forename = request.form["forename"]
            surname = request.form["surname"]
            dob = request.form["dob"]
            nationality = request.form["nationality"]
            driverUrl = request.form["driverUrl"]
            db.add_driver(Driver(0, driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl))
        except:
            print(traceback.format_exc())
        finally:
            return redirect(url_for("drivers_page"))

def seasons_page():
    return render_template("seasons.html")

# ============ DRIVER STANDINGS ============ #

def driver_standings_page():
    db = current_app.config["db"]
    if request.method == "GET":
        driver_standings = db.get_driver_standings()
        return render_template("driver_standings.html", driver_standings=driver_standings)
    else:
        driver_standing_ids = request.form.getlist("driver_standing_id")
        for driver_standing_id in driver_standing_ids:
            db.remove_driver_standing(driver_standing_id)
        return redirect(url_for("driver_standings_page"))

def update_driver_standing_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("update_driver_standing.html")
    else:
        driver_standing_id = request.form['driverStandingsId']
        attr_names = list()
        attr_values = list()
        if "raceId" in request.form:
            attr_names.append("raceId")
            attr_values.append(request.form["raceId"])
        if "driverId" in request.form:
            attr_names.append("driverId")
            attr_values.append(request.form["driverId"])
        if "points" in request.form:
            attr_names.append("points")
            attr_values.append(request.form["points"])
        if "position" in request.form:
            attr_names.append("position")
            attr_values.append(request.form["position"])
        if "positionText" in request.form:
            attr_names.append("positionText")
            attr_values.append(request.form["positionText"])
        if "wins" in request.form:
            attr_names.append("wins")
            attr_values.append(request.form["wins"])
        db.update_driver_standing(driver_standing_id, attr_names, attr_values)
        return redirect(url_for("driver_standings_page"))

def add_driver_standing_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("add_driver_standing.html")
    else:
        try:
            raceId = request.form["raceId"]
            driverId = request.form["driverId"]
            points = request.form["points"]
            position = request.form["position"]
            positionText = request.form["positionText"]
            wins = request.form["wins"]
            db.add_driver_standing(DriverStanding(0, raceId, driverId, points, position, positionText, wins))
        except:
            print(traceback.format_exc())
        finally:
            return redirect(url_for("driver_standings_page"))

# ============ RACES ============ #

def races_page():
    db = current_app.config["db"]
    if request.method == "GET":
        races = db.get_races()
        return render_template("races.html", races=races)
    else:
        race_ids = request.form.getlist("race_id")
        for race_id in race_ids:
            db.remove_race(race_id)
        return redirect(url_for("races_page"))

def update_race_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("update_race.html")
    else:
        race_id = request.form['race_id']
        attr_names = list()
        attr_values = list()
        if "raceYear" in request.form:
            attr_names.append("raceYear")
            attr_values.append(request.form["raceYear"])
        if "raceRound" in request.form:
            attr_names.append("raceRound")
            attr_values.append(request.form["raceRound"])
        if "circutId" in request.form:
            attr_names.append("circutId")
            attr_values.append(request.form["circutId"])
        if "raceName" in request.form:
            attr_names.append("raceName")
            attr_values.append(request.form["raceName"])
        if "raceDate" in request.form:
            attr_names.append("raceDate")
            attr_values.append(request.form["raceDate"])
        if "raceTime" in request.form:
            attr_names.append("raceTime")
            attr_values.append(request.form["raceTime"])
        if "raceUrl" in request.form:
            attr_names.append("raceUrl")
            attr_values.append(request.form["raceUrl"])
        if "fp1_date" in request.form:
            attr_names.append("fp1_date")
            attr_values.append(request.form["fp1_date"])
        if "fp1_time" in request.form:
            attr_names.append("fp1_time")
            attr_values.append(request.form["fp1_time"])
        if "fp2_date" in request.form:
            attr_names.append("fp2_date")
            attr_values.append(request.form["fp2_date"])
        if "fp2_time" in request.form:
            attr_names.append("fp2_time")
            attr_values.append(request.form["fp2_time"])
        if "fp3_date" in request.form:
            attr_names.append("fp3_date")
            attr_values.append(request.form["fp3_date"])
        if "fp3_time" in request.form:
            attr_names.append("fp3_time")
            attr_values.append(request.form["fp3_time"])
        if "quali_date" in request.form:
            attr_names.append("quali_date")
            attr_values.append(request.form["quali_date"])
        if "quali_time" in request.form:
            attr_names.append("quali_time")
            attr_values.append(request.form["quali_time"])
        if "sprint_date" in request.form:
            attr_names.append("sprint_date")
            attr_values.append(request.form["sprint_date"])
        if "sprint_time" in request.form:
            attr_names.append("sprint_time")
            attr_values.append(request.form["sprint_time"])
        db.update_race(race_id, attr_names, attr_values)
        return redirect(url_for("races_page"))

def add_race_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("add_race.html")
    else:
        try:
            raceYear = request.form["raceYear"]
            raceRound = request.form["raceRound"]
            circutId = request.form["circutId"]
            raceName = request.form["raceName"]
            raceDate = request.form["raceDate"]
            raceTime = request.form["raceTime"]
            raceUrl = request.form["raceUrl"]
            fp1_date = request.form["fp1_date"]
            fp1_time = request.form["fp1_time"]
            fp2_date = request.form["fp2_date"]
            fp2_time = request.form["fp2_time"]
            fp3_date = request.form["fp3_date"]
            fp3_time = request.form["fp3_time"]
            quali_date = request.form["quali_date"]
            quali_time = request.form["quali_time"]
            sprint_date = request.form["sprint_date"]
            sprint_time = request.form["sprint_time"]
            db.add_race(Race(0, raceYear, raceRound, circutId, raceName, raceDate, raceTime, raceUrl, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time))
        except:
            print(traceback.format_exc())
        finally:
            return redirect(url_for("races_page"))

# ============ LAP TIMES ============ #

def lap_times_page():
    db = current_app.config["db"]
    if request.method == "GET":
        lap_times = db.get_lap_times()
        return render_template("lap_times.html", lap_times=lap_times)
    else:
        lap_keys = request.form.getlist("lap_key")
        for lap_key in lap_keys:
            db.remove_lap_time(lap_key)
        return redirect(url_for("lap_times_page"))

def update_lap_time_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("update_lap_time.html")
    else:
        raceId = request.form['raceId']
        driverId = request.form['driverId']
        lap = request.form['lap']
        attr_names = list()
        attr_values = list()
        if "position" in request.form:
            attr_names.append("position")
            attr_values.append(request.form["position"])
        if "lapTime" in request.form:
            attr_names.append("lapTime")
            attr_values.append(request.form["lapTime"])
        if "milliseconds" in request.form:
            attr_names.append("milliseconds")
            attr_values.append(request.form["milliseconds"])
        db.update_lap_time(raceId, driverId, lap, attr_names, attr_values)
        return redirect(url_for("lap_times_page"))

def add_lap_time_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("add_lap_time.html")
    else:
        try:
            raceId = request.form["raceId"]
            driverId = request.form["driverId"]
            lap = request.form["lap"]
            position = request.form["position"]
            lapTime = request.form["lapTime"]
            milliseconds = request.form["milliseconds"]
            db.add_lap_time(LapTime(raceId, driverId, lap, position, lapTime, milliseconds))
        except:
            print(traceback.format_exc())
        finally:
            return redirect(url_for("lap_times_page"))