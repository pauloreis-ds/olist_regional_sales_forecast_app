import os


class Directory:
    def __init__(self, __file__):
        self.__file__ = __file__
        self.THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.MODEL_DIR = os.path.join(os.path.join(self.BASE_DIR, 'model'))

    def __str__(self):
        return f'''Directory(__file__ = {self.__file__},
        THIS_DIR = {self.THIS_DIR},
        BASE_DIR = {self.BASE_DIR},
        MODEL_DIR = {self.MODEL_DIR})'''


def translate_region(region):
    pt_en_regions = {
        'centro oeste': 'midwest',
        'norte': 'north',
        'nordeste': 'northeast',
        'sul': 'south',
        'sudeste': 'southeast'
    }
    try:
        return pt_en_regions[region]
    except:
        return region