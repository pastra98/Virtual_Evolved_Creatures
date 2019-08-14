from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb
from geom_creation import Geometry_op

# init ShowBase class in order to get a scene graph and other stuff
base = shb.ShowBase()

class Creature(Geometry_op):
    """
    this class contains everything that has to do with creatures.
    """
    def __init__(self):
        """
        creates a list that stores every structure (like bones)
        and builds a first structure.
        """
        self.skelleton = []
        self.skelleton.append(self.build_structure("bone1"))

my_creature = Creature()
print(my_creature.skelleton)
