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
        Succesively builds a structure based on a given build instruct.
        Currently this method does not delete any primitives or verts.
        """
        # base triangle "0" on which first extension will be performed
        self.make_tri(base_tri)
        build_instr.sort()
        # var for checking if base_tri should be flipped or kept
        check_0 = 0

        # loop through every instruction (extension) in the set
        for extension in build_instr:

            # finds face that is given in extension[1]
            for face in self.f_list:
                if face[0] == extension[1]:
                    t_tri = face

            # gets point on target face at given coords and height
            ext_p = self.extend_p(t_tri, extension[2][0],
                                     extension[2][1], extension[3])

            # make tri
            self.make_tri(["{}A".format(extension[0]),
                          t_tri[1], t_tri[2], ext_p])

            self.make_tri(["{}B".format(extension[0]),
                          t_tri[2], t_tri[3], ext_p])

            self.make_tri(["{}C".format(extension[0]),
                          t_tri[3], t_tri[1], ext_p])

            # check what to do with base_tri.
            if check_0 <= 2: # Has base_tri been extended twice?
                if extension[0] == 1: # is the extension positive?
                    self.make_tri(["02", t_tri[3], t_tri[2], t_tri[1]])
                    check_0 += 1 # make a new one with flipped face
                elif extension[0] == -1: # is it negative / downwards?
                    check_0 += 1

            # self.flip_normals(self.f_list[0])
            # calc volume and add it to self.volume
            # remove face
            # add extension to self.buildInstruct



