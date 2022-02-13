import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


class MyCustomNodePerson(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake profiles of people from the Faker library.'''
    bl_idname = 'CustomNodePerson'
    bl_label = "Person"
    bl_icon = 'ACTION'

    def update_person_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].person_prefix = self.person_prefix
        self.outputs[0].person_first_name = self.person_first_name
        self.outputs[0].person_last_name = self.person_last_name

    person_prefix: bpy.props.BoolProperty(name="Prefix", update=update_person_node_attribute)
    person_first_name: bpy.props.BoolProperty(name="First Name", update=update_person_node_attribute)
    person_last_name: bpy.props.BoolProperty(name="Last Name", update=update_person_node_attribute)

    
    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypePerson', "Person")
        self.person_prefix = True
        self.person_first_name = True
        self.person_last_name = False


    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''

        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.person_prefix = self.outputs[0].person_prefix
            self.outputs[0].links[0].to_socket.person_first_name = self.outputs[0].person_first_name
            self.outputs[0].links[0].to_socket.person_last_name = self.outputs[0].person_last_name
    
        print("**************** NODE: PERSON *********************")
        print("Output :: Prefix     :: ", self.outputs[0].person_prefix)
        print("Output :: First Name :: ", self.outputs[0].person_first_name)
        print("Output :: Last Name  :: ", self.outputs[0].person_last_name)
        print("***************************************************")
        
    
    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)


    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")


    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="Person Information")
        layout.prop(self, "person_prefix")
        layout.prop(self, "person_first_name")
        layout.prop(self, "person_last_name")
        

    def draw_buttons_ext(self, context, layout):
        pass


    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Person"
