from direct.showbase.ShowBase import ShowBase
import panda3d.core as pan

# creating an array for a GeomVertexArray Format:
arr1 = pan.GeomVertexArrayFormat()

#creating a Format to later add my arrays to:
format1 = pan.GeomVertexFormat()

# adding column to our array, specifying that the first column in arr1 is going
# to be for vertices
arr1.addColumn("vertex", 3, pan.Geom.NTFloat32, pan.Geom.CPoint)

# adding our array to the Format
format1.addArray(arr1)

# registering the format, by replacing original format with the return Value of
# registerFormat method
format1 = pan.GeomVertexFormat.registerFormat(format1)

# making a vertex data object, with a data1 as it's name, passing in our own
# format, and using the 3rd paramater to define it as static (means it won't
# change during runtime)
vdata1 = pan.GeomVertexData('data1', format1, pan.Geom.UHStatic)

# just for performance reasons, we specify how many rows we are going to add
vdata1.setNumRows(4)

# creating a geomvertexwriter, an object that takes our inputed data, and adds
# it to our vertex data. There are writers for every type of column in our
# vertexdata object (ie. color, texmap, normals etc.)
vertex = pan.GeomVertexWriter(vdata1, 'vertex')

# THIS IS GONNA NEED SOME COMMENTING, YOU BETTER COMMENT THIS SHIT, YOU LITTLE
# BITCH
vertex.addData3f(1, 0, 0)
vertex.addData3f(1, 1, 0)
vertex.addData3f(0, 1, 0)
vertex.addData3f(0, 0, 0)
