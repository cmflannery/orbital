#!/usr/bin/env python

""" orbital: a orbit and trajectory design and analysis tool """

from
class satellite():
    """ satellite is the base class used for for orbital design and analysis """
    def __init__(self, **kwargs):
        elements = kwargs

    def epoch():
        doc = "The epoch property."
        def fget(self):
            return self._epoch
        def fset(self, value):
            self._epoch = value
        def fdel(self):
            del self._epoch
        return locals()

    def ra():
        doc = "The epoch property."
        def fget(self):
            return self._epoch
        def fset(self, value):
            self._epoch = value
        def fdel(self):
            del self._epoch
        return locals()

epoch = property(**epoch())

if __name__ == '__main__':
    sat = orbit(pos=[0, 0, 0], vel=[0, 0, 0], epoch=TimeEpochDate.value)
