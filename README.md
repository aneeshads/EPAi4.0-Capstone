# Capstone assignment of EPAi4.0
### Submitted by Aneesha Das
### E-mail id: dasaneesha@gmail.com

## Introduction
Blender version 3.0.0
Blender is a software that is extensively used for the visualization of 2D and 3D shapes. 
Blender elements used are as follows:

### Nodes
In the current project, each individual nodes represent a data point, whose output is forwarded to a final supra node that conditionally displays the incoming data fields. This implies that the user can choose whether the information being output from a node can be displayed or not.
### Sockets
The entry of data as well as its forwarding to the next node happens via points housed within panels inside each node. These panels are known as sockets.
### Links
The connection between individual nodes and the entry points within the sockets happens via links, which are also known as edges.

## Description of the project

The Python API of Blender and its various other elements described above have been used to create a directional data flow model. The directional data flow model channels the inputs from a source node to a recipient node which has the appropriate socket point to receive the data from the former. In order to ensure that any change of input in the source node is reflected in the recipient as well, appropriate backend codes have been deployed. 

The following Faker providers have been used in the current project:</br>
1. address </br>
2. bank </br>
3. company </br>
4. credit card </br>
5. geo </br>
6. job </br>
7. license plate </br>
8. person </br>
9. phone </br>
10. social security number </br>

## Requirements:

### Installation of Faker library: 
This can be done using the following commands:
```python
from pip._internal import main
main(['install', 'faker'])
```
### Usage






