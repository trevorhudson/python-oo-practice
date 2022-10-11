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
        '''initialize SerialGenerator with start value '''
        self.start = start
        self.last_serial = self.start - 1

    def generate(self):
        ''' increments counter +1. returns new number.'''
        self.last_serial += 1
        return self.last_serial

    def reset(self):
        ''' reset serial generator to initializing value'''
        self.last_serial = self.start






