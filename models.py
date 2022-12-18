class Driver:
    def __init__(self, driverId, driverRef, number, code, forename, surname, dob, nationality, url):
        self.driverId       = driverId
        self.driverRef      = driverRef
        self.number         = number
        self.code           = code
        self.forename       = forename
        self.surname        = surname
        self.dob            = dob
        self.nationality    = nationality
        self.url            = url

class Season:
    def __init__(self, year, url):
        self.year = year
        self.url  = url

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
    