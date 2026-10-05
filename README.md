# ApexPlanet Data Analytics Internship — Task 4
## Data Storytelling, Business Intelligence & Statistical Validation

### 📌 Project Overview

This project was completed as part of the **ApexPlanet Data Analytics Internship — Task 4: Data Storytelling**.

The objective of this task was to transform the findings from previous data analysis tasks into a coherent business story, validate an important business hypothesis statistically, and present actionable recommendations for stakeholders.

The analysis combines:

- Exploratory Data Analysis
- Business Intelligence
- Customer Segmentation
- Category & Product Analysis
- Geographic Analysis
- Monthly Sales Analysis
- Statistical Hypothesis Testing
- Business Recommendations

---

## 🎯 Business Objective

The primary objective was to understand:

- How the business is performing overall
- Which customer segments contribute most to revenue
- Which categories and products drive sales
- How sales vary across cities
- How sales change over time
- Whether an observed difference in transaction value is statistically significant
- What actions can be recommended to stakeholders

---

## 📊 Dataset Overview

The final cleaned dataset contains:

| Metric | Value |
|---|---:|
| Records | 1,000 |
| Columns | 12 |
| Unique Customers | 947 |
| Unique Order IDs | 992 |
| Total Sales | ~₹139.4M |
| Total Quantity Sold | 5,435 |
| Average Order Value | ₹140,523.63 |
| Missing Values | 0 |
| Complete Duplicate Rows | 0 |
| Analysis Period | Jan 2025 – Jan 2026 |

> **Note:** January 2026 contains partial-period data and was therefore excluded from direct complete-month comparisons.

---

## 🔍 Key Business Findings

### 1. Customer Value Concentration

Revenue is strongly concentrated among High Value customers.

- High Value customers: ~25% of customers
- Contribution to total sales: ~55%
- Medium Value customers: ~50% of customers
- Contribution to total sales: ~41%
- Low Value customers: ~25% of customers
- Contribution to total sales: ~4%

This indicates that customer retention and relationship management are especially important for High Value customers.

---

### 2. Category Performance

**Electronics** was the leading revenue-generating category.

- Sales: approximately **₹50.78M**
- Share of total sales: approximately **36.43%**

Education was the second-largest category.

---

### 3. Product Performance

The leading products by sales were:

| Product | Approx. Sales |
|---|---:|
| Laptop | ₹25.44M |
| Mobile | ₹25.34M |
| Book | ₹25.03M |
| Rice | ₹22.23M |
| Chair | ₹21.52M |
| Shoes | ₹19.84M |

Laptop and Mobile were the strongest products by total sales.

---

### 4. Geographic Performance

- **Patna** recorded the highest total sales at approximately **₹19.29M**.
- **Bengaluru** recorded the highest sales per customer at approximately **₹156,446**.
- Kolkata and Bengaluru were also among the strongest-performing cities.

These geographic differences can support targeted growth and sales planning.

---

### 5. Monthly Sales Performance

Among complete months:

- **March 2025:** Highest sales — approximately ₹13.06M
- **September 2025:** Lowest sales — approximately ₹9.18M

January 2026 was treated as a partial period and was not directly compared with complete months.

---

# 🧪 Hypothesis Testing

### Business Question

> Do Electronics transactions have a significantly different average transaction sales value compared with Non-Electronics transactions?

### Hypotheses

**H₀ (Null Hypothesis):**  
There is no significant difference in mean transaction sales between Electronics and Non-Electronics.

**H₁ (Alternative Hypothesis):**  
A significant difference exists.

### Statistical Test

**Welch's Independent Two-Sample t-Test**

- Significance level (α): **0.05**
- Electronics transactions: **354**
- Non-Electronics transactions: **646**
- Electronics mean: **₹143,442.32**
- Non-Electronics mean: **₹137,183.99**
- Mean difference: **₹6,258.33**
- t-statistic: **0.8179**
- p-value: **0.413674**
- 95% Confidence Interval: **−₹8,764.16 to ₹21,280.82**
- Cohen's d: **0.0548**
- Effect Size: **Negligible**
- Decision: **Fail to Reject H₀**

### Statistical Interpretation

Electronics transactions have a higher observed average transaction sales value than Non-Electronics transactions. However, the difference is **not statistically significant at the 5% significance level**.

Therefore, the analysis does not provide sufficient statistical evidence to conclude that the population mean transaction sales values are different.

This demonstrates the importance of combining descriptive business metrics with statistical validation.

---

# 💡 Key Business Insights

1. Revenue is strongly concentrated among High Value customers.
2. Electronics is the largest revenue-generating category.
3. Laptop and Mobile are the leading products.
4. Sales performance varies across cities and months.
5. Electronics does not show a statistically significant difference in average transaction sales compared with Non-Electronics.

---

# 🚀 Business Recommendations

### 1. Prioritise High Value Customer Retention
Develop retention and relationship strategies for customers responsible for the largest share of revenue.

### 2. Maintain Electronics Strength
Continue monitoring inventory, pricing and availability within the Electronics category.

### 3. Monitor Laptop and Mobile
Track demand and performance of the two leading products closely.

### 4. Use Geographic Insights
Use both total sales and sales-per-customer metrics to identify city-level growth opportunities.

### 5. Monitor Monthly Trends
Use monthly sales patterns to support sales planning and inventory decisions.

### 6. Combine Descriptive and Statistical Evidence
Use statistical validation alongside business metrics before making important decisions based on observed differences.

---

# 📈 Project Deliverables

| File | Description |
|---|---|
| `Key_Findings.md` | Consolidated business findings and recommendations |
| `Hypothesis_Testing.py` | Statistical hypothesis testing script |
| `Hypothesis_Testing_Summary.xlsx` | Statistical summary |
| `Statistical_Test_Results.txt` | Statistical test results |
| `01_Customer_Segment_Sales.png` | Customer segment analysis |
| `02_Category_Sales.png` | Category performance |
| `03_Product_Sales.png` | Product performance |
| `04_City_Sales.png` | Geographic performance |
| `05_Monthly_Sales_Trend.png` | Monthly sales trend |
| `06_Electronics_vs_NonElectronics.png` | Hypothesis testing visualization |
| `ApexPlanet_Task4_Data_Storytelling.pptx` | Final stakeholder presentation |
| `ApexPlanet_Task4_Final_Report.pdf` | Final business report |
| `ApexPlanet_Cleaned_Dataset.csv` | Cleaned analytical dataset |

---

# 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Statistical Analysis
- Excel
- Data Visualization
- Business Intelligence
- GitHub
- PowerPoint
- NotebookLM

---

# 🎯 Conclusion

The analysis demonstrates strong overall sales performance with significant revenue concentration among High Value customers.

Electronics emerged as the leading revenue-generating category, while Laptop and Mobile were the strongest products. Geographic and monthly patterns provide additional opportunities for targeted business planning.

However, statistical validation showed that the higher observed average transaction sales value of Electronics compared with Non-Electronics was **not statistically significant**.

The final business direction is therefore to focus on customer retention, maintain strong-performing categories and products, identify geographic opportunities, monitor sales trends, and combine descriptive analytics with statistical evidence when making business decisions.

---

## 📌 Internship

**ApexPlanet Data Analytics Internship**  
**Task 4 — Data Storytelling**

Project focus: **Business Intelligence, Statistical Validation & Stakeholder Communication**
