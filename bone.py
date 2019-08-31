from tetrahedrical import tetrahedrical
from geom_creation import Geometry_op

from panda3d import core as cor

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
        # initializes tetrahedrical, which then passes name on to geom_
        # creation class, where name is used as name for vertex data.
        super().__init__(name)

        # must always be given in a counter-clockwise order
        base_triangle = ["0", cor.LPoint3f(0, 0, 0),
                              cor.LPoint3f(10, 0, 0),
                              cor.LPoint3f(0, 10, 0)]

        # nested list containing structure of geom.
        # [0]:extension point number, [1]:name of face for extend,
        # [2]:barycentric coords , [3]:height of extension, [4]:color
        # if [0] is -1, [1] must be "-0"
        build_instructions = [[1, "0", [0.3, 0.3], 5, "blue"],
                              [-1, "-0", [0.3, 0.3], 5, "blue"],
                              [-2, "-1A", [0.3, 0.3], 5, "blue"]]

        # invalid when [1]face_n is refered bef. corresp. [0]extension
        self.build_struct(base_triangle, build_instructions)


