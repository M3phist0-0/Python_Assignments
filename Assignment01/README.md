# Programming Assignment: Object-Oriented Shelter Modeling in Python

## Assignment Overview

This project was completed as a programming assignment to demonstrate understanding of core Object-Oriented Programming (OOP) principles in Python. The goal of the assignment was to design and implement a class hierarchy that models different types of outdoor shelters while applying inheritance, method overriding, operator overloading, and structured comparison logic.

The project also includes standalone functions that demonstrate list manipulation, tuple processing, boolean filtering, and control flow.

---

## Learning Objectives

This assignment reinforces the following concepts:

- Class construction and attribute management  
- Inheritance and superclass/subclass relationships  
- Method overriding  
- Polymorphism  
- Special (magic) methods: `__str__`, `__repr__`, and `__lt__`  
- Static methods  
- Boolean logic and conditional expressions  
- List processing with `zip` and `itertools.zip_longest`  

---

## Part 1–2: List Pairing and Filtering

The first portion of the assignment implements functions that:

- Pair two lists together using `zip` and `zip_longest`
- Handle uneven list lengths using placeholder values
- Filter paired tuples based on whether numeric values are even or odd
- Return new lists based on conditional logic

These functions demonstrate:

- Looping and control flow
- Conditional branching
- Boolean parameter usage
- Tuple indexing and modular arithmetic

---

## Part 3–5: Shelter Class Implementations

The core portion of the assignment required implementing multiple related classes to model different shelter types.

Each shelter type includes attributes such as:

- Number of occupants  
- Material  
- Setup time  
- Weight  
- Season rating  

Each class implements:

- `__str__` for readable object output  
- `__repr__` for simplified object representation  
- `__lt__` for object comparison  
- `is_better()` method for evaluating performance  

---

## Shelter Class Hierarchy

### `Shelter` (Base Class)

Defines shared attributes and behavior common across all shelters.  
Includes:

- Shared initialization logic  
- A general `is_better()` comparison method  
- A static method `total_sleep_spots()` to aggregate occupancy  

---

### `Tent`

Extends `Shelter` and adds:

- Square footage (`sqft`)  
- Vestibule indicator  
- Structural pole indicator  

Overrides comparison logic based on occupant capacity and square footage.

---

### `Hammock`

Extends `Shelter` and adds:

- Length attribute  

Implements comparison logic prioritizing weight and setup efficiency.

---

### `Tarp`

Extends `Shelter` and adds:

- Square footage  

Overrides comparison behavior based on size and occupant capacity.

---

## Key Programming Concepts Demonstrated

- Inheritance using `super()`  
- Polymorphic behavior through overridden `__lt__` methods  
- Type checking using `isinstance`  
- Encapsulation of comparison criteria  
- Static methods  
- Operator overloading  

---

## Purpose of the Assignment

The purpose of this assignment was to practice structuring related classes within a clean hierarchy, applying comparison logic across objects, and reinforcing Python’s object-oriented design principles. The focus of the project is clarity, organization, and correct application of OOP concepts.