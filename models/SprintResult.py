class SprintResult:
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