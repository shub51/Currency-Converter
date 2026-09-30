# Project Design

## Main Modules

### 1. main.py

Handles the menu and interaction with the user.

### 2. converter.py

Performs the currency conversion.

### 3. currencies.py

Stores the names of the supported currencies.

### 4. history.py

Displays previous conversion records.

## Workflow

User
   |
   v
Main Menu
   |
   v
Enter Amount
   |
   v
Select Currencies
   |
   v
Currency Conversion
   |
   v
Display Result
   |
   v
Save History

## Functional Requirements

- The program should accept an amount.
- The program should accept a source currency.
- The program should accept a target currency.
- The program should calculate the converted amount.
- The program should display the result.
- The program should save conversion history.

## Non-Functional Requirements

- The program should be simple to use.
- The program should give useful error messages.
- The program should be easy to understand.
- The program should run using standard Python.

## Limitation

The exchange rates are fixed sample rates.
The program does not use a live currency API.