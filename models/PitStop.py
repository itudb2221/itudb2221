class PitStop:
    def __init__(self, raceId, driverId, stop, lap, time, duration, milliseconds) -> None:
        self.raceId         = raceId
        self.driverId       = driverId
        self.stop           = stop
        self.lap            = lap
        self.time           = time
        self.duration       = duration
        self.milliseconds   = milliseconds