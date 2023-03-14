from AMF import AMF
from PneumaticValve import PneumaticValve
from enum import Enum

# Selector positions (4 and 6 are not used)
selectorPos = {
    "reactor": 1,
    "flush": 2,
    "rinsingSolvent": 3,
    "valve": 5
}

valvePos = {
    "loopFill": 1,
    "NMRFill": 2
}


class Reactor:
    # Constants
    RVM_CONFIG = 6
    SPM_CONFIG = 6

    def __init__(self, selector_port: str, valve_port: str):
        self.selector = AMF(selector_port, self.SPM_CONFIG, 1, 1)
        self.valve = AMF(valve_port, self.RVM_CONFIG)
        self.NMRFill = PneumaticValve()
        self.flush = PneumaticValve()

    def fillSyringe(self, volume):
        # Safety controls
        self._checkNitrogen()

        # Process
        self.selector.switch(selectorPos["reactor"])
        self.selector.pump(volume)

    def fillLoop(self, volume):
        self._checkNitrogen()
        self.selector.switch(selectorPos["valve"])
        self.valve.switch(valvePos["loopFill"])
        self.selector.push(volume)

    def flushCanula(self, volume):
        self._checkNitrogen()
        self.selector.switch(selectorPos["reactor"])
        self.selector.homeSyringe()
        self.selector.switch(selectorPos["flush"])
        self.flush.open()
        self.selector.pump(volume)
        self.selector.switch(selectorPos["reactor"])
        self.selector.push(volume)

    def _checkNitrogen(self):
        if self.flush.isOpen():
            self.flush.close()

        if self.NMRFill.isOpen():
            self.NMRFill.close()
