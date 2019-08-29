from tetrahedrical import tetrahedrical
from geom_creation import Geometry_op

from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb

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


class Bone(tetrahedrical):
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
        super().__init__(name)
        base_triangle = ["0", cor.LPoint3f(0, 0, 0),
                              cor.LPoint3f(10, 0, 0),
                              cor.LPoint3f(0, 10, 0)]

        build_instructions = [[1, "0", [0.3, 0.3], 5]]

        self.build_struct(base_triangle, build_instructions)


