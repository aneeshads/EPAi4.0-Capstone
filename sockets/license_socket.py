import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


class MyCustomSocketLicense(NodeSocket):
    '''Custom node socket type for creating data input points for license plate information.'''
    bl_idname = 'CustomSocketTypeLicense'
    bl_label = "Custom Node License Plate Information"


    def update_license_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()

    license_include: bpy.props.BoolProperty(name="Include license", update=update_license_socket)

    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="License")
            layout.prop(self, "license_include", text="License Plate Information")


    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)