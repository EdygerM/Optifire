from Reactor import Reactor
from Multiplexer import Multiplexer

MultiplexerParameters = {
    "SelectorPort": " ",
}

reactorLeftParameters = {
    "ReactorPosition": 1,
    "SelectorPort": "/dev/ttyUSB1",
    "ValvePort": "/dev/ttyUSB0",
    "volumeSyringe": 400,
    "volumeLoop": 200,
    "volumeFlush": 200,
    "flushTime": 1000  # ms
}

reactorCenterParameters = {
    "ReactorPosition": 2,
    "SelectorPort": " ",
    "ValvePort": " ",
    "volumeSyringe": 0,
    "volumeLoop": 0,
    "volumeFlush": 0,
    "flushTime": 0
}

reactorRightParameters = {
    "ReactorPosition": 3,
    "SelectorPort": " ",
    "ValvePort": " ",
    "volumeSyringe": 0,
    "volumeLoop": 0,
    "volumeFlush": 0,
    "flushTime": 0
}


class OptiFire:
    MAX_VOLUME = 1000  # [µL]

    def __init__(self):
        self._checkParameters()
        self.multiplexer = Multiplexer(MultiplexerParameters["SelectorPort"])
        self.reactorLeft = Reactor(reactorLeftParameters["SelectorPort"], reactorLeftParameters["ValvePort"])
        # self.reactorCenter = Reactor(reactorCenterParameters["SelectorPort"], reactorCenterParameters["ValvePort"])
        # self.reactorRight = Reactor(reactorRightParameters["SelectorPort"], reactorRightParameters["ValvePort"])

    def _launchReactor(self, reactor, parameters):
        self.multiplexer.move(parameters["ReactorPosition"])
        reactor.fillSyringe(parameters["volumeSyringe"])
        reactor.fillLoop(parameters["volumeLoop"])
        reactor.flushCanula(parameters["volumeFlush"], parameters["FlushTime"])
        reactor.fillNMRProbe()

    def _checkParameters(self):
        self._checkVolume(reactorLeftParameters)
        self._checkVolume(reactorCenterParameters)
        self._checkVolume(reactorRightParameters)

    def _checkVolume(self, parameters):
        if parameters["volumeSyringe"] < parameters["volumeLoop"]:
            raise Exception("The volume of the loop should be lower than the volume of the syringe")
        if parameters["volumeSyringe"] > self.MAX_VOLUME:
            raise Exception("Volume cannot be more than 1000 µL")

    def launchReactorLeft(self):
        self._launchReactor(self.reactorLeft, reactorLeftParameters)

    def launchReactorCenter(self):
        self._launchReactor(self.reactorCenter, reactorCenterParameters)

    def launchReactorRight(self):
        self._launchReactor(self.reactorRight, reactorRightParameters)

