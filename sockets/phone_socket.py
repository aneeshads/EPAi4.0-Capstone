import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket
from datetime import datetime


# Custom socket type
class MyCustomSocketPhone(NodeSocket):
    '''Custom node socket type for creating data input points for phone number information.'''
    bl_idname = 'CustomSocketTypePhone'
    bl_label = "Custom Node Socket Phone"

    def update_phone_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()


    phone_items = (
        ('MSISDN', "MSISDN", "Get the MSISDN number"),
        ('PHONE', "Phone Number", "Get the phone number"),
    )

    phone_type: bpy.props.EnumProperty(
        name="Phone Type",
        description="Choose phone type",
        items=phone_items,
        default='PHONE',
        update=update_phone_socket
    )

   
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="Phone")
            layout.prop(self, "phone_type", text=text)

    
    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)