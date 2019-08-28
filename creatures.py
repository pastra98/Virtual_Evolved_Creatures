from geom_creation import Geometry_op
from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb

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
        # self.skelleton.append(self.build_structure("bone1"))


class Bone(Geometry_op):
    """
    this class inherits from Geometry_op, and provides certain
    operations, that can be of use when creating the morphology of a
    creature. It also holds a collection of shapes, that can later be
    called upon
    """
    def __init__(self, name):
        """
        For now this just creates a default bone, all this will be
        changed later.
        """
        # initialize parent Geometry_op with given name
        super().__init__(name)
        p1 = cor.LPoint3f(0, 100, 0)
        p2 = cor.LPoint3f(10, 100, 0)
        p3 = cor.LPoint3f(0, 100, 10)
        self.base_tri = self.make_tri(["A", p1, p2, p3])



