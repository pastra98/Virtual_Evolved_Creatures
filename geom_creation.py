import numpy as np
from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb


class Geometry_op:
    """
    This class contains basic operations on a single Geom. The 
    class Bone inherits from it.
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
        self.tri_prim.add_next_vertices(3)
        # close primitive
        self.tri_prim.closePrimitive()
        # adds primitive to geom
        self.b_geom.add_primitive(self.tri_prim)

        print(face)
        print(self.v_dat)
        return self.tri_prim



    def extend_structure(self, t_tri = 0, t_point = 0):
        """
        Operates on a given 3d_Struct, by creating 3 tris that extend
        from t_tri to t_point. WILL ALSO WORK DIFFERENTLY IN THE END!!!
        """
        pass


