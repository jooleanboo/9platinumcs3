# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: StringInstrument
Description: The StringInstrument class represents a musical instrument that produces sound through strings. In this activity, the StringInstrument objects represent guitars.
## New Related Class
Class: Guitarist
Description: This class represents a person who plays guitars
## Association
Relationship: Guitarist HAS-A collection of StringInstruments.
Explanation: A guitarist can own and play multiple guitars. In this system the guitarist object named Bonaobra is connected to three StringInstrument objects: Julian, Xander, and Joolean.
## Multiplicity

Multiplicity: 1 : 0..*
Explanation: One Guitarist can have zero or more StringInstrument objects. This fits the system because a guitarist can have multiple guitars.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png) <img width="249" height="389" alt="image" src="https://github.com/user-attachments/assets/0cacf537-fbe9-4d6c-9fa9-928e27ebfd1c" />

## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png) <img width="959" height="503" alt="image" src="https://github.com/user-attachments/assets/753faa43-fd79-4841-93ce-83f8cb98daca" />

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png) <img width="217" height="354" alt="image" src="https://github.com/user-attachments/assets/e7e6951c-c357-4d43-932a-bb745d77024c" />

## Analysis
### What is the association between your two classes?
The association between Guitarist and StringInstrument is a HAS-A relationship. A Guitarist can have and manage multiple StringInstrument objects. In my system, Bonaobra has three guitars: Julian, Xander, and Joolean.
### What multiplicity did you choose and why?
I chose a one-to-many relationship with a multiplicity of 1 : 0..*. One Guitarist can have zero or more StringInstrument objects. This fits because a guitarist can have several guitars.
### How did you implement the relationship in Python?
I implemented the relationship using the private `__instruments` list inside the Guitarist class. The `add_instrument()` method adds actual StringInstrument objects to this list. This allows the Guitarist object to access the information of each related guitar.
### Why did you store an object reference instead of copying its data?
I stored the actual StringInstrument objects so that the Guitarist can access their properties and methods. For example, Bonaobra can access Julian's instrument name and number of strings through the object reference. This avoids creating duplicate copies of the guitar's information.
### If your relationship uses many, why is a list appropriate?
A list is appropriate because one Guitarist can be connected to multiple StringInstrument objects. The list contains the actual guitar objects rather than just their names. This allows the program to loop through Bonaobra's guitars and access their information.
