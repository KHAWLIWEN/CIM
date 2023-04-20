import bpy

#create box1
bpy.ops.mesh.primitive_cube_add()
box1=bpy.context.object
box1.name='box1'

#set box dimension
box1.dimensions = (3.0,3.0,3.0)

#create lid1
bpy.ops.mesh.primitive_cube_add()
lid1=bpy.context.object
lid1.name='lid1'

#set lid dimension
lid1.dimensions = (3.5,3.5,0.5)

#set lid location
lid1.location = (0.0,0.0,1.5)

#create box2
bpy.ops.mesh.primitive_cube_add()
box2=bpy.context.object
box2.name='box2'

#set box dimension
box2.dimensions = (5.0,5.0,5.0)

#set box location
box2.location = (8.0,0.0,0.0)

#create lid1
bpy.ops.mesh.primitive_cube_add()
lid2=bpy.context.object
lid2.name='lid2'

#set lid dimension
lid2.dimensions = (5.5,5.5,1.0)

#set lid location
lid2.location = (8.0,0.0,2.5)


#create box3
bpy.ops.mesh.primitive_cube_add()
box3=bpy.context.object
box3.name='box3'

#set box dimension
box3.dimensions = (8.0,8.0,8.0)

#set box location
box3.location = (20.0,0.0,0.0)

#create lid1
bpy.ops.mesh.primitive_cube_add()
lid3=bpy.context.object
lid3.name='lid3'

#set lid dimension
lid3.dimensions = (8.5,8.5,1.5)

#set lid location
lid3.location = (20.0,0.0,4.0)
