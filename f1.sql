CREATE TABLE IF NOT EXISTS DRIVERS (
    driverId INTEGER PRIMARY KEY AUTOINCREMENT,
    driverRef VARCHAR(50) NOT NULL,
    driverNumber INTEGER,
    code VARCHAR(3),
    forename VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    dob DATE,
    nationality VARCHAR(50),
    driverUrl VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS CONSTRUCTORS (
    constructorId INTEGER PRIMARY KEY AUTOINCREMENT,
    constructorRef VARCHAR(50),
    constructorName VARCHAR(255),
    nationality VARCHAR(50),
    constructorUrl VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS CIRCUITS (
    circuitId INTEGER PRIMARY KEY AUTOINCREMENT,
    circuitRef VARCHAR(50),
    circuitName VARCHAR(255),
    circutitLocation VARCHAR(50),
    country VARCHAR(50),
    lat FLOAT,
    lng FLOAT,
    alt INTEGER,
    circuitUrl VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS SEASONS (
    seasonYear INTEGER PRIMARY KEY,
    seasonUrl VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS RACES (
    raceId INTEGER,
    raceYear INTEGER REFERENCES SEASONS (seasonYear) ON DELETE CASCADE ON UPDATE CASCADE,
    raceRound INTEGER,
    circutId INTEGER REFERENCES CIRCUITS (circuitId) ON DELETE CASCADE ON UPDATE CASCADE,
    raceName VARCHAR(255),
    raceDate DATE,
    raceTime TIME,
    raceUrl VARCHAR(50),
    fp1_date DATE,
    fp1_time TIME,
    fp2_date DATE,
    fp2_time TIME,
    fp3_date DATE,
    fp3_time TIME,
    quali_date DATE,
    quali_time TIME,
    sprint_date DATE,
    sprint_time TIME,
    PRIMARY KEY (raceId, raceYear)
);

CREATE TABLE IF NOT EXISTS STATUS_T (
    statusId INTEGER PRIMARY KEY AUTOINCREMENT,
    statusDef VARCHAR (255)
);

-- QUALIFYING HERE


CREATE TABLE IF NOT EXISTS SPRINT_RESULTS(
    sprintResultId INTEGER PRIMARY KEY AUTOINCREMENT,
    raceId INTEGER REFERENCES RACES (raceId) ON DELETE CASCADE ON UPDATE CASCADE,
    driverId INTEGER REFERENCES DRIVERS (driverId) ON DELETE CASCADE ON UPDATE CASCADE,
    constructorId INTEGER REFERENCES CONSTRUCTORS (constructorId) ON DELETE CASCADE ON UPDATE CASCADE,
    sp_number INTEGER,
    grid INTEGER,
    position INTEGER,
    positionText VARCHAR(255),
    positionOrder INTEGER,
    points FLOAT,
    laps INTEGER,
    sp_time VARCHAR(255),
    milliseconds INTEGER,
    fastestLap INTEGER,
    fastestLapTime VARCHAR(255),
    statusId INTEGER REFERENCES STATUS_T (statusId) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS RESULTS (
    resultId INTEGER PRIMARY KEY AUTOINCREMENT,
    raceId INTEGER REFERENCES RACES (raceId) ON DELETE CASCADE ON UPDATE CASCADE,
    driverId INTEGER REFERENCES DRIVERS (driverId) ON DELETE CASCADE ON UPDATE CASCADE,
    constructorId INTEGER REFERENCES CONSTRUCTORS (constructorId) ON DELETE CASCADE ON UPDATE CASCADE,
    raceNumber INTEGER,
    grid INTEGER,
    position INTEGER,
    positionText VARCHAR (2),
    positionOrder INTEGER,
    points FLOAT,
    laps INTEGER,
    resultTime VARCHAR (31),
    milliseconds INTEGER,
    fastestLap INTEGER,
    resultRank INTEGER,
    fastestLapTime VARCHAR (31),
    fastestLapSpeed VARCHAR (31),
    statusId INTEGER REFERENCES STATUS_T (statusId) ON DELETE CASCADE ON UPDATE CASCADE
);

-- PIT_STOPS HERE

CREATE TABLE IF NOT EXISTS LAP_TIMES (
    raceId INTEGER REFERENCES RACES (raceId) ON DELETE CASCADE ON UPDATE CASCADE,
    driverId INTEGER REFERENCES DRIVERS (driverId) ON DELETE CASCADE ON UPDATE CASCADE,
    lap INTEGER,
    position INTEGER,
    lapTime VARCHAR (8),
    milliseconds INTEGER,
    PRIMARY KEY (raceId, driverId, lap)
);

CREATE TABLE IF NOT EXISTS DRIVER_STANDINGS (
    driverStandingsId INTEGER PRIMARY KEY AUTOINCREMENT,
    raceId INTEGER REFERENCES RACES (raceId) ON DELETE CASCADE ON UPDATE CASCADE,
    driverId INTEGER REFERENCES DRIVERS (driverId) ON DELETE CASCADE ON UPDATE CASCADE,
    points FLOAT,
    position INTEGER,
    positionText VARCHAR(255),
    wins INTEGER
);

CREATE TABLE IF NOT EXISTS CONSTRUCTOR_STANDINGS (
    constructorStandingsId INTEGER PRIMARY KEY AUTOINCREMENT,
    raceId INTEGER REFERENCES RACES (raceId) ON DELETE CASCADE ON UPDATE CASCADE,
    constructorId INTEGER REFERENCES CONSTRUCTORS (constructorId) ON DELETE CASCADE ON UPDATE CASCADE,
    points FLOAT,
    position INTEGER,
    positionText VARCHAR(2),
    wins INTEGER
);

CREATE TABLE IF NOT EXISTS CONTRUCTOR_RESULTS (
    constructorResultsId INTEGER PRIMARY KEY AUTOINCREMENT,
    raceId INTEGER REFERENCES RACES (raceId) ON DELETE CASCADE ON UPDATE CASCADE,
    constructorId INTEGER REFERENCES CONSTRUCTORS (constructorId) ON DELETE CASCADE ON UPDATE CASCADE,
    points FLOAT,
    constructorStatus VARCHAR(31)
);