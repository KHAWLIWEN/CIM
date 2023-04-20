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


#join 
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.join()
