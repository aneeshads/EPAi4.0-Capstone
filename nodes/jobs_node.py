import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


# Derived from the Node base type.
class MyCustomNodeJobs(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake occupation details from the Faker library.'''
    bl_idname = 'CustomNodeJobs'
    bl_label = "Occupation"
    bl_icon = 'ACTION'


    def update_jobs_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].jobs_include = self.jobs_include
    
    jobs_include: bpy.props.BoolProperty(name="Include occupation", update=update_jobs_node_attribute)

    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypeJobs', "Jobs")
        self.jobs_include = True
        

    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.jobs_include = self.outputs[0].jobs_include  
    
        print("**************** NODE: OCCUPATION INFORMATION *********************")
        print("Input  :: Occupation :: ", self.jobs_include)
        print("Output :: Occupation :: ", self.outputs[0].jobs_include)
        print("***************************************************")


    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)

    
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

    
    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="Occupation information")
        layout.prop(self, "jobs_include")


    def draw_buttons_ext(self, context, layout):
        pass


    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Occupation"
