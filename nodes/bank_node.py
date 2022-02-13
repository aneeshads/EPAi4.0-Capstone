import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


class MyCustomNodeBank(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake bank information from the Faker library.'''
    bl_idname = 'CustomNodeBank'
    bl_label = "Bank"
    bl_icon = 'ACTION'


    def update_bank_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].bank_country = self.bank_country
        self.outputs[0].bank_type = self.bank_type

    bank_country: bpy.props.BoolProperty(name="Bank Country", update=update_bank_node_attribute)

    bank_items = (
        ('BBAN', "BBAN", "Basic Bank Account Number"),
        ('IBAN', "IBAN", "International Bank Account Number"),
    )

    bank_type: bpy.props.EnumProperty(
        name="Account Type",
        description="Choose the account information required",
        items=bank_items,
        default='BBAN',
        update=update_bank_node_attribute
    )


    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.  '''
        self.outputs.new('CustomSocketTypeBank', "Bank Details")
        self.bank_country = True
        

    def update(self):
        '''This function ensures that the required output is generated from the given \
        input data.'''
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.bank_country = self.outputs[0].bank_country
            self.outputs[0].links[0].to_socket.bank_type = self.outputs[0].bank_type
    
        print("**************** NODE: BANK DETAILS *********************")
        print("Input  :: Bank Country :: ", self.bank_country)
        print("Input  :: Account Type :: ", self.bank_type)
        print("Output :: Bank Country :: ", self.outputs[0].bank_country)
        print("Output :: Account Type :: ", self.outputs[0].bank_type)
        print("***************************************************")


    def copy(self, node):
        '''This function facilitates the copying of a node. '''
        print("Copying from node ", node)

  
    def free(self):
        '''This function facilitates the copying of a node.'''
        print("Removing node ", self, ", Goodbye!")


    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node. '''
        layout.label(text="Bank Information")
        layout.prop(self, "bank_country")
        layout.prop(self, "bank_type")


    def draw_buttons_ext(self, context, layout):
        pass


    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Bank"
