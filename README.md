# sales-forecasting-ai
# Sales Forecasting Dataset Analysis

## Overview
This analysis explores a sales dataset to identify key trends, correlations, and patterns that influence sales performance. The dataset includes sales transactions across multiple stores and products.

## Data Cleaning Process
- Converted `date` column to datetime format.
- Removed duplicate entries.
- Standardized categorical data formatting (lowercase, stripped whitespace).
- Filled missing `date` values using forward-fill and backward-fill methods.
- Ensured numerical columns were properly formatted.

## Key Findings

### **1. Correlation Analysis**
- **Total Sales vs Quantity Sold:** Strong correlation (~1.00) confirms that increasing sales volume is a key driver of revenue.
- **Total Sales vs Unit Price:** High-priced products significantly contribute to total revenue.
- **Base Price vs Unit Price:** Strong correlation suggests that product pricing strategies align with base costs.
- **Weak impact of Seasonality:** No strong correlation between sales and month, indicating limited seasonal effects.

### **2. Visualizations & Insights**
- **Sales Trend Over Time:** Shows fluctuations in total sales across different dates.
- **Total Sales by Product Category:** Highlights which categories contribute the most to sales.
- **Monthly Sales Trend:** Examines whether sales vary across months.
- **Quantity Sold vs Unit Price:** Helps determine pricing strategies based on sales volume.

## Visualizations
- **Correlation Matrix Heatmap**
- **Scatter Plots for Key Correlations**
- **Time Series Sales Trends**
- **Sales Distribution Across Categories**




 
