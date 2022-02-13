import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


class MyCustomSocketAddress(NodeSocket):
    '''Custom node socket type for creating data input points for address information.'''
    bl_idname = 'CustomSocketTypeAddress'
    bl_label = "Custom Node Socket Address"


    def update_address_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()

    address_city: bpy.props.BoolProperty(name="City", update=update_address_socket)
    address_country: bpy.props.BoolProperty(name="Country",  update=update_address_socket)
    
    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="Address")
            layout.prop(self, "address_city", text="City")
            layout.prop(self, "address_country", text="Country")

    
    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)
