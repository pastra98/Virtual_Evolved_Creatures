from direct.showbase.ShowBase import ShowBase as shb
import panda3d.core as pan

# this line calls the ShowBase class, thus creating a ShowBase object with all
# its implications including creating a node path, with render as its root.
# NEEDS MORE DISCRIPTIONS!!!!
base = shb()

# creating an array for a GeomVertexArray Format:
arr1 = pan.GeomVertexArrayFormat()

#creating a Format to later add my arrays to:
format1 = pan.GeomVertexFormat()

# adding column to our array, specifying that the first column in arr1 is going
# to be for vertices.
arr1.addColumn("vertex", 3, pan.Geom.NTFloat32, pan.Geom.CPoint)

# adding a second column that will contain color information, using 4 components
arr1.addColumn("color", 3, pan.Geom.NTFloat32, pan.Geom.CColor)

# adding a third column for normals
arr1.addColumn("normal", 3, pan.Geom.NTFloat32, pan.Geom.CVector)

# adding our array to the Format
format1.addArray(arr1)

# registering the format, by replacing original format with the return Value of
# registerFormat method
format1 = pan.GeomVertexFormat.registerFormat(format1)

# making a vertex data object, with a data1 as it's name, passing in our own
# format, and using the 3rd paramater to define it as static (means it won't
# change during runtime)
vdata1 = pan.GeomVertexData("data1", format1, pan.Geom.UHStatic)

# just for performance reasons, we specify how many rows we are going to add
vdata1.setNumRows(4)

# creating a geomvertexwriter, an object that takes our inputed data, and adds
# it to our vertex data. There are writers for every type of column in our
# vertexdata object (ie. color, texmap, normals etc.)
# the writer object increases it's row counter every time it is called, so even
# if on some vertices you want to use the default setting on, it should still be
# applied, in order for the following rows to work
vertex = pan.GeomVertexWriter(vdata1, "vertex")

# creating a writer for colors:
color = pan.GeomVertexWriter(vdata1, "color")

# creating a writer for normals
normal = pan.GeomVertexWriter(vdata1, "normal")

# this calls the addData method on our writer (3 components, a float),
# this needs to be called for every vertice in our data. even if we just
# want to use the default value on certain rows, it still needs to be called
# in those rows, in order for the following ones to work.
# first row:
vertex.addData3f(100, 0, 0)
color.addData3f(1, 0, 0)
normal.addData3f(0, 0, 1)

# second row:
vertex.addData3f(100, 100, 0)
color.addData3f(0, 1, 0)
normal.addData3f(0, 0, 1)

# third row:
vertex.addData3f(0, 100, 0)
color.addData3f(0, 0, 1)
normal.addData3f(0, 0, 1)

# creating a Triangle GeomPrimitive. UHStatic is a usage hint, just like in
# vdata1. since we don't plan on changing the vertex indices during runtime,
# we'll leave it as static.
tri1 = pan.GeomTriangles(pan.Geom.UHStatic)

# adding my vertices by index(sorted by order of instantiation) to the triangle.
# alternatively I could also call something like prim.addVertices(0, 1, 2) in
# order to add them all at once. Or add_consecutive_vertices(start, numVertices)
# And finally: add_next_vertices(numVertices), which adds a given number of ver
tri1.addVertex(0)
tri1.addVertex(1)
tri1.addVertex(2)

# now we close our primitve, since it is just a simple tri, we should be done
# for now. This NEEDS to be done every time we have finished inputting all v's.
# ACTUALLY NOT! but I have to figure when to close it...
tri1.closePrimitive()

# creating a geom, and giving it vdata1 as its vertex data. this can be changed
# later by calling geom.setVertexData(). There can only be one vdata per Geom!
basicgeom = pan.Geom(vdata1)

# adding the triangle primitive to our Geom
basicgeom.addPrimitive(tri1)

# Creating a node, which is required in panda in order to add things to our
# scene.
tri_node = pan.GeomNode("mynode")

# attaching our geom to the created node
tri_node.addGeom(basicgeom)

# creates a nodepath object (triangle), attaches it to the root
triangle = render.attachNewNode(tri_node)

# add another normal on the other side of the face, making it visible from both
# sides
triangle.setTwoSided(True)

# adding a light to the scene graph
dlight = pan.DirectionalLight('dlight')
dlight.setColor(pan.VBase4(0.8, 0.8, 0.5, 1))
dlnp = render.attachNewNode(dlight)
dlnp.setHpr(0, -60, 0)
render.setLight(dlnp)
# Use a 512x512 resolution shadow map
dlight.setShadowCaster(True, 512, 512)
# Enable the shader generator for the receiving nodes
render.setShaderAuto()

# runs panda3d.core.showbase.ShowBase, thus opening our scene in a window
base.run()
