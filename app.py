from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)
db = Database("database.db")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/drivers")
def drivers():
    drivers = db.get_drivers()
    return render_template("drivers.html", drivers=drivers)

@app.route("/seasons")
def seasons():
    return render_template("seasons.html")

@app.route("/driver_standings")
def driver_standings():
    return render_template("driver_standings.html")

@app.route("/pit_stops")
def pit_stops():
    pit_stops = db.getPitStops()
    return render_template("pit_stops.html", pit_stops=pit_stops)

@app.route("/pit_stops/add", methods=["POST"])
def add_pit_stop():
    if (request.method == "POST"):
        db.addPitStop(request.form["raceId"], request.form["driverId"], request.form["stop"], 
                    request.form["lap"], request.form["time"], request.form["duration"], request.form["milliseconds"])

        return pit_stops() 

@app.route("/pit_stops/delete/<identifier>", methods=["POST"])
def delete_pit_stops(identifier):
    raceId, driverId, time = identifier.split('-')
    db.deletePitStop(raceId, driverId, time)

    return pit_stops()

@app.route("/pit_stops/update/<identifier>", methods=["GET", "POST"])
def update_pit_stops(identifier):
    raceId, driverId, time = identifier.split('-')

    if (request.method == "POST"):
        db.updatePitStop(raceId, driverId, time, request.form["raceId"], request.form["driverId"], request.form["stop"], 
                        request.form["lap"], request.form["time"], request.form["duration"], request.form["milliseconds"])

        return pit_stops() 
    
    if (request.method == "GET"):
        pitstop = db.getPitStopByRaceIdAndDriverIdAndTime(raceId, driverId, time)

        return render_template("update_pitstop.html", pitstop=pitstop)
       

@app.route("/edit_tables")
def edit_tables_page():
    return render_template("edit_tables.html")

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8080)