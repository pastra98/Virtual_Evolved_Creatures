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

        # nested list containing structure of geom. First value
        # represents extension point number, second is which face it
        # applies to, third is the barycentric coords of the extension
        # point, and fourth is the height of the extension.
        self.buildInstruct = []

        # WILL ADD VOLUME VARIABLE TO KEEP TRACK OF TOTAL GEOM VOLUME


    def build_struct(self, base_tri, build_instr):
        """
        """
        self.make_tri(base_tri)
        build_instr.sort()

        for extension in build_instr:
            # will have to figure out how to use f_list
            ext_p = self.extend_p(self.f_list[0], extension[2][0],
                                     extension[2][1], extension[3])

            # make tri & append name to extension (ext = 1 build instr.)
            # names will also have to be fixed
            self.make_tri(["A",
                          self.f_list[0][1], self.f_list[0][2], ext_p])
            self.make_tri(["B",
                          self.f_list[0][2], self.f_list[0][3], ext_p])
            self.make_tri(["C",
                          self.f_list[0][3], self.f_list[0][1], ext_p])


            # calc volume and add it to self.volume
            # remove face
            # add extension to self.buildInstruct



