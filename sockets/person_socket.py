import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


# Custom socket type
class MyCustomSocketPerson(NodeSocket):
    '''Custom node socket type for creating data input points for person profile information.'''
    bl_idname = 'CustomSocketTypePerson'
    bl_label = "Custom Node Socket Person"

    def update_person_socket(self, context):
        self.node.update()

    person_prefix: bpy.props.BoolProperty(name="Prefix", update=update_person_socket)
    person_first_name: bpy.props.BoolProperty(name="FirstName",  update=update_person_socket)
    person_last_name: bpy.props.BoolProperty(name="LastName",  update=update_person_socket)    
    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="Person")
            layout.prop(self, "person_prefix", text="Prefix")
            layout.prop(self, "person_first_name", text="First Name")
            layout.prop(self, "person_last_name", text="Last Name")

   
    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)
