class FigureColor:
    def __init__(self):
        self._color = None
    
    @property
    def colorproperty(self):
        return self._color

    @colorproperty.setter
    def colorproperty(self, val):
        self._color = val

    @colorproperty.deleter
    def colorproperty(self):
        del self._color
