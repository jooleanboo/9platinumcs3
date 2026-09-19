# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
## Inheritance Relationship
Parent: StringInstrument
Child: Guitar
Explanation: A Guitar is a type of StringInstrument because it produces sound through strings. The Guitar class inherits the common attributes and methods of StringInstrument and adds the guitar-specific attribute guitar_style.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation
Explanation: The Guitarist class aggregates Guitar objects because a guitarist can have multiple guitars, but the guitars can still exist independently from the guitarist. In this system, Bonaobra has the guitars Julian, Xander, and Joolean.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png) <img width="209" height="347" alt="image" src="https://github.com/user-attachments/assets/5126df0c-56f4-4e4e-b99e-5d52ae604e8a" />

## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png) <img width="959" height="499" alt="image" src="https://github.com/user-attachments/assets/57850933-fa2e-49b6-bff9-eb2997befc37" />

## Object Diagram
![Objects](images/advancedObjectDiagram.png) <img width="308" height="286" alt="image" src="https://github.com/user-attachments/assets/31200da3-044e-44ed-a073-b9eef8518070" />


## Reflection
#### 1. Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.
I chose Guitar as the child class of StringInstrument because a guitar is a type of string instrument. The Guitar class can use the common properties and methods of StringInstrument. It can also have its own guitar-specific property, such as guitar_style.
#### 2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Inheritance allowed the Guitar class to reuse the attributes and methods already written in StringInstrument. For example, instrument_name, instrument_type, number_of_strings, tune(), and display_info() do not need to be written again in the Guitar class. This makes the code shorter and avoids repeating the same code.
#### 3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.
The relationship between Guitarist and Guitar is aggregation because the guitars can exist independently from the guitarist. Julian, Xander, and Joolean are created before they are added to Bonaobra's guitar collection. Therefore, removing Bonaobra would not mean that the guitar objects have to be removed.
#### 4. What is the difference between Association from Part III and the advanced relationship you
implemented?
The association in Part III connected Guitarist and StringInstrument because the guitarist had a collection of instruments. In this activity, the relationship between Guitarist and Guitar is specifically modeled as aggregation because the guitars can exist independently. The system also now uses inheritance because Guitar is a type of StringInstrument.
#### 5. How does your design follow the DRY principle?
The design follows the DRY principle by placing common string instrument features in the StringInstrument parent class. The Guitar class inherits these features instead of rewriting them. This reduces repeated code and makes the system easier to maintain.
