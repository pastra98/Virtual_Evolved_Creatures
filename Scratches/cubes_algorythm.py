from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb

# initializing ShowBase class in order to get a scene graph and other stuff
base = shb.ShowBase()

class rect_prism:
    # class variables (shared by all cubes):
    # list containing all vert combins that make up the tris and norm in cube.
    # Using list, because it saves space & we will only iterate through this
    # list, not search through it. Also idkwid.
    vert_norm_order = [["a", "b", "c"], ["c", "d", "a"],
                       ["d", "c", "f"], ["f", "e", "d"],
                       ["e", "f", "g"], ["g", "h", "e"],
                       ["h", "g", "b"], ["b", "a", "h"],
                       ["a", "h", "e"], ["e", "d", "a"],
                       ["b", "g", "f"], ["f", "c", "b"]]

    # format for Vertex Data (contains vert, norm, and color [4compon, RGBA])
    c_f = cor.GeomVertexFormat.getV3n3c4()
    c_f = c_f.registerFormat(c_f) # registering & replacing

    # initialize, requiring the coordinates and a name
    def __init__(x_len, y_len, z_len, name):
        # # dimensions of cube --  DON'T THINK I'LL NEED THESE ANYMORE
        # self.x_len = x_len
        # self.y_len = y_len
        # self.z_len = z_len
        # vertex data of cube
        self.v_dat = cor.GeomVertexData("d_{}".format(name), c_f, geo.UHStatic)
        # vertex writers of cube
        self.ver_w = cor.GeomVertexWriter(self.v_dat, "vertex")
        self.nor_w = cor.GeomVertexWriter(self.v_dat, "normal")
        self.col_w = cor.GeomVertexWriter(self.v_dat, "color")
        # dict used for both addition and normals, normal data
        self.normd = {"x+" : [x_len, 0, 0], "x-" : [-x_len, 0, 0],
                      "y+" : [0, y_len, 0], "y-" : [0, -y_len, 0],
                      "z+" : [0, 0, z_len], "z-" : [0, 0, -z_len]}
        # generating vertices by adding our normal data
        for key, vert in [normd["z+"]]


# I will turn all of this into a class, and use loops, this is just a test,
# wether I can create a cube using tristrips. I'll also have to figure out how
# to automate the normals generating process
ver_vw.addData3f(0, 0, 0)
nor_vw.addData3f(0, 0, -1)
col_vw.addData3f(1, 0, 0)

ver_vw.addData3f(0, -1, 0)
nor_vw.addData3f(0, 0, -1)
col_vw.addData3f(1, 0, 0)

ver_vw.addData3f(1, 0, 0)
nor_vw.addData3f(0, 0, -1)
col_vw.addData3f(1, 0, 0)

ver_vw.addData3f(1, -1, 0)
nor_vw.addData3f(0, 0, -1)
col_vw.addData3f(1, 0, 0)

# creating a tstrips primitive
square_p = cor.GeomTristrips(geo.UHStatic)

# adding our vertices to the primitive
square_p.add_next_vertices(4)

# closing our primitive
square_p.closePrimitive()

# creating a square Geom
square_g = cor.Geom(cube_data)

# adding our square primitive
square_g.addPrimitive(square_p)

# making a node for our square
square_n = cor.GeomNode("square")

# adding our square to the newly created node
square_n.addGeom(square_g)

# creating a nodepath for our square and attaching it to render
square_np = render.attachNewNode(square_n)

# making our normals two-sided
square_np.setTwoSided(True)

# running the ShowBase class to keep the window open
base.run()
