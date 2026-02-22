# Assignment 2  
## AutoMPG Object-Oriented Data Loader

---

## Overview

This assignment implements an object-oriented system for reading, cleaning, and modeling automobile MPG data.

The project introduces:

- Object-Oriented Programming (OOP)
- File input/output operations
- Data cleaning techniques
- Named tuples
- Custom object comparison methods
- Iteration over user-defined classes

The program reads automobile data, cleans it if necessary, loads it into structured `AutoMPG` objects, and prints each record.

---

# Program Structure

## `AutoMPG` Class

Represents a single automobile.

### Attributes

- `make` — Manufacturer of the vehicle
- `model` — Model name
- `year` — Model year (converted to full year format)
- `mpg` — Miles per gallon

### Implemented Methods

- `__init__` — Constructor
- `__repr__` — Returns string representation
- `__str__` — Formats object as `AutoMPG(make, model, year, mpg)`
- `__eq__` — Equality comparison
- `__lt__` — Less-than comparison
- `__hash__` — Enables use in sets/dictionaries

These methods allow objects to be:

- Compared
- Sorted
- Hashed
- Printed cleanly

---

## `AutoMPGData` Class

Responsible for:

- Loading automobile data
- Cleaning raw data
- Creating `AutoMPG` objects
- Storing objects in a list
- Supporting iteration

### Key Methods

#### `__init__`
Initializes the object and loads data.

#### `_load_data`
- Checks if `auto-mpg.clean.txt` exists
- Calls `_clean_data()` if necessary
- Uses a named tuple (`Record`) to parse each row
- Extracts:
  - Make
  - Model
  - Year
  - MPG
- Creates `AutoMPG` objects
- Stores them in `self.data`

#### `_clean_data`
- Reads `auto-mpg.data.txt`
- Expands tabs
- Standardizes formatting
- Writes cleaned data to `auto-mpg.clean.txt`

---

# Running the Program

From the directory containing the file:

```bash
python3 Assignment2_sol.py