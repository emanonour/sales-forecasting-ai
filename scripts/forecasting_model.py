# Selecting numerical columns for correlation matrix
numerical_cols = ['quantity', 'unit_price', 'base_price', 'total_sales', 'month', 'sales_seasonality']
correlation_matrix = df[numerical_cols].corr()

# Displaying the correlation matrix
import ace_tools as tools
tools.display_dataframe_to_user(name="Correlation Matrix", dataframe=correlation_matrix)
Always show details

Copy code

import seaborn as sns

# Compute the correlation matrix
correlation_matrix = df_cleaned.corr()

# Plot 1: Heatmap of the Correlation Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()

# Plot 2: Scatter plot of Total Sales vs Quantity (Strongest Correlation)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_cleaned['quantity'], y=df_cleaned['total_sales'], alpha=0.6)
plt.xlabel('Quantity Sold')
plt.ylabel('Total Sales')
plt.title('Total Sales vs Quantity Sold (Strongest Correlation)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Plot 3: Scatter plot of Unit Price vs Total Sales (Strong Correlation)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_cleaned['unit_price'], y=df_cleaned['total_sales'], alpha=0.6)
plt.xlabel('Unit Price')
plt.ylabel('Total Sales')
plt.title('Total Sales vs Unit Price')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Plot 4: Scatter plot of Base Price vs Unit Price (Strong Correlation)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_cleaned['base_price'], y=df_cleaned['unit_price'], alpha=0.6)
plt.xlabel('Base Price')
plt.ylabel('Unit Price')
plt.title('Base Price vs Unit Price')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()