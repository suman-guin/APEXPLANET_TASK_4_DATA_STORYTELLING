# APEXPLANET TASK 4 — DATA STORYTELLING

## 1. Business Objective

The objective of this analysis is to understand sales performance,
customer contribution, category performance, geographic variation,
and transaction-level behaviour using the cleaned sales dataset.

The analysis combines findings from data cleaning, exploratory
data analysis, business intelligence, and statistical validation
to identify actionable business insights.

---

## 2. Dataset Overview

- Total Records: 1,000
- Total Columns: 12
- Unique Customers: 947
- Unique Order IDs: 992
- Missing Values: 0
- Complete Duplicate Rows: 0
- Date Range: January 2025 to January 2026
- Total Sales: Approximately ₹139.4 Million
- Total Quantity Sold: 5,435

The dataset contains information about orders, customers,
products, categories, locations, quantities, prices, and sales.

---

# 3. Key Business Findings

## 3.1 Overall Sales Performance

The dataset generated approximately ₹139.4 Million in total sales
across 1,000 transaction records.

The average order value based on unique Order IDs was approximately
₹140,523.63.

This indicates a substantial sales volume across the analysed
period.

---

## 3.2 Customer Value Concentration

Customer-level analysis revealed a strong concentration of revenue
among high-value customers.

### Customer Segmentation

| Segment | Customers | % of Customers | Sales Contribution |
|--------|-----------|----------------|--------------------|
| High Value | 237 | 25.03% | 55.27% |
| Medium Value | 473 | 49.95% | 40.69% |
| Low Value | 237 | 25.03% | 4.04% |

The High Value customer segment represents approximately one-quarter
of customers but contributes more than half of total sales.

### Business Insight

High-value customers are strategically important because a relatively
small customer group generates a disproportionately large share of
revenue.

Customer retention and relationship-building strategies should
therefore prioritise this segment.

---

## 3.3 Category Performance

Electronics was the leading category by total sales.

### Category Highlight

- Electronics Sales: Approximately ₹50.78 Million
- Share of Total Sales: Approximately 36.43%

Education was the second-largest category by sales contribution.

### Business Insight

Electronics is the strongest revenue-generating category and should
remain an important focus area for product availability, pricing,
inventory planning, and customer targeting.

However, total category sales should not automatically be interpreted
as higher transaction-level performance.

---

## 3.4 Product Performance

The leading products by sales included:

1. Laptop — approximately ₹25.44 Million
2. Mobile — approximately ₹25.34 Million
3. Book — approximately ₹25.03 Million
4. Rice — approximately ₹22.23 Million
5. Chair — approximately ₹21.52 Million
6. Shoes — approximately ₹19.84 Million

### Business Insight

Laptop and Mobile were the strongest individual products by sales,
while the overall product portfolio showed relatively broad
contribution across multiple products.

---

## 3.5 Geographic Performance

Patna generated the highest total sales at approximately
₹19.29 Million.

Kolkata and Bengaluru were also among the strongest-performing
cities.

Bengaluru recorded the highest sales per customer at approximately
₹156,446.

### Business Insight

Geographic performance varies across cities.

Total sales and sales-per-customer provide different perspectives,
so both measures should be considered when identifying priority
markets.

---

## 3.6 Monthly Sales Trend

Among complete months, March 2025 recorded the highest monthly sales
at approximately ₹13.06 Million.

September 2025 recorded the lowest monthly sales among complete
months at approximately ₹9.18 Million.

January 2026 contains only partial-period data and should therefore
not be directly compared with complete months.

### Business Insight

Monthly sales show noticeable variation over time.

Future planning should consider seasonal or time-based patterns
when evaluating sales performance.

---

# 4. Statistical Validation

## Business Hypothesis

The statistical analysis tested whether Electronics transactions
have a significantly different average transaction sales value
compared with Non-Electronics transactions.

### Null Hypothesis (H0)

There is no significant difference in the mean transaction sales
between Electronics and Non-Electronics transactions.

### Alternative Hypothesis (H1)

There is a significant difference in the mean transaction sales
between Electronics and Non-Electronics transactions.

### Test Used

Welch's Independent Two-Sample t-test

### Significance Level

α = 0.05

---

## Statistical Results

| Metric | Result |
|--------|--------|
| Electronics Transactions | 354 |
| Non-Electronics Transactions | 646 |
| Electronics Mean | ₹143,442.32 |
| Non-Electronics Mean | ₹137,183.99 |
| Mean Difference | ₹6,258.33 |
| T-Statistic | 0.8179 |
| P-Value | 0.413674 |
| 95% Confidence Interval | ₹−8,764.16 to ₹21,280.82 |
| Cohen's d | 0.0548 |
| Effect Size | Negligible |
| Decision | Fail to Reject H0 |

---

## Statistical Interpretation

Electronics transactions had a higher observed average sales value
than Non-Electronics transactions by approximately ₹6,258.33.

However, the p-value of 0.413674 is greater than the significance
level of 0.05.

Therefore, there is not enough statistical evidence to conclude that
the mean transaction sales differ significantly between Electronics
and Non-Electronics transactions.

The 95% confidence interval includes zero, and the Cohen's d value
of 0.0548 indicates a negligible effect size.

---

# 5. Key Business Story

The analysis shows that the business generates substantial sales
across a diverse customer and product base.

A major finding is the concentration of revenue among High Value
customers, with approximately 25% of customers contributing more
than 55% of total sales.

Electronics is the largest revenue-generating category, contributing
approximately 36.43% of total sales.

However, statistical testing shows that Electronics transactions do
not have a statistically significant difference in average
transaction sales compared with Non-Electronics transactions.

This means that Electronics leads in overall revenue primarily as a
category contribution, but the analysis does not provide evidence
that individual Electronics transactions are inherently higher in
value.

---

# 6. Business Recommendations

## 1. Prioritise High-Value Customers

Develop customer retention strategies for High Value customers
because they contribute a disproportionately large share of revenue.

## 2. Maintain Electronics Category Strength

Continue monitoring Electronics inventory, pricing, product
availability, and customer demand because it is the largest
revenue-generating category.

## 3. Focus on Product-Level Performance

Give particular attention to high-performing products such as
Laptop and Mobile while monitoring the performance of the broader
product portfolio.

## 4. Use Geographic Insights

Prioritise strong-performing cities while investigating opportunities
in lower-performing markets.

Sales per customer should be considered alongside total sales when
evaluating geographic opportunities.

## 5. Use Data-Driven Category Decisions

Do not assume that Electronics transactions inherently have higher
transaction values.

Category decisions should consider multiple factors including
customer segment, product mix, quantity, pricing, and geography.

## 6. Monitor Monthly Trends

Use monthly sales trends to support future sales planning,
inventory decisions, and performance monitoring.

---

# 7. Conclusion

The combined analysis provides a clear view of sales performance,
customer concentration, product and category contribution,
geographic variation, and transaction-level behaviour.

The strongest business opportunity is customer retention among
High Value customers, while Electronics remains the leading
revenue-generating category.

At the same time, statistical validation demonstrates that the
observed difference in average transaction sales between Electronics
and Non-Electronics is not statistically significant.

Therefore, future business decisions should combine descriptive
business intelligence with statistical evidence rather than relying
on a single metric.

---

# 8. Call to Action

1. Strengthen retention strategies for High Value customers.
2. Monitor Electronics performance and product availability.
3. Track Laptop and Mobile performance closely.
4. Identify growth opportunities across cities.
5. Monitor monthly sales trends for planning.
6. Use statistical validation when making important category-level
   business decisions.