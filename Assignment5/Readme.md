# Programming Assignment 5: Real Estate Data Processing & Statistical Analysis

## Overview

This assignment implements a modular real estate data processing system using object-oriented design, custom context managers, and functional-style statistical computation.

The project loads structured property data from a CSV file, organizes listings by state and territory, and computes various real estate statistics such as cheapest, priciest, best deal, and budget-friendly properties.

The design emphasizes modularity, separation of concerns, and reusable helper functions.

---

## Learning Objectives

This assignment demonstrates:

- Object-Oriented Programming (OOP)
- Modular project organization
- Custom context managers (`__enter__`, `__exit__`)
- Namedtuple data containers
- Nested `defaultdict` structures
- Functional programming techniques
- Dictionary-based dispatch (function mapping)
- File handling and directory management
- Data filtering and validation
- Statistical computation

---

# Core Components

## 1. `RealEstate` Class (`load.py`)

The `RealEstate` class is responsible for:

- Loading property data from CSV
- Creating namedtuple containers dynamically
- Organizing properties by:
  - US States
  - US Territories
- Storing data in a nested dictionary structure
- Computing statistics via function dispatch

### Key Methods

- `load_data()`  
  Uses a custom context manager to safely change directories and read the CSV file.

- `_create_container()`  
  Dynamically creates a namedtuple class from CSV headers.

- `compute_stats()`  
  Uses dictionary-based dispatch to call statistical helper functions.

---

## 2. Custom Context Manager (`context_manager.py`)

Implements a manual context manager that:

- Temporarily changes the working directory
- Opens a file
- Restores the original directory upon exit
- Ensures file closure

Demonstrates understanding of:

- `__enter__`
- `__exit__`
- Resource management
- Safe file handling

---

## 3. Statistical Helper Functions (`calculate_stats.py`)

Defines multiple real estate evaluation functions:

### `cheapest`
Returns the lowest-priced property within a specified state.

### `priciest`
Returns the highest-priced property within a specified state.

### `dirt_cheap`
Returns the absolute cheapest property across all states and territories.

### `best_deal`
Returns the best value property in a state based on price-to-size ratio.

### `budget_friendly`
Returns the best price-per-size property that meets:
- Bedroom requirement
- Bathroom requirement
- Maximum budget constraint

All statistical computations rely on:

- Filtering invalid numeric fields
- Converting string values safely
- Using `min()` and `max()` with lambda expressions

---

## 4. `run.py`

Acts as the entry point.

Responsibilities:

- Instantiates the `RealEstate` class
- Prints sample property data
- Calls statistical functions
- Handles runtime exceptions gracefully

---

# Data Organization

Properties are stored in a nested dictionary:
