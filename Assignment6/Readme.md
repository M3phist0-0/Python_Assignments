# Programming Assignment 6: Real Estate Data Analysis with Pandas

## Overview

This assignment builds upon previous real estate data processing work by transitioning to a Pandas-based data analysis approach. The project loads, cleans, filters, and analyzes real estate property data using DataFrame operations and aggregation functions.

The objective of this assignment is to demonstrate proficiency with:

- Pandas DataFrames
- Data cleaning and type conversion
- Filtering and grouping
- Statistical summarization
- Modular class design

---

## Files Included

- `production.py` – Final implementation
- `prototyping.ipynb` – Jupyter notebook used for experimentation and development
- `realtor-data.csv` – Real estate dataset
- `data/` – Directory containing dataset

---

## Learning Objectives

This assignment demonstrates:

- Object-Oriented Programming (OOP)
- DataFrame manipulation using Pandas
- CSV file loading and validation
- Handling missing values
- Converting column types to numeric
- Removing duplicates
- Group-by aggregation
- Summary statistics generation
- Defensive column validation
- Modular design with helper methods

---

# Core Class: `RealEstate2`

The `RealEstate2` class is responsible for:

- Loading real estate data from CSV
- Cleaning and converting column types
- Filtering data by state
- Computing summary statistics
- Handling null values
- Removing unwanted records

---

## Key Methods

### `load_data()`

- Reads dataset using `pandas.read_csv`
- Converts numeric columns
- Drops duplicates
- Optionally filters dataset by state

---

### `_col_2_numeric()`

- Converts applicable columns to numeric type
- Uses `errors='coerce'` to safely handle invalid entries

---

### `filter_by_location(location_col, location_val)`

- Filters dataset by a specified column and value
- Returns a filtered DataFrame

---

### `num_nulls(col_name)`

- Returns number of null values in a specified column

---

### `get_unique_vals(col_name)`

- Returns:
  - Number of unique values
  - Array of unique entries

---

### `filth_be_gone(col_name, value)`

- Removes rows containing a specified value
- Reports number of rows removed

---

### `col_val_count(col_name)`

- Returns frequency counts for a column

---

### `helper_sum_stat(col_name)`

- Computes percentage of values above the median
- Demonstrates statistical aggregation

---

### `summary_table(col_name)`

Generates grouped summary statistics including:

- Mean
- Minimum
- Maximum
- Count
- Percentage of values above median

Grouped by:
- State
- City

Returns a structured DataFrame of summary metrics.

---

# Example Execution

Run from project root:

```bash
python production.py