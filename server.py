from flask import Flask
import views
from database import Database
def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule('/', view_func=views.home_page)
    app.add_url_rule('/drivers', view_func=views.drivers_page, methods=["GET", "POST"])
    app.add_url_rule('/updateDriver', view_func=views.update_driver_page, methods=["GET", "POST"])
    app.add_url_rule('/addDriver', view_func=views.add_driver_page, methods=["GET", "POST"])
    app.add_url_rule('/seasons', view_func=views.seasons_page)
    app.add_url_rule('/driverStandings', view_func=views.driver_standings_page, methods=["GET", "POST"])
    app.add_url_rule('/updateDriverStanding', view_func=views.update_driver_standing_page, methods=["GET", "POST"])
    app.add_url_rule('/addDriverStanding', view_func=views.add_driver_standing_page, methods=["GET", "POST"])
    app.add_url_rule('/races', view_func=views.races_page, methods=["GET", "POST"])
    app.add_url_rule('/addRace', view_func=views.add_race_page, methods=["GET", "POST"])
    app.add_url_rule('/updateRace', view_func=views.update_race_page, methods=["GET", "POST"])
    app.add_url_rule('/pitStops', view_func=views.pit_stops, methods=["GET"])
    app.add_url_rule('/pitStops/add', view_func=views.add_pit_stop, methods=["POST"])
    app.add_url_rule('/pit_stops/delete/<identifier>', view_func=views.delete_pit_stop, methods=["POST"])



    return app

app = create_app()

db = Database("database.db")
app.config["db"] = db

port = app.config.get("PORT", 5000)
app.run(host="0.0.0.0", port=port)
