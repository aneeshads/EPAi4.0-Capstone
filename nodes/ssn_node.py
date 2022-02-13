import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


class MyCustomNodeSSN(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake social security numbers (SSN) \
    from the Faker library.'''
    bl_idname = 'CustomNodeSSN'
    bl_label = "Social Security Number"
    bl_icon = 'ACTION'


    def update_ssn_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].ssn_include = self.ssn_include
   
    ssn_include: bpy.props.BoolProperty(name="Include SSN", update=update_ssn_node_attribute)


    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypeSSN', "SSN")
        self.ssn_include = True
        

    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.ssn_include = self.outputs[0].ssn_include  
    
        print("**************** NODE: SSN *********************")
        print("Input  :: Include SSN :: ", self.ssn_include)
        print("Output :: Social Security Number :: ", self.outputs[0].ssn_include)
        print("***************************************************")


    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)

    
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="Social Security Number")
        layout.prop(self, "ssn_include")


    def draw_buttons_ext(self, context, layout):
        pass


    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Social Security Number"
