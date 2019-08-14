from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb



class Geometry_op:
    """
    this class will hold all the information for the creation &
    modification of 3d objects.
    """
    # format for Vertex Data (contains vert and color [4compon, RGBA])
    form3 = cor.GeomVertexFormat.get_v3n3c4()
    form3 = form3.registerFormat(form3) # registering & replacing
    
    def build_structure(self, name):
        """
        this method returns a new 3d simplex consisting of 4 Vertices
        and 4 faces. This object must store all its belonging vertex
        data. All modifiying operations such as extend_structure will
        be performed on the 3d_Struct object this method creates.
        """
        self.v_dat = cor.GeomVertexData("d_{}".format(name),
                                        self.form3, geo.UHStatic)
        return str(name + "is a structure")

    def extend_structure(self, d_Struct, t_tri, t_point):
        """
        operates on a given 3d_Struct, by creating 3 tris that extend
        from t_tri to t_point.
        """
        pass

    def make_tri(self, d_Struct, p1, p2, p3):
        """
        creates a triangle, whose vertices are written onto 3d_Struct
        object.
        """
        pass

    def calc_normals(p1, p2, p3):
        """
        calculates normal vector to 3 given points, assuming they're
        on the same plane.
        """
        pass
