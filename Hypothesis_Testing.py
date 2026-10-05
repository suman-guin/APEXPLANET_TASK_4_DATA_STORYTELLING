# ==============================================================
# APEXPLANET DATA ANALYTICS INTERNSHIP
# TASK 4 — HYPOTHESIS TESTING
# ==============================================================

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import t


# ==============================================================
# 1. LOAD DATASET
# ==============================================================

file_path = (
    r"D:\APEXPLANET_TASK_4_DATA_STORYTELLING"
    r"\07_Dataset\ApexPlanet_Cleaned_Dataset.csv"
)

df = pd.read_csv(file_path)

print("=" * 70)
print("APEXPLANET TASK 4 — HYPOTHESIS TESTING")
print("=" * 70)

print("\nDataset Shape:")
print(df.shape)


# ==============================================================
# 2. DATA VALIDATION
# ==============================================================

print("\n" + "-" * 70)
print("DATA VALIDATION")
print("-" * 70)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nComplete Duplicate Rows:")
print(df.duplicated().sum())


# Ensure Total_Sales is numeric
df["Total_Sales"] = pd.to_numeric(
    df["Total_Sales"],
    errors="coerce"
)

# Remove rows where required values are missing
df = df.dropna(
    subset=["Category", "Total_Sales"]
)

print("\nRows After Validation:")
print(len(df))


# ==============================================================
# 3. BUSINESS HYPOTHESIS
# ==============================================================

print("\n" + "-" * 70)
print("BUSINESS HYPOTHESIS")
print("-" * 70)

print("""
Business Question:

Do Electronics transactions have a significantly different
average transaction sales value compared with Non-Electronics
transactions?


Null Hypothesis (H0):

There is no significant difference in the mean transaction
sales between Electronics and Non-Electronics transactions.


Alternative Hypothesis (H1):

There is a significant difference in the mean transaction
sales between Electronics and Non-Electronics transactions.


Statistical Test:

Welch's Independent Two-Sample t-test


Significance Level:

alpha = 0.05
""")


# ==============================================================
# 4. CREATE TWO GROUPS
# ==============================================================

electronics = df[
    df["Category"] == "Electronics"
]["Total_Sales"]

non_electronics = df[
    df["Category"] != "Electronics"
]["Total_Sales"]


print("-" * 70)
print("GROUP INFORMATION")
print("-" * 70)

print(
    "\nElectronics Transactions:",
    len(electronics)
)

print(
    "Non-Electronics Transactions:",
    len(non_electronics)
)


# ==============================================================
# 5. DESCRIPTIVE STATISTICS
# ==============================================================

mean_electronics = electronics.mean()
median_electronics = electronics.median()
std_electronics = electronics.std()

mean_non_electronics = non_electronics.mean()
median_non_electronics = non_electronics.median()
std_non_electronics = non_electronics.std()


print("\n" + "-" * 70)
print("DESCRIPTIVE STATISTICS")
print("-" * 70)

print("\nElectronics:")
print(f"Mean: ₹{mean_electronics:,.2f}")
print(f"Median: ₹{median_electronics:,.2f}")
print(f"Standard Deviation: ₹{std_electronics:,.2f}")

print("\nNon-Electronics:")
print(f"Mean: ₹{mean_non_electronics:,.2f}")
print(f"Median: ₹{median_non_electronics:,.2f}")
print(f"Standard Deviation: ₹{std_non_electronics:,.2f}")


# ==============================================================
# 6. WELCH'S INDEPENDENT TWO-SAMPLE T-TEST
# ==============================================================

t_statistic, p_value = stats.ttest_ind(
    electronics,
    non_electronics,
    equal_var=False
)


print("\n" + "-" * 70)
print("WELCH'S T-TEST RESULT")
print("-" * 70)

print(f"\nT-Statistic: {t_statistic:.4f}")
print(f"P-Value: {p_value:.6f}")


# ==============================================================
# 7. HYPOTHESIS DECISION
# ==============================================================

alpha = 0.05

if p_value < alpha:

    decision = "Reject H0"

    conclusion = (
        "There is a statistically significant difference "
        "in mean transaction sales between Electronics and "
        "Non-Electronics transactions."
    )

else:

    decision = "Fail to Reject H0"

    conclusion = (
        "There is not enough statistical evidence to conclude "
        "that mean transaction sales differ between Electronics "
        "and Non-Electronics transactions."
    )


print("\n" + "-" * 70)
print("HYPOTHESIS DECISION")
print("-" * 70)

print(f"\nDecision: {decision}")
print(f"Conclusion: {conclusion}")


# ==============================================================
# 8. MEAN DIFFERENCE
# ==============================================================

mean_difference = (
    mean_electronics -
    mean_non_electronics
)

print("\n" + "-" * 70)
print("MEAN DIFFERENCE")
print("-" * 70)

print(
    f"\nElectronics Mean: ₹{mean_electronics:,.2f}"
)

print(
    f"Non-Electronics Mean: ₹{mean_non_electronics:,.2f}"
)

print(
    f"Mean Difference: ₹{mean_difference:,.2f}"
)


# ==============================================================
# 9. 95% CONFIDENCE INTERVAL
# ==============================================================

n1 = len(electronics)
n2 = len(non_electronics)

var1 = electronics.var()
var2 = non_electronics.var()


# Welch-Satterthwaite degrees of freedom

df_welch = (
    (var1 / n1 + var2 / n2) ** 2
    /
    (
        ((var1 / n1) ** 2 / (n1 - 1))
        +
        ((var2 / n2) ** 2 / (n2 - 1))
    )
)


# Standard Error

standard_error = np.sqrt(
    (var1 / n1) +
    (var2 / n2)
)


# Critical value for 95% CI

critical_value = t.ppf(
    0.975,
    df_welch
)


# Margin of Error

margin_of_error = (
    critical_value *
    standard_error
)


# Confidence Interval

ci_lower = (
    mean_difference -
    margin_of_error
)

ci_upper = (
    mean_difference +
    margin_of_error
)


print("\n" + "-" * 70)
print("95% CONFIDENCE INTERVAL")
print("-" * 70)

print(
    f"\nWelch Degrees of Freedom: "
    f"{df_welch:.2f}"
)

print(
    f"Mean Difference: "
    f"₹{mean_difference:,.2f}"
)

print(
    f"95% CI Lower Bound: "
    f"₹{ci_lower:,.2f}"
)

print(
    f"95% CI Upper Bound: "
    f"₹{ci_upper:,.2f}"
)


# ==============================================================
# 10. EFFECT SIZE — COHEN'S d
# ==============================================================

pooled_std = np.sqrt(
    (
        ((n1 - 1) * var1)
        +
        ((n2 - 1) * var2)
    )
    /
    (n1 + n2 - 2)
)


cohens_d = (
    mean_difference /
    pooled_std
)


# Effect Size Interpretation

if abs(cohens_d) < 0.2:

    effect_interpretation = "Negligible effect"

elif abs(cohens_d) < 0.5:

    effect_interpretation = "Small effect"

elif abs(cohens_d) < 0.8:

    effect_interpretation = "Medium effect"

else:

    effect_interpretation = "Large effect"


print("\n" + "-" * 70)
print("EFFECT SIZE")
print("-" * 70)

print(
    f"\nCohen's d: {cohens_d:.4f}"
)

print(
    f"Interpretation: "
    f"{effect_interpretation}"
)


# ==============================================================
# 11. FINAL STATISTICAL INTERPRETATION
# ==============================================================

print("\n" + "=" * 70)
print("FINAL STATISTICAL INTERPRETATION")
print("=" * 70)

if p_value < alpha:

    print("""
The Welch's t-test indicates a statistically significant
difference in mean transaction sales between Electronics
and Non-Electronics transactions.
""")

else:

    print("""
The Welch's t-test indicates that there is no statistically
significant difference in mean transaction sales between
Electronics and Non-Electronics transactions.

Although Electronics transactions have a higher average
sales value, the observed difference is not statistically
significant at the 5% significance level.
""")


print(f"Electronics Mean: ₹{mean_electronics:,.2f}")
print(f"Non-Electronics Mean: ₹{mean_non_electronics:,.2f}")
print(f"Mean Difference: ₹{mean_difference:,.2f}")

print(
    f"95% Confidence Interval: "
    f"₹{ci_lower:,.2f} to ₹{ci_upper:,.2f}"
)

print(
    f"Cohen's d: {cohens_d:.4f}"
)

print(
    f"Effect Size: "
    f"{effect_interpretation}"
)

print(
    f"T-Statistic: "
    f"{t_statistic:.4f}"
)

print(
    f"P-Value: "
    f"{p_value:.6f}"
)

print(
    f"Decision: "
    f"{decision}"
)

print("=" * 70)
print("HYPOTHESIS TESTING COMPLETED")
print("=" * 70)