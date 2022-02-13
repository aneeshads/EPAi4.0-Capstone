import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


class MyCustomNodeGeo(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake geographical location information \
    (longitude and latitude) from the Faker library.'''
    bl_idname = 'CustomNodeGeo'
    bl_label = "Geographical location"
    bl_icon = 'ACTION'

    def update_geo_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].geo_type = self.geo_type

    geo_items = (
        ('LATLNG', "Lat and Long", "Get the latitude and longitude"),
        ('LOCALLATLNG', "Location", "Get the location"),
    )

    geo_type: bpy.props.EnumProperty(
        name="Geographical location",
        description="Choose type of output",
        items=geo_items,
        default='LATLNG',
        update=update_geo_node_attribute
    )


    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypeGeo', "Geographical location")


    def update(self):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.geo_type = self.outputs[0].geo_type
            
        print("**************** NODE: GEOGRAPHICAL LOCATION *********************")
        print("Input  :: GEOTYPE :: ", self.geo_type)
        print("Output :: GEOTYPE :: ", self.outputs[0].geo_type)
        print("***************************************************")
            

    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)

    
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

    
    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="Geographical location")
        layout.prop(self, "geo_type")
    

    def draw_buttons_ext(self, context, layout):
        pass


    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Geographical location"
