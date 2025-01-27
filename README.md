# Financial Data Analysis for Bank Loans

## Overview

This project performs detailed analysis on financial data related to bank loans. The key objectives include exploring customer demographics, understanding customer behaviors, and identifying factors affecting personal loan approvals. The analysis is supplemented with descriptive statistics, data visualization, and hypothesis testing.

## Features

### 1. Data Exploration
- Reads and processes data from an Excel file.
- Drops irrelevant columns (`ID`, `ZIP Code`) for better analysis.
- Identifies and resolves issues like negative values in certain attributes (e.g., `Experience`).

### 2. Data Visualization
- Boxplots and histograms for understanding distributions and variability.
- Pie charts for demographic analysis.
- Correlation heatmaps for exploring relationships between variables.
- Count plots to analyze behaviors by key attributes.

### 3. Customer Behavior Analysis
- Examines behavior across education levels, income, and personal loan status.
- Identifies the impact of factors like securities accounts, online banking, and credit card usage.

### 4. Hypothesis Testing
- Tests hypotheses to understand the impact of attributes like age, income, and family size on personal loan approvals.

## Requirements

The following Python libraries are required to run the project:

```bash
pandas
numpy
matplotlib
seaborn
scipy
plotly
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/anakail20/financial-data-analysis-for-bank-loans
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the file path in the script to point to the Excel file containing the data.

4. Run the script:
   ```bash
   python PythonScript.py
   ```

## Workflow

1. **Data Cleaning**:
   - Fixes negative values in the `Experience` column using mean values for corresponding age groups.
   - Removes irrelevant columns to focus on significant attributes.

2. **Exploratory Data Analysis (EDA)**:
   - Analyzes distributions and relationships between variables.
   - Highlights key insights through visualizations.

3. **Customer Segmentation**:
   - Groups customers by education and account-holding categories.
   - Explores behaviors such as income levels and loan status.

4. **Hypothesis Testing**:
   - Assesses whether attributes like age, income, or family size impact personal loan approvals.

## Key Insights

- **Distributions**:
  - `Age` and `Experience` are nearly uniformly distributed.
  - Income is right-skewed, with higher-income groups more likely to take personal loans.
- **Education Levels**:
  - Undergraduates form the largest group, followed by advanced professionals.
- **Customer Segments**:
  - Customers with securities accounts or certificates of deposit are more likely to take loans.
- **Hypothesis Testing**:
  - Age and income significantly impact personal loan approvals.

## Visualizations

- **Pie Charts**:
  - Distribution of customers by education levels.
  - Account-holding categories.
- **Boxplots**:
  - Five-point summary of numerical attributes.
- **Heatmaps**:
  - Correlation matrix for all attributes.
- **Count Plots**:
  - Behavioral analysis by customer segments.

## Future Enhancements

- Incorporate machine learning models to predict loan approvals.
- Include interactive dashboards for real-time data analysis.
- Expand hypothesis testing to additional variables.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **Libraries**: Thanks to the developers of `pandas`, `seaborn`, and `scipy` for their amazing tools.
- **Data**: Sample data provided in the project repository.

---

Feel free to contribute to this repository by submitting issues or pull requests.
