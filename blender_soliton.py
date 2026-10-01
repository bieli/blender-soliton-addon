bl_info = {
    "name": "Soliton Wave Generator",
    "author": "Marcin Bielak <marcin.bieli+github+blender+soliton+addon@gmail.com",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Soliton",
    "description": "Generates and animates a mathematical soliton wave on a mesh grid.",
    "category": "Add Mesh",
}

import bpy
import math


def calculate_soliton_z(x, t, A, v, w):
    try:
        val = w * (x - (v * t))
        cosh_val = math.cosh(val)
        return A / (cosh_val * cosh_val)
    except OverflowError:
        return 0.0

# --- ANIMATION LOGIC (HANDLER) ---
def soliton_frame_handler(scene):
    # Look for the object named "Soliton_Grid"
    obj = scene.objects.get("Soliton_Grid")
    if not obj or obj.type != 'MESH':
        return
        
    A = scene.soliton_amplitude
    v = scene.soliton_velocity
    w = scene.soliton_width
    
    # Convert frames to time (slowed down for a better visual effect)
    t = scene.frame_current * 0.1 
    
    mesh = obj.data
    # Iterate through vertices and modify the Z axis
    for vtx in mesh.vertices:
        x = vtx.co.x
        vtx.co.z = calculate_soliton_z(x, t, A, v, w)

# --- PROPERTIES ---
def init_properties():
    bpy.types.Scene.soliton_amplitude = bpy.props.FloatProperty(
        name="Amplitude", default=2.0, min=0.1, max=10.0)
    bpy.types.Scene.soliton_velocity = bpy.props.FloatProperty(
        name="Velocity", default=1.0, min=-10.0, max=10.0)
    bpy.types.Scene.soliton_width = bpy.props.FloatProperty(
        name="Width", default=1.5, min=0.1, max=5.0)

def clear_properties():
    del bpy.types.Scene.soliton_amplitude
    del bpy.types.Scene.soliton_velocity
    del bpy.types.Scene.soliton_width

# --- MESH CREATION OPERATOR ---
class MESH_OT_add_soliton(bpy.types.Operator):
    """Adds a grid prepared for the soliton wave"""
    bl_idname = "mesh.add_soliton"
    bl_label = "Add Soliton Grid"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Create a dense grid
        bpy.ops.mesh.primitive_grid_add(x_subdivisions=200, y_subdivisions=20, size=20)
        obj = context.active_object
        obj.name = "Soliton_Grid"
        
        # Apply smooth shading
        bpy.ops.object.shade_smooth()
        return {'FINISHED'}

# --- USER INTERFACE (UI PANEL) ---
class VIEW3D_PT_soliton(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Soliton"
    bl_label = "Soliton Generator"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.operator("mesh.add_soliton", icon='MESH_GRID')
        layout.separator()
        
        box = layout.box()
        box.label(text="Wave Parameters:")
        box.prop(scene, "soliton_amplitude")
        box.prop(scene, "soliton_velocity")
        box.prop(scene, "soliton_width")

# --- ADD-ON REGISTRATION ---
classes = (
    MESH_OT_add_soliton,
    VIEW3D_PT_soliton,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    init_properties()
    # Add a handler that triggers before frame change
    bpy.app.handlers.frame_change_pre.append(soliton_frame_handler)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    clear_properties()
    if soliton_frame_handler in bpy.app.handlers.frame_change_pre:
        bpy.app.handlers.frame_change_pre.remove(soliton_frame_handler)

if __name__ == "__main__":
    register()
