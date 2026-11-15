# Intelligent Data Platform

A Python project that loads, cleans, analyzes and visualizes sales data,
trains a simple prediction model and builds an HTML dashboard.

## Structure
- `src/` : data loading, cleaning, analysis and charts
- `models/` : sales prediction model (linear regression)
- `dashboard/` : HTML dashboard builder
- `tests/` : automated tests with pytest
- `data/` : raw and processed data

## How to run
    pip install -r requirements.txt
    python main.py
    python -m pytest

## Technologies
Python, pandas, matplotlib, numpy, pytest