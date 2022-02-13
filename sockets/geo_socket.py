import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket


class MyCustomSocketGeo(NodeSocket):
    '''Custom node socket type'''
    bl_idname = 'CustomSocketTypeGeo'
    bl_label = "Custom Node Socket Geographical Location"


    def update_geo_socket(self, context):
        '''This function updates the output of the current node.'''
        self.node.update()
    
    geo_items = (
        ('LATLNG', "Lat and Long", "Get the latitude and longitude"),
        ('LOCALLATLNG', "Location", "Get the location"),
    )

    geo_type: bpy.props.EnumProperty(
        name="Geo Type",
        description="Choose type of output",
        items=geo_items,
        default='LATLNG',
        update=update_geo_socket
    )
    
    
    def draw(self, context, layout, node, text):
        '''This function creates the labels for the socket panels within the node.'''
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.label(text="Geo Location")
            layout.prop(self, "geo_type", text="Geo Location")
            

    def draw_color(self, context, node):
        '''This function determines the colour of the input and output points within the socket.'''
        return (1.0, 0.4, 0.216, 0.5)
