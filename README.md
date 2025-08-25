# Vendor Performance Analysis

### (sql, python, powerbi)

_Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, and Power BI._

---

## Table of Contenets
- <a href = "#overview"> Overview </a>
- <a href = "#business-problem"> Business Problem </a>
- <a href = "#dataset"> Dataset </a>
- <a href = "#tools--technologies"> Tools & Technologies </a>
- <a href = "#project-structure"> Project Structure </a>
- <a href = "#data-cleaning--preparation"> Data Cleaning & Preparation </a>
- <a href = "#exploratory-data-analysis-eda"> Exploratory Data Analysis (EDA) </a>
- <a href = "#research-questions--key-findings"> Research Questions & Key Findings </a>
- <a href = "#dashboard"> Dashboard </a>
- <a href = "#how-to-run-this-project"> How to Run This Project </a>
- <a href = "#final-recommendations"> Final Recommendations </a>
- <a href = "#author-contact"> Author & Contact </a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization. A complete data pipeline was built using SQL for ETL, Python for analysis and hypothesis testing, and Power BI for visualization.

---

<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Effective inventory and sales management are critical for optimizing profitability in the retail and wholesale industry. Companies need to ensure that they are not incurring losses die to inefficient pricing, poor inventory turnover, or vendor dependency. The goal od this analysis is to :
- Identify underperforming brands that require promotional or pricing adjustments.
- Determine top vendors contributing to sales and gross profit.
- Analyze the impact of bulk purchasing on unit costs.
- Assess inventory turnover to reduce holding costs and improve efficiency.
- Investigate the profitability variance b/w high performance and low performance vendors.

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Multiple CSV files located in `/data/` folder (sales, vendors, inventory)
- This dataset is very large and have crores of rows of data which makes it more challanging and interesting to performe various analytical operations.
- `vendor-sales-summary` table create from ingested data and used for analysis.

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- SQL (Common Table Expression(cte), Joins, Filtering)
- Python (Pandas, Matplotlib, Seaborn, Scipy)
- Power Bi(Interactive Visualization, DAX)

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
vendor-performance-analysis/
|
|-- README.md
|-- .gitignore
|-- Vendor Performance Report.pdf
|
|-- notebook/               # Jupyter notebook
|   |-- exploratory_data_analysis.ipynb
|   |-- ingestion_creating_process.ipynb
|   |-- vendor_performance_analysis.ipynb  
|
|-- scripts/                # Python scripts for ingestion and processing
|   |-- ingestion_db.py
|   |-- get_vendor_summary.py
|
|-- dashboard/              # Power BI dashboard file
|   |-- Vendor Performance Analysis Dashboard.pbix
```

### Project Flow
<img width="1369" height="893" alt="Project Flow" src="https://github.com/user-attachments/assets/05d88314-e614-45f8-9d0d-8395abaef32b" />

---

<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preperation</h2>

### 1. Data Cleaning
- Gather raw data from multiple CSV files
- Import into SQL/Python/Power BI for processing.
- Check data structure (rows, columns, data types).
- Identify missing values, duplicates, and outliers.
- Verify column names, units, and formats.
- Drop duplicate rows.
- Filter out irrelevant or redundant columns.
- Keep only useful records for analysis.
- Convert data types (e.g., strings → dates, floats → integers).
- Standardize text fields (lowercase, remove spaces, special characters).
- Ensure consistent units (e.g., INR vs USD).


### 2. Data Preparation
- Remove transactions with:
    - Gross Profit <= 0
    - Profit Margin <= 0
    - Sales Quantity = 0

---

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

**Negative or Zero Values Detected:**
- Gross Profit : Min -52,002.78 (loss-making sales)
- Profit Margin : Min -∞ (sales at zero pr below cost)
- Unsold Inventory : Indicating slow-moving stock

**Outliers Identified:**
- High Freight Costs (upto 257k)
- Large Purchase/Actual Prices

**Correlation Analysis:**
- Weak between Purchase Price and Profit
- Strong between Purchase Qty & Sales Qty (0.999)
- Negative between Profit Margin & Sales Price (-0.179)

---

<h2><a class="anchor" id="research-questions--key-findings"></a>Reseach Question & Key Findings</h2>

1. **Brands for Promotions:** 198 brands with low sales but high profit margins
2. **Top Vendors:** Top 10 vendors = 65.69% of purchases -> risk of over-reliance
3. **Bulk Purchasing Impact:** 72% cost savings per unit in large orders
4. **Inventory Turnover:** $2.71M worth of unsold inventory
5. **Vendor Profitability:** 
    - High Vendors: Mean Margin = 31.17%
    - Low Vendors: Mean Margin = 41.55%
6. **Hypothesis Testing:** Statistically significant difference in profit margins -> distinct vendor straregies

---

<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

- Power BI Dashboard Shows:

    1. **Visualizations**
    - Top 10 Vendors by Purchase Contribution
    - Top Brands by Sales
    - Top Vendors by Sales
    - Low Performing Vendors
    - Low Performing Brands

    2. **Measures**
    - Sum of Gross Profit
    - Total Purchase
    - Total Unsold Capital
    - Profit Margin
    - Total Sales
### Vendor Performance Analysis Dashboard
<img width="1390" height="787" alt="Vendor Performance Dashboard" src="https://github.com/user-attachments/assets/34b009f4-1acd-4fce-94f1-ebc27ec9aaf1" />

---

<h2><a class="anchor" id="how-to-run-this-project"></a> How to Run This Project</h2>

1. Clone the repository:
```bash
git clone https://github.com/AbhishekAdil/vendor-performance-analysis-sql-python-powerbi
```

2. Load the CSVs and ingest into database:
```bash
python scripts/ingestion_db.py
```

3. Create vendor summary table:
```bash
python scripts/get_vendor_summary.py
```

4. Open and rum notebooks:
    - `notebook/exploratory_data_analysis.ipynb`
    - `notebooks/vendor_performance_analysis.ipynb`

5. Open Power BI Dashboard:
    - `dashboard/Vendor Performance Analysis Dashboard.pbix`

---

<h2><a class="anchor" id="final-recommendations"></a> Final Recommendation</h2>

- Diversify vendor base to reduce risks
- Optimize bulk order strategies
- Reprice slow-moving, high-margin brands
- Clear unsold inventory strategically
- Improve marketing for underperforming vendors

<h2><a class="anchor" id="author-contact"></a> Author & Contact</h2>

**Abhishek Adil**

Data Analyst

Email: abhishek.adil2002@gmail.com

[LinkedIn](https://www.linkedin.com/in/abhishek-adil-2285351b8/) : abhishekadil
