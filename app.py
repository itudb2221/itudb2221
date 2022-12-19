from flask import Flask, render_template
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

@app.route("/edit_tables")
def edit_tables_page():
    return render_template("edit_tables.html")

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8080)