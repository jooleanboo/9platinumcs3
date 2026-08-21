# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
I can use encapsulation by designing a Product class to manage important details such as the item’s name, cost, and available quantity. Instead of allowing other parts of the program to directly change these values, I can provide functions like get_stock() and update_stock() to safely retrieve and adjust the inventory. This makes the code more structured, easier to manage, and protects the product data from unintended changes.

### 2. Abstraction
I can use abstraction to simplify the way my inventory system works by providing straightforward functions for tasks that would otherwise involve several steps. For instance, a sell_product() function could handle updating the available stock automatically, so I wouldn’t need to deal with the calculations each time a product is sold. This keeps the code cleaner and makes the system easier for me to work with.

### 3. Inheritance
I can structure the inventory system around a main Product class and then build more specific classes, such as SchoolProduct and FoodProduct, from it. The specialized classes would automatically receive common details like the product name, cost, and available quantity. This avoids defining the same information repeatedly and makes it simpler to introduce additional product categories later.

### 4. Polymorphism
I can use polymorphism by defining a common function for different types of products while letting each product category decide how that function behaves. For instance, FoodProduct and SchoolProduct could both have a display_info() function, but each one could present details relevant to its own category. This lets the inventory system use the same function call for different products without needing separate method names.

## Reflection
Reflection on the Most Useful OOP Pillar

Among the four pillars of Object-Oriented Programming, I think inheritance would be the most useful for the sari-sari store inventory system. I can create a general Product class and use it to make other classes like FoodProduct and SchoolProduct. These classes can reuse things like the product name, price, and stock instead of writing them again. I think inheritance is useful because it reduces repeated code and makes the inventory system easier to organize and add to in the future.
