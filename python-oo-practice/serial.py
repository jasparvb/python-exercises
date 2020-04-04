"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.increment = 0
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"

    def generate(self):
        """Returns current increment value added to start number and adds one to increment value."""
        serial = self.start + self.increment
        self.increment += 1
        return serial
    
    def reset(self):
        """Resets the increment value to 0"""
        self.increment = 0
