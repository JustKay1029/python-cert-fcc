## Object-Oriented Programming (OOP) Quick Review Guide

* **Object-Oriented Programming (OOP)**: A programming style where code is organized around real-world objects using four core pillars: **encapsulation**, **inheritance**, **polymorphism**, and **abstraction**.
* **Classes**: The blueprints used to create objects, defining their initial attributes (data) and methods (behaviors).

---

### Core Pillars of OOP

#### 1. Encapsulation

* **Definition**: Bundling an object's data and methods into a single unit while hiding its internal state from unauthorized direct access.

 **Access Control Conventions**:
* Single underscore prefix (`_variable`): A developer convention indicating an attribute or method is meant for internal/protected use only.
* Double underscore prefix (`__variable`): Triggers **name mangling**, renaming the attribute internally to `_ClassName__variable` to prevent accidental overriding or outside access.


 **Getters, Setters, and Properties**:
* Getters (using `@property`) retrieve values securely, while setters (using `@property_name.setter`) validate and modify values.
* Properties allow attributes to be accessed using clean dot notation (e.g., `my_circle.radius`) rather than calling explicit getter/setter methods.
* Deleters (`@property_name.deleter`) manage custom logic when an attribute is deleted via the `del` keyword.



#### 2. Inheritance

* **Definition**: The process where a child class acquires the attributes and methods of a parent class to promote code reuse and establish clear hierarchical relationships.
* **Types**:
* *Single Inheritance*: A child class inherits from one parent class.
* *Multiple Inheritance*: A child class inherits from more than one parent class simultaneously.


* **The `super()` Function**: Used to call methods from a parent class, allowing subclasses to extend or modify parent behavior without code duplication.

#### 3. Polymorphism

* **Definition**: The ability of different classes to share the same method name while implementing unique behaviors tailored to each class.
* **Inheritance-Based Polymorphism**: A parent class defines a standard method interface, and each child class overrides it with its own custom implementation.

#### 4. Abstraction

* **Definition**: Hiding complex internal implementation details and exposing only the essential features to keep systems manageable.
* **Implementation in Python**: Utilizes the `abc` module, requiring the `ABC` base class and the `@abstractmethod` decorator to enforce that child classes implement required methods.

---

### Common Pitfalls & Student Confusions

* **Assigning Directly to Properties in Setters**: Inside a setter method, assigning a value directly to the property name (e.g., `self.radius = value` inside the `radius` setter) triggers an infinite recursive loop (`RecursionError`). Always store the value in an internal auxiliary attribute (e.g., `self._radius = value`).
* **Treating Single Underscores as Private**: Relying on a single underscore (`_attribute`) for strict data hiding. Python does not restrict access to single-underscore variables from outside the class; it is strictly a naming convention for internal use.
* **Forgetting to Override Abstract Methods**: Trying to instantiate an abstract base class or forgetting to implement an `@abstractmethod` in a concrete subclass will throw a `TypeError`.
* **Misunderstanding Name Mangling**: Assuming double underscores (`__attr`) make variables completely secure. They can still be accessed externally if you explicitly use their mangled name (`_ClassName__attr`), as Python only changes the name internally to prevent inheritance collisions.

---

`self` represents the specific instance of the class you are currently creating or interacting with.

When you define a class, it acts as a blueprint. A single blueprint can be used to build dozens of unique objects (for instance, creating multiple unique `Circle` or `Wallet` instances). Python needs a way to know *which* specific object's data you are modifying or reading at any given moment. That is what `self` hands to the method—a direct reference to the individual object currently calling the method.

Writing `self.name = name` inside an `__init__` constructor accomplishes two things:

1. **`name` (the parameter)**: Receives whatever value you pass in when you instantiate the object (e.g., `user = User("Kavya")`).
2. **`self.name` (the instance attribute)**: Binds that incoming value to the specific object (`self`), storing it in that object's local namespace (its internal dictionary, `__dict__`) so it can be accessed later by other methods using `self.name`.

Without `self`, Python wouldn't know whether `name = name` was meant to update a global variable, a local function variable, or which specific object's data to change. While `self` is just a naming convention and Python technically accepts any valid identifier in its place, sticking to `self` is a universally accepted standard that keeps your code readable for other developers.

---

### Practice Interview Questions

1. **What is the primary difference between data hiding achieved via single underscores (`_`) versus double underscores (`__`) in Python?**
2. **Why should you use `@property` getters and setters instead of writing traditional getter methods (like `get_radius()`) and setter methods (like `set_radius()`)?**
3. **What happens if you try to assign a value to a property name inside its own setter method, and how do you prevent it?**
4. **How does Python's `super()` function work in the context of multiple inheritance, and what role does the Method Resolution Order (MRO) play?**
5. **Explain how abstraction differs from encapsulation. Can you give a real-world programming example of each?**

