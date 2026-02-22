# Assignment 8 – Baby Names Data Analysis System

## Overview

This programming assignment implements a modular Python application for analyzing historical U.S. baby name data across multiple centuries. The project emphasizes structured package design, generator-based data ingestion, recursive file traversal, and data analysis using Pandas.


---

## Module Responsibilities

### `main.py`

Entry point for the application.

- Initializes file retrieval
- Constructs the BabyNames class
- Executes analysis operations

---

### `contents/babynames.py`

Core analysis class responsible for:

- Constructing a Pandas DataFrame from generator output
- Filtering by year and gender
- Aggregating name popularity statistics
- Performing analytical queries

---

### `contents/helper_functions/hf.py`

Data ingestion layer.

#### `retrieve_files(filetype)`

- Recursively searches directories
- Identifies matching `.txt` files
- Returns file path list

#### `record_loader_gen(files)`

- Extracts year from filename using regex
- Opens each file
- Parses records
- Yields structured tuples using a generator

This approach avoids loading all data into memory at once.

---

### `contents/baby_names/`

Contains raw dataset files grouped by century.

Each file:
- Represents one year
- Follows consistent CSV format: