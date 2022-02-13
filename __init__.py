# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy, nodeitems_utils
from bpy.types import Operator, AddonPreferences
from nodeitems_utils import NodeCategory, NodeItem
from .customnodetree import MyCustomTree
# Import custom nodes
from .nodes.generator_node import MyCustomNodeGenerator
from .nodes.person_node import MyCustomNodePerson
from .nodes.phone_node import MyCustomNodePhone
from .nodes.address_node import MyCustomNodeAddress
from .nodes.ssn_node import MyCustomNodeSSN
from .nodes.geo_node import MyCustomNodeGeo
from .nodes.license_node import MyCustomNodeLicense
from .nodes.creditcard_node import MyCustomNodeCreditcard
from .nodes.jobs_node import MyCustomNodeJobs
from .nodes.bank_node import MyCustomNodeBank
from .nodes.company_node import MyCustomNodeCompany
# Import custom sockets
from .sockets.phone_socket import MyCustomSocketPhone
from .sockets.person_socket import MyCustomSocketPerson
from .sockets.address_socket import MyCustomSocketAddress
from .sockets.ssn_socket import MyCustomSocketSSN
from .sockets.geo_socket import MyCustomSocketGeo
from .sockets.license_socket import MyCustomSocketLicense
from .sockets.creditcard_socket import MyCustomSocketCreditcard
from .sockets.jobs_socket import MyCustomSocketJobs
from .sockets.bank_socket import MyCustomSocketBank
from .sockets.company_socket import MyCustomSocketCompany

bl_info = {
    "name": "MyFaker",
    "author": "Aneesha Das",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "Faker Node Tree",
    "description": "Faker Node Editor",
    "category": "MyFaker"    
}

classes = []

class Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout


classes += [MyCustomTree]
classes += [MyCustomNodeGenerator, MyCustomNodePerson, MyCustomNodePhone, MyCustomNodeAddress, MyCustomNodeSSN, MyCustomNodeGeo, MyCustomNodeLicense, MyCustomNodeCreditcard, MyCustomNodeJobs, MyCustomNodeBank, MyCustomNodeCompany]
classes += [MyCustomSocketPhone, MyCustomSocketPerson, MyCustomSocketAddress, MyCustomSocketSSN, MyCustomSocketGeo, MyCustomSocketLicense, MyCustomSocketCreditcard, MyCustomSocketJobs, MyCustomSocketBank, MyCustomSocketCompany]
classes += [Preferences]

class MyNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'FakerTreeType'

# all categories in a list
node_categories = [
    # identifier, label, items list
    MyNodeCategory('PROVIDER_NODES', "Providers", items=[
        NodeItem("CustomNodePerson"),
        NodeItem("CustomNodePhone"),
        NodeItem("CustomNodeAddress"),
        NodeItem("CustomNodeSSN"),
        NodeItem("CustomNodeGeo"),
        NodeItem("CustomNodeLicense"),
        NodeItem("CustomNodeCreditcard"),
        NodeItem("CustomNodeJobs"),
        NodeItem("CustomNodeBank"),
        NodeItem("CustomNodeCompany"),
    ]),
	MyNodeCategory('GENERATOR_NODES', "Generators", items=[
        NodeItem("CustomNodeGenerator"),
    ]),
]

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('FAKER_NODES', node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories('FAKER_NODES')
	
    from bpy.utils import unregister_class
    for cls in reversed(classes):
	    unregister_class(cls)