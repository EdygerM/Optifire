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


class OptiFire:
    MAX_VOLUME = 1000  # [µL]

    def __init__(self):
        self._checkParameters()
        self.multiplexer = Multiplexer(MultiplexerParameters["SelectorPort"])
        self.reactorLeft = Reactor(reactorLeftParameters["SelectorPort"], reactorLeftParameters["ValvePort"])

    def _launchReactor(self, reactor, parameters):
        self.multiplexer.move(parameters["ReactorPosition"])
        reactor.fillSyringe(parameters["volumeSyringe"])
        reactor.fillLoop(parameters["volumeLoop"])
        reactor.flushCanula(parameters["volumeFlush"], parameters["FlushTime"])

    def _checkParameters(self):
        self._checkVolume(reactorLeftParameters)

    def _checkVolume(self, parameters):
        if parameters["volumeSyringe"] < parameters["volumeLoop"]:
            raise Exception("The volume of the loop should be lower than the volume of the syringe")
        if parameters["volumeSyringe"] > self.MAX_VOLUME:
            raise Exception("Volume cannot be more than 1000 µL")

    def launchReactorLeft(self):
        self._launchReactor(self.reactorLeft, reactorLeftParameters)
