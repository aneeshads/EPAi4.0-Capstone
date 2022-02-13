import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..customnodetree import MyCustomTreeNode
from collections import namedtuple

from faker import Faker
fake = Faker()
Faker.seed(0)


class MyCustomNodeGenerator(Node, MyCustomTreeNode):
    '''A custom node that accepts input information from all the other custom nodes.'''
    bl_idname = 'CustomNodeGenerator'
    bl_label = "Generator"
    bl_icon = 'ACTION'

    def update_generator_node_attribute(self, context):
        '''This function updates the output of the current node'''
        self.update()

    generator_count: bpy.props.IntProperty(name="Count", default=5, update=update_generator_node_attribute)


    def init(self, context):
        ''' '''
        self.inputs.new('CustomSocketTypePerson', "Person Data")
        self.inputs.new('CustomSocketTypePhone', "Phone")
        self.inputs.new('CustomSocketTypeAddress', "Address")
        self.inputs.new('CustomSocketTypeSSN', "SSN")
        self.inputs.new('CustomSocketTypeGeo', "Geo Location")
        self.inputs.new('CustomSocketTypeBank', "Bank")
        self.inputs.new('CustomSocketTypeCompany', "Company")
        self.inputs.new('CustomSocketTypeCreditcard', "Credit Card")
        self.inputs.new('CustomSocketTypeJobs', "Job")
        self.inputs.new('CustomSocketTypeLicense', "License")
        self.inputs[0].person_prefix = True
        self.inputs[0].person_first_name = True
        self.inputs[0].person_last_name = False
        self.inputs[2].address_city = True
        self.inputs[3].ssn_include = True
        self.inputs[5].bank_country = True
        self.inputs[6].company_suffix = True
        self.inputs[6].company_motto = False
        self.inputs[7].creditcard_pin = False
        self.inputs[8].jobs_include = False
        self.inputs[9].license_include = False
        
    
    def socket_value_update(self):
        ''' '''
        print("MyCustomNodeGenerator::socket_value_update:", type(self).__name__)

    
    def _get_named_tuple(self):
        ''' '''
        FakerDataInit = namedtuple('FakerDataInit', ['Sl_no'])
        faker_headers = FakerDataInit._fields
        if self.inputs[0].person_prefix:
            faker_headers += ('prefix', )
        if self.inputs[0].person_first_name:
            faker_headers += ('first_name', )
        if self.inputs[0].person_last_name:
            faker_headers += ('last_name', )
        faker_headers +=('phone', )
        faker_headers +=('address', )
        if self.inputs[2].address_city:
            faker_headers += ('city', )
        if self.inputs[2].address_country:
            faker_headers += ('country', )
        if self.inputs[3].ssn_include:
            faker_headers += ('ssn_no', )
        faker_headers +=('geo_location', )
        faker_headers +=('bank_acc', )
        if self.inputs[5].bank_country:
            faker_headers+=('bank_country', )
        faker_headers+=('company', )
        if self.inputs[6].company_suffix:
            faker_headers+=('company_suffix', )
        if self.inputs[6].company_motto:
            faker_headers+=('company_motto', )
        faker_headers+=('credit_card', )
        if self.inputs[7].creditcard_pin:
            faker_headers+=('creditcard_pin', )
        if self.inputs[8].jobs_include:
            faker_headers+=('job', )
        if self.inputs[9].license_include:
            faker_headers+=('license_plate', )

        FakerData =  namedtuple('FakerData', faker_headers)

        return FakerData

    
    def _generate_fake_data_row(self, row_number):
        ''' '''
        
        rows_data = []
        rows_data.append(row_number)

        # Get the required fake values in name
        if self.inputs[0].person_prefix:
            rows_data.append(fake.prefix()) 
        
        if self.inputs[0].person_first_name:
            rows_data.append(fake.first_name()) 
        
        if self.inputs[0].person_last_name:
            rows_data.append(fake.last_name())

        # Get fake phone number based on type
        if self.inputs[1].phone_type == 'MSISDN':
            rows_data.append(fake.msisdn()) 
        elif self.inputs[1].phone_type == 'PHONE':
            rows_data.append(fake.phone_number()) 
        
        # Get fake address based on type
        rows_data.append(fake.address()) 
        if self.inputs[2].address_city:
            rows_data.append(fake.city())
        
        if self.inputs[2].address_country:
            rows_data.append(fake.country())
        
        # Get fake SSN data based on choice of user 
        if self.inputs[3].ssn_include:
            rows_data.append(fake.ssn())

        # Get fake Geo data based on choice of user 
        if self.inputs[4].geo_type == 'LATLNG':
            rows_data.append(fake.latlng())
        elif self.inputs[4].geo_type == 'LOCALLATLNG':
            rows_data.append(fake.local_latlng())

        # Get fake Bank data based on choice of user 
        if self.inputs[5].bank_type == 'IBAN':
            rows_data.append(fake.iban())
        elif self.inputs[5].bank_type == 'BBAN':
            rows_data.append(fake.bban())
        
        if self.inputs[5].bank_country:
            rows_data.append(fake.bank_country())

         # Get fake company data
        rows_data.append(fake.company())
        
        if self.inputs[6].company_suffix:
            rows_data.append(fake.company_suffix())
        
        if self.inputs[6].company_motto:
            rows_data.append(fake.catch_phrase())

        # Get fake credit card data
        if self.inputs[7].creditcard_type == 'AMEX':
            rows_data.append(fake.credit_card_number(card_type='amex'))
        elif self.inputs[7].creditcard_type == 'MAESTRO':
            rows_data.append(fake.credit_card_number(card_type='maestro'))
        elif self.inputs[7].creditcard_type == 'MASTERCARD':
            rows_data.append(fake.credit_card_number(card_type='mastercard'))
        else:
            rows_data.append(fake.credit_card_number())

        if self.inputs[7].creditcard_pin:
            rows_data.append(fake.credit_card_security_code())

        # Get fake job data
        if self.inputs[8].jobs_include:
            rows_data.append(fake.job())

        # Get fake license plate data
        if self.inputs[9].license_include:
            rows_data.append(fake.license_plate())

        return rows_data

    
    def update(self):
        '''This function connects the output of the current node to the input socket of the \
        next node.'''

        print("**************** NODE: GENERATOR *********************")
        print("Input :: Count                   :: ", self.generator_count)
        print("Input :: Prefix                  :: ", self.inputs[0].person_prefix)
        print("Input :: First Name              :: ", self.inputs[0].person_first_name)
        print("Input :: Last Name               :: ", self.inputs[0].person_last_name)
        print("Input :: Phone Type              :: ", self.inputs[1].phone_type)
        print("Input :: City name               :: ", self.inputs[2].address_city)
        print("Input :: Country name            :: ", self.inputs[2].address_country)
        print("Input :: Social Security Number  :: ", self.inputs[3].ssn_include)
        print("Input :: Geographical location   :: ", self.inputs[4].geo_type)
        print("Input :: Bank Country            :: ", self.inputs[5].bank_country)
        print("Input :: Bank Account Type       :: ", self.inputs[5].bank_type)
        print("Input :: Company Suffix          :: ", self.inputs[6].company_suffix)
        print("Input :: Company Motto           :: ", self.inputs[6].company_motto)
        print("Input :: Credit Card Type        :: ", self.inputs[7].creditcard_type)
        print("Input :: Credit Card Pin         :: ", self.inputs[7].creditcard_pin)
        print("Input :: Job                     :: ", self.inputs[8].jobs_include)
        print("Input :: License                 :: ", self.inputs[9].license_include)
        print("***************************************************")
    
        FakerData = self._get_named_tuple()
        generated_faker_data = []
        for i in range(self.generator_count):
            rows_list = []
            rows_list = self._generate_fake_data_row(i+1)
            tuplerow = FakerData(*rows_list)
            generated_faker_data.append(tuplerow)
        
        print("******************* Generated Faker Data **********************")
        for row in generated_faker_data:
            print(row)
            print("---------------------------------------------------------------")
        print("******************* Generated Faker Data **********************")


    def copy(self, node):
        '''This function facilitates the copying of a node.'''
        print("Copying from node ", node)

        
    def free(self):
        '''This function facilitates the removal of a node.'''
        print("Removing node ", self, ", Goodbye!")

    
    def draw_buttons(self, context, layout):
        layout.label(text="Generator Settings")
        layout.prop(self, "generator_count")
        layout.label(text="Input Sockets")

    
    def draw_buttons_ext(self, context, layout):
        '''This function creates the labels for the display panels within the node.'''
        pass

   
    def draw_label(self):
        '''This function determines the name of the node which appears at its head.'''
        return "Generator"
