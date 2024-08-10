import warnings
warnings.filterwarnings('ignore')

from huygens.namespace import *
pink = color.rgba(1.0, 0.37, 0.36, 0.5)
grey = color.rgba(0.85, 0.85, 0.85, 0.5)
cream = color.rgba(1.0, 1.0, 0.92, 0.5)
cyan = color.rgba(0.0, 0.81, 0.80, 0.5)
yellow = color.rgba(1.0, 0.93, 0.4, 0.5)

from huygens.wiggle import Cell0, Cell1, Cell2
n = Cell0("n", fill=pink)
n
