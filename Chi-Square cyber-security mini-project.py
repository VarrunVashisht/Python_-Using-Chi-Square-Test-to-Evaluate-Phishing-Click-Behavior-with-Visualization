# Is there a relationship between cyber awareness training and how often employees click phishing emails?

'''
1. Realistic Cybersecurity Dataset

Training Completion (Yes / No)
Department (IT, HR, Finance, Sales)
Phishing Simulation Result (Clicked / Ignored)

Let's simulate a more realistic dataset that looks like:
| Department | Training Status | Clicked | Not Clicked | Total |
| ---------- | --------------- | ------- | ----------- | ----- |
| IT         | Trained         | 2       | 48          | 50    |
| IT         | Not Trained     | 5       | 25          | 30    |
| HR         | Trained         | 10      | 40          | 50    |
| HR         | Not Trained     | 20      | 20          | 40    |
| Finance    | Trained         | 8       | 42          | 50    |
| Finance    | Not Trained     | 25      | 15          | 40    |
| Sales      | Trained         | 12      | 38          | 50    |
| Sales      | Not Trained     | 30      | 10          | 40    |
Total employees = 350

2. Cleaned Dataset for Chi-Square Test
Combine the Clicked and Not Clicked across all departments:

| Training Status | Clicked | Not Clicked | Total |
| --------------- | ------- | ----------- | ----- |
| Trained         | 32      | 168         | 200   |
| Not Trained     | 80      | 70          | 150   |
| **Total**       | 112     | 238         | 350   |

This is now PERFECT for a chi-square test.
'''

import pandas as pd
from scipy.stats import chi2_contingency

# More realistic cybersecurity dataset
data = \
[
    [32, 168],   # Trained: Clicked, Not_Clicked
    [80, 70]     # Not Trained: Clicked, Not_Clicked
]

df = pd.DataFrame(data,
                  columns=["Clicked", "Not_Clicked"],
                  index=["Trained", "Not_Trained"])
print("Contingency Table:")
print(df)

# Run chi-square test
chi2, p, dof, expected = chi2_contingency(df)

print("\nChi-Square Value:", chi2)
print("P-Value:", p)
print("Degrees of Freedom:", dof)
print("\nExpected Values:\n", expected)

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df, annot=True, fmt="d", cmap="Reds")
plt.title("Phishing Clicks vs Training Status")
plt.show()
