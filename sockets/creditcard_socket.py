import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


class MyCustomSocketCreditcard(NodeSocket):
    '''Custom node socket type for creating data input points for credit card information.'''
    bl_idname = 'CustomSocketTypeCreditcard'
    bl_label = "Custom Node Socket Credit card information"

    def update_creditcard_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()

    creditcard_pin: bpy.props.BoolProperty(name="Pin", update=update_creditcard_socket)

    creditcard_items = (
        ('AMEX', "Amex", "American Express"),
        ('MAESTRO', "Maestro", "Maestro"),
        ('MASTERCARD', "Mastercard", "Mastercard"),
    )

    creditcard_type: bpy.props.EnumProperty(
        name="Type",
        description="Choose the information required",
        items=creditcard_items,
        default='AMEX',
        update=update_creditcard_socket
    )

    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="Credit Card")
            layout.prop(self, "creditcard_type", text="Type")
            layout.prop(self, "creditcard_pin", text="Pin")

    
    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)
