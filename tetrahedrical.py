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

        # keeps track of the total geom volume
        self.geom_vol = 0


    def volume_tetrahed(self, t_tri, ext_p):
        """
        Returns area of a tetrahedron, given the base, and top point.
        Method: Calculates vol of parallelepiped, divides by 6.
        """
        # find cross product of the two base vectors, returns np.array
        c_prod = np.cross(t_tri[2] - t_tri[1], t_tri[3] - t_tri[1])

        vol = (np.dot(c_prod, (ext_p - t_tri[1])) / 6)
        self.geom_vol += vol


    def build_struct(self, base_tri, build_instr):
        """
        Succesively builds a structure based on a given build instruct.
        Currently this method does not delete any primitives or verts.
        """
        # base triangle "0" on which first extension will be performed
        self.make_tri(base_tri)

        # make reversed base tri for downwards extension
        self.make_tri(["-0", base_tri[3], base_tri[2], base_tri[1]])

        # loop through every instruction (extension) in the set
        for extension in build_instr:

            # finds face that is given in extension[1]
            for face in self.f_list:
                if face[0] == extension[1]:
                    t_tri = face

            # gets point on target face at given coords and height
            ext_p = self.extend_p(t_tri, extension[2][0],
                                         extension[2][1], extension[3])

            # generate 3 tris from t_tri to ext_p
            self.make_tri(["{}A".format(extension[0]),
                            t_tri[1], t_tri[2], ext_p])

            self.make_tri(["{}B".format(extension[0]),
                            t_tri[2], t_tri[3], ext_p])

            self.make_tri(["{}C".format(extension[0]),
                            t_tri[3], t_tri[1], ext_p])


            # Calculate volume of extension and add it to self.geom_vol
            self.volume_tetrahed(t_tri, ext_p)

