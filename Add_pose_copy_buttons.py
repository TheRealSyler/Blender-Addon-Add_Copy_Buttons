import bpy

bl_info = {
    "name" : "Add Pose Copy Buttons",
    "author" : "Syler",
    "version": (0, 1),
    "description": "Adds Pose Copy Buttons To Header",
    "blender" : (2, 80, 0),
    "category" : "3D view"
}



def menu_func(self, context):
    if bpy.context.mode == 'POSE':
        row = self.layout.row(align=True)
        row.separator()
        row.operator("pose.copy", text="", icon='COPYDOWN')
        row.operator("pose.paste", text="", icon='PASTEDOWN').flipped = False
        row.operator("pose.paste", text="", icon='PASTEFLIPDOWN').flipped = True
        

classes = [
]


def register():
    for c in classes:
        bpy.utils.register_class(c)

    # ------------------------------------------------------------------------------------------------------------
    # Append Register stuff
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.VIEW3D_MT_editor_menus.append(menu_func)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    # ------------------------------------------------------------------------------------------------------------
    # Append Unregister stuff
    # ------------------------------------------------------------------------------------------------------------

    bpy.types.VIEW3D_MT_editor_menus.remove(menu_func)

    
if __name__ == "__main__":
    register()
