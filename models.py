class Driver:
    def __init__(self, driverId, driverRef, driverNumber, code, forename, surname, dob, nationality, driverUrl) -> None:
        self.driverId       = driverId
        self.driverRef      = driverRef
        self.driverNumber   = driverNumber
        self.code           = code
        self.forename       = forename
        self.surname        = surname
        self.dob            = dob
        self.nationality    = nationality
        self.driverUrl      = driverUrl

class Constructor:
    def __init__(self, constructorId, constructorRef, constructorName, nationality, constructorUrl) -> None:
        self.constructorId      = constructorId
        self.constructorRef     = constructorRef
        self.constructorName    = constructorName
        self.nationality        = nationality
        self.constructorUrl     = constructorUrl

class Circuit:
    def __init__(self, circuitId, circuitRef, circuitName, circutitLocation, country, lat, lng, alt, circuitUrl) -> None:
        self.circuitId          = circuitId
        self.circuitRef         = circuitRef
        self.circuitName        = circuitName
        self.circutitLocation   = circutitLocation
        self.country            = country
        self.lat                = lat
        self.lng                = lng
        self.alt                = alt
        self.circuitUrl         = circuitUrl

class Season:
    def __init__(self, seasonYear, seasonUrl):
        self.seasonYear = seasonYear
        self.seasonUrl  = seasonUrl

class Race:
    def __init__(self, raceId, raceYear, raceRound, circutId, raceName, raceDate, raceTime, raceUrl, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time):
        self.raceId      = raceId
        self.raceYear    = raceYear
        self.raceRound   = raceRound
        self.circutId    = circutId
        self.raceName    = raceName
        self.raceDate    = raceDate
        self.raceTime    = raceTime
        self.raceUrl     = raceUrl
        self.fp1_date    = fp1_date
        self.fp1_time    = fp1_time
        self.fp2_date    = fp2_date
        self.fp2_time    = fp2_time
        self.fp3_date    = fp3_date
        self.fp3_time    = fp3_time
        self.quali_date  = quali_date
        self.quali_time  = quali_time
        self.sprint_date = sprint_date
        self.sprint_time = sprint_time

class DriverStanding:
    def __init__(self, driverStandingsId, raceId, driverId, points, position, positionText, wins):
        self.driverStandingsId  = driverStandingsId
        self.raceId             = raceId
        self.driverId           = driverId
        self.points             = points
        self.position           = position
        self.positionText       = positionText
        self.wins               = wins

class SprintResults:
    def __init__(self, sprintResultId ,raceId,driverId,constructorId,sp_number ,grid,position,positionText,positionOrder,points,laps,sp_time ,milliseconds,fastestLap,fastestLapTime,statusId):
        self.sprintResultId  = sprintResultId 
        self.raceId = raceId
        self.driverId = driverId
        self.constructorId = constructorId
        self.sp_number  = sp_number 
        self.grid = grid
        self.position = position
        self.positionText = positionText
        self.positionOrder = positionOrder
        self.points = points
        self.laps = laps
        self.sp_time  = sp_time 
        self.milliseconds = milliseconds
        self.fastestLap = fastestLap
        self.fastestLapTime = fastestLapTime
        self.statusId = statusId

class Qualifying:
    def __init__(self, qualifyingId, raceId, driverId, constructorId, carNumber, position, q1, q2, q3) -> None:
        self.qualifyingId   = qualifyingId
        self.raceId         = raceId
        self.driverId       = driverId
        self.constructorId  = constructorId
        self.carNumber      = carNumber
        self.position       = position
        self.q1             = q1
        self.q2             = q2
        self.q3             = q3

<<<<<<< HEAD
class PitStop:
    def __init__(self, raceId, driverId, stop, lap, time, duration, milliseconds) -> None:
        self.raceId         = raceId
        self.driverId       = driverId
        self.stop           = stop
        self.lap            = lap
        self.time           = time
        self.duration       = duration
        self.milliseconds   = milliseconds
=======
class LapTime:
    def __init__(self, raceId, driverId, lap, position, lapTime, milliseconds):
        self.raceId = raceId
        self.driverId = driverId
        self.lap = lap
        self.position = position
        self.lapTime = lapTime
        self.milliseconds = milliseconds
>>>>>>> origin/main
