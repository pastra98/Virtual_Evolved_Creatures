from panda3d import core as cor
from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb

# initiating ShowBase class in order to get a scene graph
base = shb.ShowBase()

# basic array format (its basic af, really), for 3 columns
basicaf = cor.GeomVertexArrayFormat()

# adding every apropriate column to our format
basicaf.addColumn("vertex", 3, geo.NTFloat32, geo.CPoint)
basicaf.addColumn("normal", 3, geo.NTFloat32, geo.CVector)
basicaf.addColumn("color", 3, geo.NTFloat32, geo.CColor)

# creating a vertex format, in which we will soon insert our array format
basicf = cor.GeomVertexFormat()

# inserting our Array format into the vertex format
basicf.addArray(basicaf)

# registering the vertex format, by replacing it with a registered version
basicf = basicf.registerFormat(basicf)

# creating a VertexData object
cube_data = cor.GeomVertexData("cdata", basicf, geo.UHStatic)

# creating writer Objects for each vertices, normals and color
ver_vw = cor.GeomVertexWriter(cube_data, "vertex")
nor_vw = cor.GeomVertexWriter(cube_data, "normal")
col_vw = cor.GeomVertexWriter(cube_data, "color")

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
