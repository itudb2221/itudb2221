from flask import Flask
import views
from database import Database
def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule('/', view_func=views.home_page)
    app.add_url_rule('/drivers', view_func=views.drivers_page)
    app.add_url_rule('/seasons', view_func=views.seasons_page)
    app.add_url_rule('/driver_standings', view_func=views.driver_standings_page)
    app.add_url_rule('/edit_tables', view_func=views.edit_tables_page)
    app.add_url_rule('/sprintResults', view_func=views.sprint_results_page(), methods=["GET", "POST"])
    app.add_url_rule('/updateSprintResults', view_func=views.update_sprint_results_page(), methods=["GET", "POST"])
    app.add_url_rule('/addSprintResults', view_func=views.add_sprint_results_page(), methods=["GET", "POST"])
    return app

app = create_app()

db = Database("database.db")
app.config["db"] = db

port = app.config.get("PORT", 5000)
app.run(host="0.0.0.0", port=port)
