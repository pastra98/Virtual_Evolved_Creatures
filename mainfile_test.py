from tetrahedrical import tetrahedrical
from geom_creation import Geometry_op
from creatures import Creature
from creatures import Bone
from panda3d import core as cor

from panda3d.core import Geom as geo
from direct.showbase import ShowBase as shb

# init ShowBase class in order to get a scene graph and other stuff
base = shb.ShowBase()

# create a geometry_op object
my_bone = Bone("bonez")
print(my_bone.f_list)
print(my_bone.b_geom)

# creating a nodepath
Node = cor.GeomNode("cube2")

# adding our triangle to the newly created node
Node.addGeom(my_bone.b_geom)

# creating a nodepath for our cube and attaching it to render
NodePath = render.attachNewNode(Node)

base.run()
