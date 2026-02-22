# Programming Assignment 4: CSV Data Processing & Statistical Analysis

## Overview

This assignment focuses on CSV file processing, structured data storage, custom exception handling, and statistical analysis using Python collections.

The program loads structured datasets, standardizes column names, dynamically creates namedtuple containers, computes frequency statistics using `Counter`, and extracts the top N most common values from specified columns.

Unit tests validate the correctness of the implementation.

---

## Files Included

- `assignment4.py` – Main implementation
- `test_assignment4.py` – Unit tests
- `credit_card.csv` – Dataset 1
- `customer_complaints.csv` – Dataset 2

---

## Learning Objectives

This assignment demonstrates:

- CSV file handling
- Data cleaning and normalization
- Namedtuple container creation
- Use of `defaultdict` and `Counter`
- Custom exception design
- Lambda expressions
- Unit testing with `unittest`
- Structured dictionary data storage
- Defensive programming

---

## Program Structure

### Custom Exceptions

Two custom exceptions are implemented:

#### `InvalidColumnNames`
Raised when column names contain invalid (non-alphanumeric) characters.

#### `NoRecordStatsFound`
Raised when statistics are requested for a column that does not exist or has not been processed.

---

## Records Class

The `Records` class is responsible for:

- Loading CSV data
- Standardizing column names
- Creating namedtuple containers
- Storing data in nested dictionaries
- Computing column statistics
- Extracting top N frequency results

---

### Key Methods

#### `load_data()`
- Reads CSV file
- Cleans header names
- Creates namedtuple entries
- Stores data in a nested `defaultdict`

---

#### `_standardize_col_names(col_names)`
- Converts column names to lowercase
- Removes non-alphanumeric characters
- Raises `InvalidColumnNames` if invalid fields are detected

---

#### `record_stats(file_title, column_name, lambda_func)`
- Extracts a specified column
- Applies lambda function
- Computes frequency using `Counter`
- Stores statistics in internal dictionary
- Returns `(column_name, Counter)`

---

#### `extract_top_n(n, file_title, stats_column_name)`
- Retrieves most common values from stored stats
- Returns a list of `(value, count)` tuples
- Raises `NoRecordStatsFound` if stats are unavailable

---

## Data Storage Structure

Data is stored using nested `defaultdict` structures:
