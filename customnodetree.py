
import bpy
from bpy_types import NodeTree

class MyCustomTree(NodeTree):
    # Description string
    # '''A custom node tree type that will show up in the editor type list'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerTreeType'
    # Label for nice name display
    bl_label = "Faker Node Tree"
    # Icon identifier
    bl_icon = 'NODETREE'

# Mix-in class for all custom nodes in this tree type.
# Defines a poll function to enable instantiation.
class MyCustomTreeNode:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'FakerTreeType'