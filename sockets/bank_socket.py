import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


class MyCustomSocketBank(NodeSocket):
    '''Custom node socket type for creating data input points for bank information.'''
    bl_idname = 'CustomSocketTypeBank'
    bl_label = "Bank Information"

    def update_bank_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()

    bank_country: bpy.props.BoolProperty(name="Bank Country", update=update_bank_socket)

    bank_items = (
        ('BBAN', "BBAN", "Basic Bank Account Number"),
        ('IBAN', "IBAN", "International Bank Account Number"),
    )

    bank_type: bpy.props.EnumProperty(
        name="Account Type",
        description="Choose the account information required",
        items=bank_items,
        default='BBAN',
        update=update_bank_socket
    )

    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="Bank")
            layout.prop(self, "bank_country", text="Country")
            layout.prop(self, "bank_type", text="Account Type")


    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)