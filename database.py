from models import *
import sqlite3 as sqlite

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile
# ============== Drivers Start =============== #
    def add_driver(self, driver: Driver): # Create
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO DRIVERS (driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    driver.driverRef,
                    driver.driverNumber,
                    driver.code,
                    driver.forename,
                    driver.surname,
                    driver.dob,
                    driver.nationality,
                    driver.driverUrl
                )
            )
            connection.commit()
    
    def get_drivers(self): # Read
        drivers = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM DRIVERS" # ORDER BY dob"
            cursor.execute(query)
            connection.commit()
            for driverId, driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl in cursor:
                drivers.append(Driver(driverId, driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl))
        return drivers

    def update_driver(self, driverId, attrNames, attrValues): # Update
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

# ============== Constructors Start ============== #
    def add_constructor(self, constructor: Constructor): # Create
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO CONSTRUCTORS (constructorId, constructorRef, constructorName, nationality, constructorUrl) VALUES (?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    constructor.constructorRef,
                    constructor.constructorName,
                    constructor.nationality,
                    constructor.constructorUrl
                )
            )
            connection.commit()
    
    def get_constructors(self): # Read
        constructors = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM CONSTRUCTORS" # ORDER BY dob"
            cursor.execute(query)
            connection.commit()
            for constructorId, constructorRef, constructorName, nationality, constructorUrl in cursor:
                constructors.append(Constructor(constructorId, constructorRef, constructorName, nationality, constructorUrl))
        return constructors

    def update_constructor(self, constructorId, attrNames, attrValues): # Update
        if "constructorId" in attrNames:
            print("Primary key cannot be updated.") # !!! Display message on screen later.
            return
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") # !!! Display message on screen later.
            return

        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE CONSTRUCTORS SET "
            for i in range(len(attrNames)):
                query += (f" {attrNames[i]} = {attrValues[i]},")
            query = query[:-1] + "WHERE constructorId = %s"
            cursor.execute(query, constructorId)

    def remove_constructor(self, constructorId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM CONSTRUCTORS WHERE (constructorId = %s)"
            cursor.execute(query, constructorId)
            connection.commit()
# ============== Constructors End ============== #

# ============== Circuits Start ============== #
    def add_circuit(self, circuit: Constructor): # Create
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO CIRCUITS (circuitRef, circuitName, circutitLocation, country, lat, lng, alt, circuitUrl) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    circuit.circuitRef,
                    circuit.circuitName,
                    circuit.circutitLocation,
                    circuit.country,
                    circuit.lat,
                    circuit.lng,
                    circuit.alt,
                    circuit.circuitUrl
                )
            )
            connection.commit()
    
    def get_circuits(self): # Read
        circuits = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM CIRCUITS" # ORDER BY dob"
            cursor.execute(query)
            connection.commit()
            for circuitId, circuitRef, circuitName, circutitLocation, country, lat, lng, alt, circuitUrl in cursor:
                circuits.append(Circuit(circuitId, circuitRef, circuitName, circutitLocation, country, lat, lng, alt, circuitUrl))
        return circuits

    def update_circuit(self, circuitId, attrNames, attrValues): # Update
        if "circuitId" in attrNames:
            print("Primary key cannot be updated.") # !!! Display message on screen later.
            return
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") # !!! Display message on screen later.
            return

        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE CIRCUITS SET "
            for i in range(len(attrNames)):
                query += (f" {attrNames[i]} = {attrValues[i]},")
            query = query[:-1] + "WHERE circuitId = %s"
            cursor.execute(query, circuitId)

    def remove_circuit(self, circuitId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM CIRCUITS WHERE (circuitId = %s)"
            cursor.execute(query, circuitId)
            connection.commit()
# ============== Circuits End ============== #


# ============== Seasons Start =============== #
    def addSeason(self, season: Season):
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO SEASONS (seasonYear, seasonUrl) VALUES (?, ?)"
            cursor.execute(
                query,
                (
                    season.seasonYear,
                    season.seasonUrl,
                )
            )
            connection.commit()
    
    def get_seasons(self): # Read
        seasons = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM SEASONS" # ORDER BY dob"
            cursor.execute(query)
            connection.commit()
            for seasonYear, seasonUrl in cursor:
                seasons.append(Season(seasonYear, seasonUrl))
        return seasons

    def update_season(self, seasonYear, attrNames, attrValues): # Update
        if "seasonYear" in attrNames:
            print("Primary key cannot be updated.") # !!! Display message on screen later.
            return
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") # !!! Display message on screen later.
            return

        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE SEASONS SET "
            for i in range(len(attrNames)):
                query += (f" {attrNames[i]} = {attrValues[i]},")
            query = query[:-1] + "WHERE seasonYear = %s"
            cursor.execute(query, seasonYear)

    def remove_season(self, seasonYear): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM SEASONS WHERE (seasonYear = %s)"
            cursor.execute(query, seasonYear)
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

# ============== RACES START ============== #
# Add AUTOINCREMENT property manually.
# ============== RACES END ============== #