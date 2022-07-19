import bpy

CONTENTS = bpy.data.collections.new("CONTENTS")

# Add collection to scene collection
bpy.context.scene.collection.children.link(CONTENTS)

bpy.ops.mesh.primitive_uv_sphere_add(
    radius=1,
    location=(0, 0, 0),
    scale=(1, 1, 1)
)
obj = bpy.context.active_object 
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all() 
# add it to our specific collection
bpy.data.collections['CONTENTS'].objects.link(obj)

bpy.ops.mesh.primitive_cube_add(
    size=1,
    location=(0, 0, 0),
    scale=(1, 1, 1)
)
obj = bpy.context.active_object 
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all() 
# add it to our specific collection
bpy.data.collections['CONTENTS'].objects.link(obj)

bpy.ops.mesh.primitive_cylinder_add(
    radius=1,
    depth=1,
    location=(0, 0, 0),
    scale=(1, 1, 1)
)
obj = bpy.context.active_object 
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all() 
# add it to our specific collection
bpy.data.collections['CONTENTS'].objects.link(obj)

bpy.ops.mesh.primitive_cone_add(
    radius1=1,
    depth=1,
    location=(0, 0, 0),
    scale=(1, 1, 1)
)
obj = bpy.context.active_object 
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all() 
# add it to our specific collection
bpy.data.collections['CONTENTS'].objects.link(obj)

DISTRIBUTOR = bpy.data.collections.new("DISTRIBUTOR")

bpy.context.scene.collection.children.link(DISTRIBUTOR)

bpy.ops.mesh.primitive_monkey_add()
obj = bpy.context.active_object 
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all() 
# add it to our specific collection
bpy.data.collections['DISTRIBUTOR'].objects.link(obj)

# Add the GeometryNodes Modifier
modifier = obj.modifiers.new("GeometryNodes", "NODES")

obj = bpy.data.objects['Suzanne']
node_group = obj.modifiers['GeometryNodes'].node_group
nodes = node_group.nodes

geom_in = nodes.get('Group Input')
geom_in.location = -600, 0

geom_out = nodes.get('Group Output')

position = nodes.new('GeometryNodeSetPosition')
position.location = -200, 0

random = nodes.new('FunctionNodeRandomValue')
random.location = -400, -200

min = nodes.new('FunctionNodeRandomValue')
min.location = -600, -100

max = nodes.new('FunctionNodeRandomValue')
max.location = -600, -300

instance_o_p = nodes.new('GeometryNodeInstanceOnPoints')
instance_o_p.location = 0, 0

separate = nodes.new('GeometryNodeSeparateComponents')
separate.location = -200, -300

col_info = nodes.new('GeometryNodeCollectionInfo')
col_info.location = -400, -400


node_group.links.new(geom_in.outputs['Geometry'], position.inputs['Geometry'])
node_group.links.new(position.outputs['Geometry'], instance_o_p.inputs['Points'])
node_group.links.new(separate.outputs['Instances'], instance_o_p.inputs['Instance'])
node_group.links.new(col_info.outputs['Geometry'], separate.inputs['Geometry'])
node_group.links.new(instance_o_p.outputs['Instances'], geom_out.inputs['Geometry'])
node_group.links.new(random.outputs['Value'], position.inputs['Position'])
node_group.links.new(max.outputs['Value'], random.inputs['Max'])
node_group.links.new(min.outputs['Value'], random.inputs['Min'])