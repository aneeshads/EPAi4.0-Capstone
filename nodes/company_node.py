import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


class MyCustomNodeCompany(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake company information from the Faker library.'''
    bl_idname = 'CustomNodeCompany'
    bl_label = "Company"
    bl_icon = 'ACTION'
    
    
    def update_company_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].company_suffix = self.company_suffix
        self.outputs[0].company_motto = self.company_motto
    
    company_suffix: bpy.props.BoolProperty(name="Suffix", update=update_company_node_attribute)
    company_motto: bpy.props.BoolProperty(name="Motto",  update=update_company_node_attribute)


    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypeCompany', "Company Data")
        self.company_suffix = True
        self.company_motto = True
        

    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.company_suffix = self.outputs[0].company_suffix
            self.outputs[0].links[0].to_socket.company_motto = self.outputs[0].company_motto
    
        print("**************** NODE: COMPANY *********************")
        print("Input  :: Suffix :: ", self.company_suffix)
        print("Input  :: Motto :: ", self.company_motto)
        print("Output :: Suffix  :: ", self.outputs[0].company_suffix)
        print("Output :: Motto :: ", self.outputs[0].company_motto)
        print("***************************************************")


    def copy(self, node):
        '''This function facilitates the copying of a node.  '''
        print("Copying from node ", node)

   
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

    
    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="Company Information")
        layout.prop(self, "company_suffix")
        layout.prop(self, "company_motto")


    def draw_buttons_ext(self, context, layout):
        pass

    
    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Company"
