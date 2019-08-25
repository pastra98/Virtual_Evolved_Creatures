import numpy as np
from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb

# init ShowBase class in order to get a scene graph and other stuff
base = shb.ShowBase()

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


    def calc_normals(self, p1, p2, p3):
        """
        Calculates normal vector to 3 given points, assuming they're
        on the same plane. Still lacks decision for correct direction.
        """
        n = np.cross(np.array(p2) - np.array(p1),
                     np.array(p3) - np.array(p1))

        return np.ndarray.tolist(n)


    def make_tri(self, p1, p2, p3, col="orange"):
        """
        Creates a triangle primitive, whose vertices are written
        onto 3d_Struct objects. Parameters p1, p2, p3 are given as a
        list, with x, y and z coordinates.
        """
        # returns normal vector as list object
        n = self.calc_normals(p1, p2, p3)
        # create list of points for looping through them
        tri_points = [p1, p2, p3]
        # create a triangle primitive
        self.tri_prim = cor.GeomTriangles(geo.UHStatic)
        # succesively fill vertex data based on given params, and add
        # it to the tri_prim
        for point in tri_points:
            self.ver_w.add_data3f(point[0], point[1], point[2])
            self.nor_w.add_data3f(n[0], n[1], n[2])
            self.col_w.add_data4f(self.colors[col][0],
                                  self.colors[col][1],
                                  self.colors[col][2],
                                  self.colors[col][3],)

        # add vertices to triangle primitive
        self.tri_prim.add_next_vertices(3)

        self.tri_prim.closePrimitive()
        print(self.v_dat)
        return self.tri_prim


    def build_structure(self):
        """
        This method returns a new 3d simplex consisting of 4 Vertices
        and 4 faces. ACTUALLY, THIS METHOD DOESN'T DO ANYTHING 
        IMPORTANT RIGHT NOW!!!!!!
        """
        self.dreieck = self.make_tri([0, 100, 0], [10, 100, 0], [0, 100, 10])
        self.b_geom.add_primitive(self.dreieck)



    def extend_structure(self, t_tri = 0, t_point = 0):
        """
        Operates on a given 3d_Struct, by creating 3 tris that extend
        from t_tri to t_point. WILL ALSO WORK DIFFERENTLY IN THE END!!!
        """
        pass


# THE FOLLOWING LINES WILL ALSO NOT BE INCLUDED VERY SOON!!!
my_triangle = Geometry_op("Test1")
my_triangle.build_structure()

# creating a nodepath
Node = cor.GeomNode("cube1")

# adding our triangle to the newly created node
Node.addGeom(my_triangle.b_geom)

# creating a nodepath for our cube and attaching it to render
NodePath = render.attachNewNode(Node)

base.run()
