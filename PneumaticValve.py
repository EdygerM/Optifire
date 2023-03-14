class PneumaticValve:
    CLOSED = 0
    OPEN = 1

    def __init__(self):
        self.status = self.CLOSED

    def close(self):
        self.status = self.CLOSED
        # TODO

    def open(self):
        self.status = self.OPEN
        # TODO

    def isClosed(self):
        if self.status == self.CLOSED:
            return True
        else:
            return False

    def isOpen(self):
        if self.status == self.OPEN:
            return True
        else:
            return False

