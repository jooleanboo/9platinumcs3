# SG4 - Understanding Classes and Objects
## Class Name
StringInstrument
## Class Description
It represents a musical instrument that produces sound through strings. It stores information about the instrument and allows actions such as tuning and playing strings.
## Properties
| Property | Data Type | Description |
|---|---|---|
| instrument_name | string | Name of the instrument |
| instrument_type | string | Type of instrument |
| number_of_strings | int | Number of strings on the instrument |
| is_tuned | boolean | Indicated whether the instrument is properly tuned |
## Methods
| Method | Description |
|---|---|
| tune() | Tunes the strings of the instrument |
| play_string(string_number: int) | Plays a specific string using its number |
| display_info() | Displays the instrument's information |
## Class Diagram
![Class Diagram](images/classDiagram.png)
## Design Explanation
### Why did you choose this class?
I chose the StringInstrument class because string instruments are commonly used in music and have different features depending on the instrument. I wanted to create a class that can represent different string instruments because I can play these instruments.
### Which property is the most important? Why?
The is_tuned property is the most important because it shows whether the instrument is ready to produce the correct notes. It helps the user know if the instrument needs to be tuned before playing.
### Which method is the most useful? Why?
The tune() method is the most useful because string instruments need to be properly tuned to produce the correct notes. It is an important action before playing the instrument.
