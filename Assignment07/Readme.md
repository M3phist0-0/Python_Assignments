# Programming Assignment 7  
# Debt Repayment & Amortization Simulator (GUI Application)

## Overview

Assignment 7 implements a modular, GUI-based loan repayment simulator that generates a full amortization schedule and allows users to explore repayment scenarios including lump-sum payments and extra monthly contributions.

The application integrates:

- Tkinter + ttkbootstrap GUI
- Financial computation engine
- Amortization table generator
- CSV export functionality
- Persistent logging system
- Modular package structure

This project demonstrates advanced Python concepts including object-oriented design, GUI development, financial modeling, logging infrastructure, and structured project architecture.

---

# Application Architecture

## 1. Entry Layer

### `dashboard.py`
- Launches the GUI application
- Instantiates the `DebtAPP` class
- Injects the `AmortizationTable` engine into the GUI

---

## 2. GUI Layer (`GUI.py`)

The GUI is built using:

- `tkinter`
- `ttkbootstrap`

### Main Class: `DebtAPP`

The primary application window that:

- Accepts loan inputs:
  - Loan type
  - Loan balance
  - Interest rate
  - Loan duration
- Displays calculated:
  - Monthly payment
  - Total repaid
  - Total interest
- Allows users to:
  - Generate amortization table
  - Add lump-sum payments
  - Add extra monthly payments
  - Recalculate repayment
  - View payoff analytics

### Additional GUI Components

- TopWindow (Loan Inputs)
- Payment (Calculated Outputs)
- ExtraInputField (Lump Sum & Extra Payment)
- UpdatedPayment (Scenario Analysis)

---

## 3. Financial Computation Layer (`tools/helper_functions.py`)

Implements core financial formulas:

### `calculate_payments()`
Computes fixed-rate loan monthly payment using standard amortization formula.

### `calculate_total_paid()`
Calculates total repayment amount across the loan term.

### `calculate_total_interest()`
Calculates total interest paid over the life of the loan.

This layer acts as the computational backend for the GUI.

---

## 4. Logging Layer (`tools/my_logger.py`)

Implements a structured logging system:

- Creates directory:  
  `debt_repayment/files/logs/`
- Writes to:  
  `getting_out_of_debt.log`
- Logs:
  - Initialization
  - Loan parameters
  - Table creation
  - CSV export events
- Includes:
  - Timestamp (UTC)
  - Log level
  - Logger name
  - Line number

This demonstrates persistent logging and traceability.

---

## 5. Amortization Engine (`amortization_table/table.py`)

### Class: `AmortizationTable`

Core engine responsible for:

- Generating amortization schedule
- Calculating:
  - Monthly interest
  - Monthly principal
  - Remaining balance
- Storing results in a Pandas DataFrame
- Saving amortization schedule to CSV
- Performing repayment analytics

---

## Amortization DataFrame Structure

Each row includes:

- Payment #
- Due date
- Payment amount
- Principal paid
- Interest paid
- Remaining balance

---

## Analytical Methods

### `more_principal()`
Returns first payment where principal paid exceeds interest paid.

### `halfway()`
Returns payment number when half of the original loan balance is paid.

### `update_payments()`
Allows:
- Lump-sum balance reduction
- Increased monthly payments
- Regeneration of amortization table

---

# Features

- Fixed-rate loan modeling
- Dynamic repayment scenario modeling
- CSV export of amortization schedule
- Persistent structured logging
- Modular project organization
- GUI-driven financial simulation
- Real-time recalculation of loan outcomes

---

# How to Run

From the root directory:
