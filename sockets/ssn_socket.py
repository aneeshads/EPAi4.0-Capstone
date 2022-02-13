import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


class MyCustomSocketSSN(NodeSocket):
    '''Custom node socket type for creating data input points for social security number information.'''
    bl_idname = 'CustomSocketTypeSSN'
    bl_label = "Custom Node Socket Social Security Number"


    def update_ssn_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()

    ssn_include: bpy.props.BoolProperty(name="Social Security Number", update=update_ssn_socket)

    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="SSN")
            layout.prop(self, "ssn_include", text="Social Security Number")


    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)