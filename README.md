# IBM Data Science Capstone — Automobile Sales Analysis

Educational analysis of IBM Skills Network's `historical_automobile_sales.csv` dataset.

## Project contents
- `notebooks/Part1_Automobile_Sales_Visualization.ipynb`: visualization tasks using Pandas, Matplotlib, Seaborn and Folium.
- `code/Part2_Automobile_Sales_Dashboard.py`: interactive Plotly Dash dashboard.
- `code/automobile_sales_analysis.sql`: SQL analysis queries.
- `code/classification_analysis.py`: optional recession classification extension.
- `code/folium_context_map.py`: context-only Folium map. The source dataset has no verified sale coordinates, so this is not a sales-density map.
- `requirements.txt`: Python dependencies.

## Dataset
IBM Skills Network `historical_automobile_sales.csv`:
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv

The course dataset is artificially generated for learning. Treat results as educational, not real market evidence.

## Install
```bash
pip install -r requirements.txt
```

## Run dashboard
```bash
python code/Part2_Automobile_Sales_Dashboard.py
```
Open http://127.0.0.1:8050.

## Run classification extension
```bash
python code/classification_analysis.py
```
Only report model scores after executing the script and recording the actual outputs.

## SQL
Import the CSV into SQLite or another SQL database as `automobile_sales`, then run `code/automobile_sales_analysis.sql`.

## Before submission
Run all notebook cells, execute SQL and classification, capture genuine dashboard/map evidence, and include the final presentation PDF. Do not invent scores or map insights.