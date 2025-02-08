# Computational Statistics with Metropolis-Hastings Algorithm

## Overview
This repository contains a Jupyter Notebook implementing computational statistics methods, focusing on **Bayesian inference** using the **Metropolis-Hastings (MH) algorithm**. The notebook demonstrates how to estimate parameters of a **Probit regression model** using MCMC sampling techniques.

## Features
- **Probit Regression**: Uses `statsmodels` to estimate parameters.
- **Bayesian Inference**: Implements Bayesian updating with a specified prior.
- **Metropolis-Hastings Algorithm**: Generates posterior samples.
- **Diagnostic Tools**: Includes convergence diagnostics and visualization of sampled distributions.
- **Synthetic Data Generation**: Simulates test datasets for model validation.

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install numpy scipy pandas matplotlib statsmodels openpyxl
```

## Usage
### 1. Load and Run the Notebook
Simply open the Jupyter Notebook and execute the cells in sequence:
```bash
jupyter notebook "Code Computational Statistics.ipynb"
```

### 2. Data Input
The code can load real-world data from an Excel file. Update `excelpath` to point to your dataset:
```python
excelpath = "path/to/your/data.xlsx"
```
Alternatively, synthetic data can be generated for testing.

### 3. Running the Metropolis-Hastings Algorithm
Execute the `MH_Algo()` function:
```python
MH_Algo(tau=0.1, excelpath="data.xlsx", num_output=1000, precision=1e-4)
```
- `tau`: Scaling parameter for proposal distribution.
- `num_output`: Number of MCMC iterations.
- `precision`: Controls numerical stability.

### 4. Diagnostic Checks
The notebook provides:
- **Acceptance Rate**: Tracks the ratio of accepted proposals.
- **Time Series Plots**: Visualizes parameter evolution.
- **Summary Statistics**: Reports posterior mean and variance.

## File Structure
- `Code Computational Statistics.ipynb`: Main Jupyter Notebook containing all computations.
- `data.xlsx` (optional): Input dataset (if using real data).


