from tetrahedrical import tetrahedrical
from geom_creation import Geometry_op

from panda3d import core as cor

class Creature():
    """
    this class contains everything that has to do with creatures.
    """
    def __init__(self):
        """
        creates a list that stores every structure (like bones)
        and builds a first structure.
        """
        self.skelleton = []
        # self.skelleton.append(self.build_structure("bone1"))

