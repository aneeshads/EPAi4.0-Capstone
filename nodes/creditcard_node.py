import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode


# Derived from the Node base type.
class MyCustomNodeCreditcard(Node, MyCustomTreeNode):
    '''A custom node that accepts input of fake credit card information from the Faker library.'''
    bl_idname = 'CustomNodeCreditcard'
    bl_label = "Credit Card"
    bl_icon = 'ACTION'

    def update_creditcard_node_attribute(self, context):
        '''This function updates the output of the current node.'''
        self.outputs[0].creditcard_type = self.creditcard_type
        self.outputs[0].creditcard_pin = self.creditcard_pin

    creditcard_pin: bpy.props.BoolProperty(name="Pin", update=update_creditcard_node_attribute)

    creditcard_items = (
        ('AMEX', "Amex", "American Express"),
        ('MAESTRO', "Maestro", "Maestro"),
        ('MASTERCARD', "Mastercard", "Mastercard"),
    )

    creditcard_type: bpy.props.EnumProperty(
        name="Type",
        description="Choose the information required",
        items=creditcard_items,
        default='MASTERCARD',
        update=update_creditcard_node_attribute
    )

    
    def init(self, context):
        '''This function creates the sockets that will house the input and the output \
        nodes.'''
        self.outputs.new('CustomSocketTypeCreditcard', "Credit Card Data")
        self.creditcard_pin = True


    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.creditcard_type = self.outputs[0].creditcard_type
            self.outputs[0].links[0].to_socket.creditcard_pin = self.outputs[0].creditcard_pin

        print("**************** NODE: CREDIT CARD INFORMATION *********************")
        print("Input  :: Credit card information  :: ", self.creditcard_type)
        print("Input  :: Credit card PIN :: ", self.creditcard_pin)
        print("Output :: Credit card information  :: ", self.outputs[0].creditcard_type)
        print("Output :: Credit card PIN :: ", self.outputs[0].creditcard_pin)
        print("***************************************************")
    
    
    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)

   
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

    
    def draw_buttons(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        layout.label(text="Credit Card Information")
        layout.prop(self, "creditcard_pin")
        layout.prop(self, "creditcard_type")

    
    def draw_buttons_ext(self, context, layout):
        pass

    
    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Credit Card"
