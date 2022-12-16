from models import *
import sqlite3 as sqlite

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile
    # ============== Drivers Start =============== #
    def addDriver(self, driver: Driver): # Create
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO DRIVERS (driverId, driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    driver.driverId,
                    driver.driverRef,
                    driver.number,
                    driver.code,
                    driver.forename,
                    driver.surname,
                    driver.dob,
                    driver.nationality,
                    driver.url
                )
            )
            connection.commit()
    
    def get_drivers(self): # Read
        drivers = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM DRIVERS ORDER BY dob"
            cursor.execute(query)
            connection.commit()
            for driverId, driverRef, number, code, forename, surname, dob, nationality, url in cursor:
                drivers.append(Driver(driverId, driverRef, number, code, forename, surname, dob, nationality, url))
        return drivers

    def update_driver(self, driverId, attrNames, attrValues):
        if "driverId" in attrNames:
            print("Primary key cannot be updated.") # !!! Display message on screen later.
            return
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") # !!! Display message on screen later.
            return

        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE DRIVERS SET "
            for i in range(len(attrNames)):
                query += (f" {attrNames[i]} = {attrValues[i]},")
            query = query[:-1] + "WHERE driverId = %s"
            cursor.execute(query, driverId)



    def remove_driver(self, driverId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM DRIVERS WHERE (driverId = %s)"
            cursor.execute(query, driverId)
            connection.commit()




# ============== Drivers End =============== #

# ============== Seasons Start =============== #
    def addSeason(self, season: Season):
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO SEASONS (year, seasonUrl) VALUES (?, ?)"
            cursor.execute(
                query,
                (
                    season.year,
                    season.url,
                )
            )
            connection.commit()
        
# ============== Seasons End =============== #

# ============== Driver Standings Start =============== #
    def addDriverStanding(self, dst: DriverStanding):
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO DRIVER_STANDINGS (raceId, driverId, points, position, positionText, wins) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    dst.raceId,
                    dst.driverId,
                    dst.points,
                    dst.position,
                    dst.positionText,
                    dst.wins
                )
            )
            connection.commit()
# ============== Driver Standings End =============== #