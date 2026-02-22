# Programming Assignment: Object-Oriented Design & Data Processing in Python

## Overview

This project was completed as a programming assignment to demonstrate proficiency in Object-Oriented Programming (OOP), data cleaning, file processing, operator overloading, inheritance, and unit testing in Python.

The assignment is divided into two major components:

1. Auto MPG Data Processing System
2. Shelter Class Hierarchy with Inheritance

Both components emphasize clean class design, comparison logic, and proper use of Python’s object model.

---

# Part 1: Auto MPG Data System

**Files:**
- `autompg.py`
- `test_autompg.py`

## Objective

Implement a system that:

- Cleans raw automobile MPG data
- Loads structured data from a cleaned file
- Instantiates objects representing vehicles
- Supports sorting, comparison, hashing, and equality checks

---

## AutoMpg Class

Defined in `autompg.py`.

### Attributes
- `make`
- `model`
- `year`
- `mpg`

### Implemented Methods

- `__repr__()` — formatted object representation
- `__str__()` — calls `__repr__`
- `__lt__()` — comparison by make, model, year, and mpg
- `__eq__()` — equality comparison using all attributes
- `__hash__()` — enables use in sets and dictionaries

This class supports full object comparison behavior.

---

## AutoMPGData Class

Responsible for:

- Cleaning raw data file (`auto-mpg.data`)
- Writing a cleaned version (`auto-mpg.clean`)
- Parsing structured data using `csv`
- Creating `AutoMpg` objects from file data
- Supporting iteration via `__iter__()`

The cleaning step standardizes spacing and formatting before parsing.

---

## Unit Testing (AutoMPG)

`test_autompg.py` validates:

- `__str__()` formatting
- Equality behavior
- Less-than comparisons
- Hash consistency
- File cleanup after tests

Testing ensures correct implementation of all magic methods and data handling logic.

---

# Part 2: Shelter Class Hierarchy

**Files:**
- `shelter.py`
- `test_shelter.py`

## Objective

Design a class hierarchy representing different shelter types using inheritance and polymorphism.

---

## Base Class: Shelter

### Attributes
- `num_occupants`
- `material`
- `setup_time`
- `weight`
- `seasons`

### Methods

- `is_better()` — compares two shelters based on:
  - Lower weight
  - Faster setup time
  - Equal or higher season rating

- `total_sleep_spots()` — static method that sums occupants across multiple shelters
- `__repr__()` and `__str__()` — structured output formatting

---

## Subclasses

### Tent
Adds:
- `sqft`
- `vestibule`
- `structure_poles`

Overrides `__lt__()` to compare by occupants and square footage.

---

### Tarp
Adds:
- `sqft`

Overrides `__lt__()` to compare by occupants and square footage.

---

### Hammock
Adds:
- `length`

Overrides `__lt__()` to compare weight and setup time.

---

## OOP Concepts Demonstrated

- Inheritance using `super()`
- Method overriding
- Polymorphism
- Operator overloading (`__lt__`, `__eq__`, `__hash__`)
- Static methods
- Encapsulation of comparison logic
- Type checking with `type()`
- Iteration protocol implementation

---

## Unit Testing (Shelter)

`test_shelter.py` validates:

- Proper string formatting
- Correct `__lt__()` behavior across subclasses
- Correct `is_better()` logic
- Object cleanup after tests

Each subclass is tested independently to verify polymorphic behavior.

---

# How to Run

### Run Auto MPG Program
```bash
python autompg.py