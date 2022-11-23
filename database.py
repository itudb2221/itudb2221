from models import *
import sqlite3 as sqlite

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile
    
    def addDriver(self, driver: Driver):
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO DRIVERS (driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
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
