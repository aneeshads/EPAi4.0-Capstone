
import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


class MyCustomNodePhone(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake phone numbers from the Faker library.'''
    bl_idname = 'CustomNodePhone'
    bl_label = "Phone"
    bl_icon = 'ACTION'

    def update_phone_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].phone_type = self.phone_type

    phone_items = (
        ('MSISDN', "MSISDN", "Get the MSISDN number"),
        ('PHONE', "Phone Number", "Get the phone number"),
    )


    phone_type: bpy.props.EnumProperty(
        name="Phone Type",
        description="Choose phone type",
        items=phone_items,
        default='PHONE',
        update=update_phone_node_attribute
    )

    
    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypePhone', "Phone Data")


    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.phone_type = self.outputs[0].phone_type

        print("**************** NODE: PHONE *********************")
        print("Output :: Phone Type     :: ", self.outputs[0].phone_type)
        print("***************************************************")
    
    
    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)

    
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

    
    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="Phone Settings")
        layout.prop(self, "phone_type")

    
    def draw_buttons_ext(self, context, layout):
        pass


    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Phone"
