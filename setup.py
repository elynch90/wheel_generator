bl_info = {
  "name": "Car Wheel Generator",
  "description": "Generate car wheels with tires",
  "author": "Your Name",
  "version": (1, 0),
  "blender": (3, 2, 0),
  "location": "View3D > Add > Mesh",
  "warning": "",
  "doc_url": "",
  "category": "Add Mesh",
}

import bpy

from .generate_wheel import GenerateCarWheelOperator

classes = (
  GenerateCarWheelOperator,
)

def register():
  for cls in classes:
    bpy.utils.register_class(cls)

def unregister():
  for cls in classes:
    bpy.utils.unregister_class(cls)

if __name__ == "__main__":
  register()
