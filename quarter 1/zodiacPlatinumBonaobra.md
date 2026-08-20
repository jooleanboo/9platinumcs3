# Chinese Zodiac Activity
## Requirements:
The requirements are to create a Python program that asks the user to input their birth year, with 1900 serving as the starting reference year. The program must validate the entered year and display an error message before stopping if the year is earlier than 1900. If the year is valid, the program should determine the user’s Chinese zodiac sign based on their birth year. The zodiac signs follow a 12-year cycle in this order: Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, and Pig, then repeat.

---
## Code
```python 
year = int(input("Enter your birth year: "))

zodiac_signs = [ 
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

if year < 1900:
    print("Invalid Year, it should not be earlier than 1900.")
    
else:
    index = (year - 1900) % 12
    print("Your Chinese Zodiac Sign is:", zodiac_signs[index])
```
