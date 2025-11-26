# 🛡️ Cybersecurity Awareness Impact Analysis

### **Using Chi-Square Test to Evaluate Phishing Click Behavior**


## 📌 **Project Overview**

This mini-project analyzes whether cybersecurity awareness training helps reduce phishing email clicks. A chi-square statistical test is used to determine if there is a significant relationship between:

* **Training Status** (Completed vs Not Completed)
* **Phishing Simulation Result** (Clicked vs Not Clicked)

This reflects a real-world cybersecurity scenario used by security teams to measure human risk.

---

## 🎯 **Objective**

Determine:

### ❓ “Does cybersecurity awareness training significantly reduce phishing clicks?”

If YES → the organization should continue or expand training.
If NO → training programs need improvement.

---

## 📁 **Dataset Description**

A realistic dataset of **350 employees** across multiple departments:

* IT
* HR
* Finance
* Sales

For each employee group, we recorded:

* Whether they **completed training**
* Whether they **clicked** a phishing simulation email

The final aggregated dataset:

| Training Status | Clicked | Not Clicked | Total |
| --------------- | ------- | ----------- | ----- |
| Trained         | 32      | 168         | 200   |
| Not Trained     | 80      | 70          | 150   |
| **Total**       | 112     | 238         | 350   |

---

## 🧪 **Statistical Test Used: Chi-Square Test**

Chi-Square helps answer:

### 👉 Are the differences between trained and untrained users real or random?

### Hypotheses:

* **H₀ (Null):** Training has no effect on phishing clicks
* **H₁ (Alt):** Training affects phishing clicks

---

## 📊 **Results**

* **Chi-Square Statistic:** > 53
* **P-Value:** < 0.000001
* **Degrees of Freedom:** 1

### ✔ **Conclusion**

There is a **very strong association** between training and phishing behavior.

### 🟢 Training works.

Employees who completed awareness training clicked far fewer phishing emails.

---

## 📉 **Visualization**

A heatmap is used to visually compare click behavior between trained and untrained groups.

---

## 🧠 **Skills Demonstrated**

* Chi-Square hypothesis testing
* Contingency table creation
* Real-world cybersecurity application
* Python data analysis
* Data interpretation for business decisions
* Basic visualization for reporting

---

## 🚀 **Why This Project Matters**

Cybersecurity teams need to **measure human risk** to prevent attacks like:

* Business Email Compromise
* Phishing
* Ransomware
* Credential Theft

This project shows how data and statistics help organizations:

* improve training
* reduce risk
* educate employees
* protect business assets

---

**Author: Varrun Vashisht**
