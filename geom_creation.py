import numpy as np

from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb


class Geometry_op:
    """
    This class contains basic operations on a single Geom. This class
    is parent to tetrahedrical (and later others), where most of the
    geometrical operations will actually happen.
    """
    # format for Vertex Data (position, normal, color)
    form3 = cor.GeomVertexFormat.get_v3n3c4()
    form3 = form3.registerFormat(form3) # registering & replacing

    # color list FIX DAT SHIT IT'S BROKEN!!!!!
    colors = {"red":(1., 0., 0., 1.), "green":(0., 1., 0., 1.),
              "blue":(1., 0., 0., 1.), "orange":(0.1, 0.5, 0., 1.)}



    def __init__(self, name):
        """
        Initializes vertex data, writers, and a Geom.
        """
        # vertex data
        self.v_dat = cor.GeomVertexData("d_{}".format(name),
                                        self.form3, geo.UHStatic)


        # vertex writers
        self.ver_w = cor.GeomVertexWriter(self.v_dat, "vertex")
        self.nor_w = cor.GeomVertexWriter(self.v_dat, "normal")
        self.col_w = cor.GeomVertexWriter(self.v_dat, "color")

        # create a Geom
        self.b_geom = cor.Geom(self.v_dat)

        # List containg all faces
        self.f_list = []
        self.deleteThis = 0


    def calc_normals(self, face):
        """
        Calculates normal vector to 3 given points, assuming they're
        on the same plane. Params must be of Type core.LPoint3f .
        Result is then appended to face array, making it 5th component.
        """
        n = np.cross(face[2] - face[1], face[3] - face[1])
        n = cor.LVector3f(n[0], n[1], n[2])
        n.normalize()

        face.append(n)
        return face


    def find_bary(self, face, u, v):
        """
        Returns the x, y and z coordinates of a Point, given a face,
        and two barycentric coordinates.
        """
        if u + v > 1:
            print("the sum of u and v should be <= 1")
        else:
            # calculates Barycentric and returns as P instead of vec
            return cor.LPoint3f(face[1] * u + face[2] * v
                                + face[3] * (1 - u - v))


    def extend_p(self, face, u, v, height):
        """
        Returns a new Point, that is the result of picking barycentric
        coordinates on a given face, and then multiplying the height
        with the normal vector.
        """
        return self.find_bary(face, u, v) + face[4] * height


    def make_tri(self, face, col="orange"):
        """
        Creates a triangle primitive, whose vertices are written
        onto geom_op object(this class). The 3 Points that make up the
        triangle are given as core.LPoint3f in a list (face).
        """
        # returns normal vector as list object
        self.calc_normals(face)
        # create a triangle primitive
        self.tri_prim = cor.GeomTriangles(geo.UHStatic)
        # succesively fill vertex data based on given params, and add
        # it to the tri_prim
        for point in face[1:4]:
            self.ver_w.add_data3f(point)
            self.nor_w.add_data3f(face[4])
            self.col_w.add_data4f(self.colors[col][0],
                                  self.colors[col][1],
                                  self.colors[col][2],
                                  self.colors[col][3],)

        # add vertices to triangle primitive
        self.tri_prim.addConsecutiveVertices(self.deleteThis, 3)
        self.deleteThis += 3
        print(self.deleteThis)
        # close primitive
        self.tri_prim.closePrimitive()
        # adds primitive to geom
        self.b_geom.add_primitive(self.tri_prim)
        # add reference of primitive to face
        face.append(self.tri_prim)
        # add face to face list for later reference
        self.f_list.append(face)

        return self.tri_prim


