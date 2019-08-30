from geom_creation import Geometry_op
import numpy as np

from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb


class tetrahedrical(Geometry_op):
    """
    This class contains all necessary operations that apply to tetra-
    hydricals, i.e. structures that consist of triangle based pyramids.
    This class was created to allow isolation from other structures
    that inherit from geometry_op, such as cube based structures.
    This class also holds the build instruction set.
    """

    def __init__(self, name):
        """
        For now this just creates a default bone, all this will be
        changed later.
        """
        # initialize parent Geometry_op with given name
        super().__init__(name)

        # nested list containing structure of geom.
        # [0] : extension point number, [1] : name of face for extend,
        # [2] : barycentric coords , [3] : height of extension
        self.buildInstruct = []

        # WILL ADD VOLUME VARIABLE TO KEEP TRACK OF TOTAL GEOM VOLUME


    def build_struct(self, base_tri, build_instr):
        """
        """
        self.make_tri(base_tri)
        build_instr.sort()

        for extension in build_instr:

            # finds face that is given in extension[1]
            for face in self.f_list:
                if face[0] == extension[1]:
                    print(extension[1])
                    t_tri = face
                    print(face)

            # gets point on target face at given coords and height
            ext_p = self.extend_p(t_tri, extension[2][0],
                                     extension[2][1], extension[3])

            # make tri & append name to extension
            self.make_tri(["{}A".format(extension[0]),
                          face[1], face[2], ext_p])

            self.make_tri(["{}B".format(extension[0]),
                          face[2], face[3], ext_p])

            self.make_tri(["{}C".format(extension[0]),
                          face[3], face[1], ext_p])

            # self.flip_normals(self.f_list[0])
            # calc volume and add it to self.volume
            # remove face
            # add extension to self.buildInstruct



