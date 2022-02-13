import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


class MyCustomSocketCompany(NodeSocket):
    '''Custom node socket type for creating data input points for company information.'''
    bl_idname = 'CustomSocketTypeCompany'
    bl_label = "Custom Node Socket Company"


    def update_company_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()

    company_suffix: bpy.props.BoolProperty(name="Suffix", update=update_company_socket)
    company_motto: bpy.props.BoolProperty(name="Motto",  update=update_company_socket)
    
    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="Company")
            layout.prop(self, "company_suffix", text="Suffix")
            layout.prop(self, "company_motto", text="Motto")

   
    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)
