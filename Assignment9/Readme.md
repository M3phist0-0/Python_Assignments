# Assignment 9 – Probability Distributions and Data Visualization

## Overview

This assignment focuses on probability distribution generation, data visualization using Matplotlib, and unit testing with Python’s `unittest` framework.

The project implements two distribution-generating classes and multiple plotting functions to visualize trigonometric functions. It reinforces object-oriented programming, NumPy usage, error handling, and automated testing practices.

---

## Learning Objectives

This assignment was designed to practice:

- Object-oriented programming in Python
- Generating probability distributions using NumPy
- Data visualization with Matplotlib
- Writing and running unit tests
- Error handling and validation
- Code modularity and reproducibility

---

## Core Components

### `Distributions` Class

Defined in `homework9.py`.

This class generates probability distributions based on user input.

Supported distributions:

- Normal
- Lognormal
- Laplace

Attributes:

- `distribution` – distribution type
- `mean` – distribution mean
- `std` – standard deviation
- `size` – sample size
- `data` – NumPy array of generated samples

The method `gen_norm_distro()` generates the specified distribution and raises a `ValueError` if an invalid distribution type is provided :contentReference[oaicite:2]{index=2}.

---

### `NumpyDistributions` Class

Also defined in `homework9.py`.

This class performs similar functionality but explicitly emphasizes NumPy-based generation methods.

It includes:

- Distribution validation
- Data generation
- String representation method

Both classes demonstrate encapsulation and reproducible data generation.

---

## Visualization Functions

Three plotting functions are included:

### `plot_sin_cos_axes()`

Plots sine and cosine on the same axes.

### `plot_sin_cos_shared_y()`

Creates two stacked subplots sharing the y-axis.

### `plot_sin_cos_shared_x()`

Creates two side-by-side subplots sharing the x-axis.

These functions demonstrate:

- Matplotlib subplot configuration
- Axis sharing
- Proper labeling and formatting

---

## Unit Testing

All functionality is validated using `unittest` in `test_homework9.py` :contentReference[oaicite:3]{index=3}.

Test coverage includes:

- Normal distribution generation
- Lognormal distribution generation
- Laplace distribution generation
- Invalid distribution type handling
- Negative standard deviation validation
- Statistical verification of generated sample mean and standard deviation

This ensures correctness, robustness, and error handling.

---

## How to Run

### Install Dependencies

```bash
pip install numpy matplotlib