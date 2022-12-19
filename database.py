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
                query += (f""" {attrNames[i]} = "{attrValues[i]}",""" if isinstance(attrValues[i], str) else f" {attrNames[i]} = {attrValues[i]},") if attrValues[i] != "" else ""
            query = query[:-1] + " WHERE (driverId = ?)"
            if query != "UPDATE DRIVERS SET WHERE (driverId = ?)":
                cursor.execute(query, (driverId,))

    def remove_driver(self, driverId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM DRIVERS WHERE (driverId = ?)"
            cursor.execute(query, (driverId,))
            connection.commit()

    def get_driver_by_id(self, driverId):
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM DRIVERS WHERE driverId = ? LIMIT 1"
            cursor.execute(query, (driverId,))
            connection.commit()
            
            for driverId, driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl in cursor:
                return Driver(driverId, driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl)

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
                query += (f""" {attrNames[i]} = "{attrValues[i]}",""" if isinstance(attrValues[i], str) else f" {attrNames[i]} = {attrValues[i]},") if attrValues[i] != "" else ""
            query = query[:-1] + "WHERE (constructorId = ?)"
            if query != "UPDATE CONSTRUCTORS SET WHERE (constructorId = ?)":
                cursor.execute(query, (constructorId,))

    def remove_constructor(self, constructorId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM CONSTRUCTORS WHERE (constructorId = ?)"
            cursor.execute(query, (constructorId,))
            connection.commit()
# ============== Constructors End ============== #

# ============== Circuits Start ============== #
    def add_circuit(self, circuit: Circuit): # Create
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
                query += (f""" {attrNames[i]} = "{attrValues[i]}",""" if isinstance(attrValues[i], str) else f" {attrNames[i]} = {attrValues[i]},") if attrValues[i] != "" else ""
            query = query[:-1] + "WHERE (circuitId = ?)"
            if query != "UPDATE CIRCUITS SET WHERE (circuitId = ?)":
                cursor.execute(query, (circuitId,))

    def remove_circuit(self, circuitId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM CIRCUITS WHERE (circuitId = ?)"
            cursor.execute(query, (circuitId,))
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
                query += (f""" {attrNames[i]} = "{attrValues[i]}",""" if isinstance(attrValues[i], str) else f" {attrNames[i]} = {attrValues[i]},") if attrValues[i] != "" else ""
            query = query[:-1] + "WHERE (seasonYear = ?)"
            if query != "UPDATE SEASONS SET WHERE (seasonYear = ?)":
                cursor.execute(query, (seasonYear,))

    def remove_season(self, seasonYear): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM SEASONS WHERE (seasonYear = ?)"
            cursor.execute(query, (seasonYear,))
            connection.commit()
# ============== Seasons End =============== #

# ============== Driver Standings Start =============== #
    def add_driver_standing(self, dst: DriverStanding): # Create
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
    
    def get_driver_standings(self): # Read
        driver_standings = list()
        import time
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM DRIVER_STANDINGS LIMIT 1000" # ORDER BY dob"
            cursor.execute(query)
            connection.commit()
            cursor2 = connection.cursor()
            for driverStandingsId, raceId, driverId, points, position, positionText, wins in cursor:
                cursor2.execute("SELECT raceYear, raceName from RACES WHERE (raceId = ?)", (raceId,))
                values = cursor2.fetchone()
                if not values:
                    continue
                raceYear, raceName = values
                cursor2.execute("SELECT forename, surname FROM DRIVERS WHERE (driverId = ?)", (driverId,))
                values = cursor2.fetchone()
                if not values:
                    continue
                forename, surname = values
                driver_standings.append(DriverStanding(driverStandingsId, [raceId, f"{raceYear} {raceName}"], [driverId, f"{forename} {surname}"], points, position, positionText, wins))
        return driver_standings

    def update_driver_standing(self, driverStandingsId, attrNames, attrValues): # Update
        if "driverStandingsId" in attrNames:
            print("Primary key cannot be updated.") # !!! Display message on screen later.
            return
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") # !!! Display message on screen later.
            return

        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE DRIVER_STANDINGS SET "
            for i in range(len(attrNames)):
                query += (f""" {attrNames[i]} = "{attrValues[i]}",""" if isinstance(attrValues[i], str) else f" {attrNames[i]} = {attrValues[i]},") if attrValues[i] != "" else ""
            query = query[:-1] + "WHERE (driverStandingsId = ?)"
            if query != "UPDATE DRIVER_STANDINGS SET WHERE (driverStandingsId = ?)":
                cursor.execute(query, (driverStandingsId,))

    def remove_driver_standing(self, driverStandingsId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM DRIVER_STANDINGS WHERE (driverStandingsId = ?)"
            cursor.execute(query, (driverStandingsId,))
            connection.commit()

# ============== Driver Standings End =============== #

# ============== RACES START ============== #
    def add_race(self, races: Race):
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO RACES (raceYear, raceRound, circuitId, raceName, raceDate, raceTime, raceUrl, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    races.raceYear,
                    races.raceRound,
                    races.circutId,
                    races.raceName,
                    races.raceDate,
                    races.raceTime,
                    races.raceUrl,
                    races.fp1_date,
                    races.fp1_time,
                    races.fp2_date,
                    races.fp2_time,
                    races.fp3_date,
                    races.fp3_time,
                    races.quali_date,
                    races.quali_time,
                    races.sprint_date,
                    races.sprint_time
                )
            )
            connection.commit()
    
    def get_races(self): # Read
        races = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM RACES" # ORDER BY dob"
            cursor.execute(query)
            connection.commit()
            for raceId, raceYear, raceRound, circutId, raceName, raceDate, raceTime, raceUrl, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time in cursor:
                races.append(Race(raceId, raceYear, raceRound, circutId, raceName, raceDate, raceTime, raceUrl, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time))
        return races

    def update_race(self, raceId, attrNames, attrValues): # Update
        if "raceId" in attrNames:
            print("Primary key cannot be updated.") # !!! Display message on screen later.
            return
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") # !!! Display message on screen later.
            return

        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE RACES SET "
            for i in range(len(attrNames)):
                query += (f""" {attrNames[i]} = "{attrValues[i]}",""" if isinstance(attrValues[i], str) else f" {attrNames[i]} = {attrValues[i]},") if attrValues[i] != "" else ""
            query = query[:-1] + "WHERE (raceId = ?)"
            if query != "UPDATE RACES SET WHERE (raceId = ?)":
                cursor.execute(query, (raceId,))

    def remove_race(self, raceId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM RACES WHERE (raceId = ?)"
            cursor.execute(query, (raceId,))
            connection.commit()
# ============== RACES END ============== #


# ============== QUALIFYING START ============== #
    def add_qualifying(self, qualifying: Qualifying): # Create
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO QUALIFYING (qualifyId, raceId, driverId, constructorId, carNumber, position, q1, q2, q3) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    qualifying.qualifyId,
                    qualifying.raceId,
                    qualifying.driverId,
                    qualifying.constructorId,
                    qualifying.carNumber,
                    qualifying.position,
                    qualifying.q1,
                    qualifying.q2,
                    qualifying.q3
                )
            )
            connection.commit()
    
    def get_qualifying(self): # Read
        qualify = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM QUALIFYING"
            cursor.execute(query)
            connection.commit()
            for qualifyId, raceId, driverId, constructorId, carNumber, position, q1, q2, q3 in cursor:
                qualify.append(Q(qualifyId, raceId, driverId, constructorId, carNumber, position, q1, q2, q3))
        return qualify

    def update_qualifying(self, qualifyId, attrNames, attrValues): # Update
        if "qualifyId" in attrNames:
            print("Primary key cannot be updated.") # !!! Display message on screen later.
            return
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") # !!! Display message on screen later.
            return

        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE QUALIFYING SET "
            for i in range(len(attrNames)):
                query += (f" {attrNames[i]} = {attrValues[i]},")
            query = query[:-1] + "WHERE qualifyId = %s"
            cursor.execute(query, qualifyId)

    def remove_qualifying(self, qualifyId): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM QUALIFYING WHERE (qualifyId = %s)"
            cursor.execute(query, qualifyId)
            connection.commit()
# ============== QUALIFYING END ============== #

# ============== Sprint Results START ============== #

    def addSprintResults(self, spRes: SprintResults):

        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO SPRINT_RESULTS (raceId, driverId, constructorId, sp_number,grid,position,positionText,positionOrder,points,laps,sp_time,milliseconds,fastestLap,fastestLapTime,statusId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    spRes.raceId,
                    spRes.driverId,
                    spRes.constructorId,
                    spRes.sp_number,
                    spRes.grid,
                    spRes.position,
                    spRes.positionText,
                    spRes.positionOrder,
                    spRes.points,
                    spRes.laps,
                    spRes.sp_time,
                    spRes.milliseconds,
                    spRes.fastestLap,
                    spRes.fastestLapTime,
                    spRes.statusId
                )
            )
            connection.commit()

    def getSprintResults(self): 
        sprint_results = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM SPRINT_RESULTS" 
            cursor.execute(query)
            connection.commit()
            for sprintResultId, raceId, driverId, constructorId, sp_number, grid, position, positionText, positionOrder, points,laps, sp_time, milliseconds, fastestLap, fastestLapTime, statusId in cursor:
                sprint_results.append(SprintResults(printResultId, raceId, driverId, constructorId, sp_number, grid, position, positionText, positionOrder, points,laps, sp_time, milliseconds, fastestLap, fastestLapTime, statusId))
        return sprint_results

    def updateSprintResults(self, sprintResultId, attrNames, attrValues):
        if "sprintResultId" in attrNames:
            print("Primary key cannot be updated.") 
            return
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") 
            return
        
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE SPRINT_RESULTS SET "
            for i in range(len(attrNames)):
                query += (f" {attrNames[i]} = {attrValues[i]},")
            query = query[:-1] + "WHERE sprintResultId = %s"
            cursor.execute(query, sprintResultId)

    def removeSprintResults(self, sprintResultId): 
        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM SPRINT_RESULTS WHERE (sprintResultId = %s)"
            cursor.execute(query, sprintResultId)
            connection.commit()
# ============== Sprint Results END ============== #

# ============== Lap Times START ============== #
    def add_lap_time(self, lap_time: LapTime): # Create
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO LAP_TIMES (raceId, driverId, lap, position, lapTime, milliseconds) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    lap_time.raceId,
                    lap_time.driverId,
                    lap_time.lap,
                    lap_time.position,
                    lap_time.lapTime,
                    lap_time.milliseconds
                )
            )
            connection.commit()
    
    def get_lap_times(self): # Read
        lap_times = list()
        with(sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM LAP_TIMES LIMIT 10000"
            cursor.execute(query)
            connection.commit()
            cursor2 = connection.cursor()
            for raceId, driverId, lap, position, lapTime, milliseconds in cursor:
                cursor2.execute("SELECT raceYear, raceName from RACES WHERE (raceId = ?)", (raceId,))
                values = cursor2.fetchone()
                if not values:
                    continue
                raceYear, raceName = values
                cursor2.execute("SELECT forename, surname FROM DRIVERS WHERE (driverId = ?)", (driverId,))
                values = cursor2.fetchone()
                if not values:
                    continue
                forename, surname = values
                lap_times.append(LapTime([raceId, f"{raceYear} {raceName}"], [driverId, f"{forename} {surname}"], lap, position, lapTime, milliseconds))
        return lap_times

    def update_lap_time(self, raceId, driverId, lap, attrNames, attrValues): # Update
        if (len(attrNames) != len(attrValues)) or not len(attrNames):
            print("Invalid input. ") # !!! Display message on screen later.
            return

        with (sqlite.connect(self.dbfile)) as connection:
            cursor = connection.cursor()
            query = "UPDATE LAP_TIMES SET "
            for i in range(len(attrNames)):
                query += (f""" {attrNames[i]} = "{attrValues[i]}",""" if isinstance(attrValues[i], str) else f" {attrNames[i]} = {attrValues[i]},") if attrValues[i] != "" else ""
            query = query[:-1] + "WHERE ((raceId, driverId, lap) = (?, ?, ?))"
            if query != "UPDATE LAP_TIMES SET WHERE ((raceId, driverId, lap) = (?, ?, ?))":
                cursor.execute(query, (raceId, driverId, lap))

    def remove_lap_time(self, lap_key): # Delete
        with (sqlite.connect(self.dbfile)) as connection:
            raceId, driverId, lap = (lap_key[1:-1]).split(',')
            cursor = connection.cursor()
            query = "DELETE FROM LAP_TIMES WHERE ((raceId, driverId, lap) = (?, ?, ?))"
            cursor.execute(query, (raceId, driverId, lap))
            connection.commit()

# ============== Lap Times END ============== #


# ============== CONSTRUCTORS START ============== #
    def addConstructors(self, cst: Constructor):
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO CONSTRUCTORS (constructorId, constructorRef, constructorName, nationality, constructorUrl) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(
                query,
                (
                    cst.constructorId,
                    cst.constructorRef,
                    cst.name,
                    cst.nationality,
                    cst.url
                )
            )
            connection.commit()
# ============== CONSTRUCTORS END ============== #

# ============== PIT STOPS START ============== #

    def addPitStop(self, raceId, driverId, stop, lap, time, duration, milliseconds):

        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO PIT_STOPS (raceId, driverId, stop, lap, time, duration, milliseconds) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (raceId, driverId, stop, lap, time, duration, milliseconds))
            connection.commit()

    def getPitStops(self):
        pit_stops = []

        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PIT_STOPS ORDER BY raceId, time LIMIT 100"
            cursor.execute(query)
            connection.commit()
            
            for raceId, driverId, stop, lap, time, duration, milliseconds in cursor:
                pit_stops.append(PitStop(raceId, driverId, stop, lap, time, duration, milliseconds))

        return pit_stops

    def deletePitStop(self, raceId, driverId, time):
        with sqlite.connect(self.dbfile) as connection:
            print(raceId, driverId, time)
            cursor = connection.cursor()
            query = "DELETE FROM PIT_STOPS WHERE raceId = ? AND driverId = ? and time = ?"
            cursor.execute(query, (raceId, driverId, time,))
            connection.commit()

    def updatePitStop(self, raceId, driverId, time, updatedRaceId, updatedDriverId, updatedStop, updatedLap, updatedTime, updatedDuration, updatedMilliseconds):
        with sqlite.connect(self.dbfile) as connection:
            print(raceId, driverId, time)
            cursor = connection.cursor()
            query = "UPDATE PIT_STOPS SET raceId = ?, driverId=?, stop=?, lap=?, time=?, duration=?, milliseconds=? WHERE raceId=? AND driverId=? and time=?"
            cursor.execute(query, (updatedRaceId, updatedDriverId, updatedStop, updatedLap, updatedTime, updatedDuration, updatedMilliseconds, raceId, driverId, time))
            connection.commit()

    def getPitStopByRaceIdAndDriverIdAndTime(self, raceId, driverId, time):
        with sqlite.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PIT_STOPS WHERE raceId = ? AND driverId = ? AND time = ? LIMIT 1"
            cursor.execute(query, (raceId, driverId, time,))
            connection.commit()
            
            for raceId, driverId, stop, lap, time, duration, milliseconds in cursor:
                return PitStop(raceId, driverId, stop, lap, time, duration, milliseconds)

# ============== PIT STOPS END ============== #

