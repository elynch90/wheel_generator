# wheel_generator
- A car wheel generator plugin for blender

This code defines a new operator called GenerateCarWheelOperator, which generates a car wheel with a tire when it is executed. The operator has several customizable parameters, such as the number of wheel splits, the wheel diameter, the tire profile, the tire width, and the tire profile bevel amount. It also has a flag to enable customizable tread.

To use this operator in Blender, you can register it using the register function, and then call it using the bpy.ops.mesh.generate_car_wheel operator. You can also unregister it using the unregister function.

To generate the car wheel and tire, you can implement the wheel generation code in the execute method of the operator. This could involve creating a new mesh object, adding vertices, edges, and faces to the mesh, and setting the custom parameters as desired.


To use the car wheel generation operator as a plugin addon in Blender, you can create a new folder for your addon, and then add the Python script containing the operator definition to the folder. You can then create a __init__.py file in the folder to register the operator when the addon is enabled.
