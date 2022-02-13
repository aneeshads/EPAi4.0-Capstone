import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


class MyCustomSocketJobs(NodeSocket):
    '''Custom node socket type for creating data input points for job information.'''
    bl_idname = 'CustomSocketTypeJobs'
    bl_label = "Custom Node Socket Jobs"


    def update_jobs_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()

    jobs_include: bpy.props.BoolProperty(name="Include occupation", update=update_jobs_socket)

    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="Job")
            layout.prop(self, "jobs_include", text="Occupation Information")


    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)