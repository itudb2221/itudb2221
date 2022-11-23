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
