import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


class MyCustomNodeLicense(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake license plate numbers from the Faker library.'''
    bl_idname = 'CustomNodeLicense'
    bl_label = "License Plate"
    bl_icon = 'ACTION'


    def update_license_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].license_include = self.license_include
    
    license_include: bpy.props.BoolProperty(name="Include license", update=update_license_node_attribute)


    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypeLicense', "License plate information")
        self.license_include = True
        
    
    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''

        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.license_include = self.outputs[0].license_include 
    
        print("**************** NODE: License Plate *********************")
        print("Input  :: Include license information :: ", self.license_include)
        print("Output :: License Plate Information :: ", self.outputs[0].license_include)
        print("***************************************************")


    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)

    
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

   
    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="License Plate Information")
        layout.prop(self, "license_include")


    def draw_buttons_ext(self, context, layout):
        pass


    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "License Plate"
