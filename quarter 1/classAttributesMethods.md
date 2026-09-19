# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
The overall design of my StringInstrument class stayed the same because the original properties and methods still fit the class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| instrument_name | string | Public | It can be accessed to identify the instrument. |
| instrument_type | string | Public | It can be accessed to identify the type of instrument. |
| number_of_strings | int | Public | It can be accessed to know how many strings the instrument has. |
| is_tuned | boolean | Private | Its value should be controlled through methods such as tune() instead of being changed directly. |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png) <img width="959" height="491" alt="image" src="https://github.com/user-attachments/assets/558a40a3-f535-4946-932e-d0d41941f197" />

## Object Diagram
![Object Diagram](images/objectDiagram.png) <img width="383" height="245" alt="image" src="https://github.com/user-attachments/assets/3e3f7adc-5216-437d-8215-38e5bc54c11b" />

## Analysis
### Why did you make your chosen attribute private?
I made is_tuned private because its value represents the tuning state of the instrument. If other parts of the program could change it directly, they could incorrectly mark an instrument as tuned without actually tuning it. Making it private allows the tune()method to control when its value changes.
### Which method changes the state of your object?
The tune() method changes the state of the object by changing the private is_tuned attribute from False to True. For example, Luna's is_tuned value changed after the tune() method was called. This shows that a method can safely modify an object's state.
### How did your two objects demonstrate that instances are independent?
The two objects were guitar and ukulele, and they had different values. When I called tune() on the guitar, its is_tuned value changed from False to True. The ukulele was not affected, showing that each object keeps its own independent state.
### What is the difference between your class diagram and your object diagram?
The class diagram shows the blueprint of the StringInstrument class, including its attributes, data types, and methods. The object diagram shows actual objects created from that class and their current values. In my example, the object diagram would show Luna as an acoustic guitar with 6 strings and Sunny as a ukulele with 4 strings.
