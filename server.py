from flask import Flask
import views

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule('/', view_func=views.home_page)
    app.add_url_rule('/drivers', view_func=views.drivers_page)
    app.add_url_rule('/seasons', view_func=views.seasons_page)
    app.add_url_rule('/driver_stangings', view_func=views.driver_standings_page)
    return app

app = create_app()
port = app.config.get("PORT", 5000)
app.run(host="0.0.0.0", port=port)
