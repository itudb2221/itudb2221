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

class DriverStanding:
    def __init__(self, driverStandingsId, raceId, driverId, points, position, positionText, wins):
        self.driverStandingsId  = driverStandingsId
        self.raceId             = raceId
        self.driverId           = driverId
        self.points             = points
        self.position           = position
        self.positionText       = positionText
        self.wins               = wins
