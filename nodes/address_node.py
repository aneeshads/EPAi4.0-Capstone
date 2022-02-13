import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


class MyCustomNodeAddress(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake addresses from the Faker library.'''
    bl_idname = 'CustomNodeAddress'
    bl_label = "Address"
    bl_icon = 'ACTION'

    def update_address_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].address_city = self.address_city
        self.outputs[0].address_country = self.address_country
    
    address_city: bpy.props.BoolProperty(name="City", update=update_address_node_attribute)
    address_country: bpy.props.BoolProperty(name="Country",  update=update_address_node_attribute)


    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypeAddress', "Address")
        self.address_city = True
        self.address_country = True
        

    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.address_city = self.outputs[0].address_city
            self.outputs[0].links[0].to_socket.address_country = self.outputs[0].address_country
    
        print("**************** NODE: ADDRESS *********************")
        print("Input  :: City    :: ", self.address_city)
        print("Input  :: Country :: ", self.address_country)
        print("Output :: City    :: ", self.outputs[0].address_city)
        print("Output :: Country :: ", self.outputs[0].address_country)
        print("***************************************************")


    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)

    
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

    
    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="Address")
        layout.prop(self, "address_city")
        layout.prop(self, "address_country")


    def draw_buttons_ext(self, context, layout):
        pass

    
    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Address"


