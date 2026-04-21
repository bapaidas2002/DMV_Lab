import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("company_dataset.csv")

# -----------------------------
# DATA CLEANING
# -----------------------------

# Clean review count
df['review_count_clean'] = df['review_count'].str.replace(r'[^\d.]', '', regex=True)
df['review_count_clean'] = df['review_count_clean'].astype(float)

# Convert years column
df['years_clean'] = df['years'].str.extract(r'(\d+)').astype(int)

# Clean employees column
df['employees_clean'] = df['employees'].fillna("Unknown")

# -----------------------------
# 1. PIE CHART (Employees Wise)
# -----------------------------
emp_counts = df['employees_clean'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(emp_counts, labels=emp_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart: Company Distribution by Employee Size")
plt.show()

# -----------------------------
# 2. FUNNEL CHART (Matplotlib Style)
# -----------------------------
df_top10 = df.sort_values(by='review_count_clean', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(df_top10['name'], df_top10['review_count_clean'], color='skyblue')

# Invert y-axis to mimic funnel (largest on top)
plt.gca().invert_yaxis()

plt.title("Funnel Chart (Top 10 Companies by Reviews)")
plt.xlabel("Review Count")
plt.ylabel("Company")
plt.show()

# -----------------------------
# 3. HEADQUARTERS (Top 10)
# -----------------------------
top10_hq = df[['name', 'hq']].head(10)

print("\nTop 10 Company Headquarters:\n")
print(top10_hq.to_string(index=False))

# -----------------------------
# 4. BAR CHART (Ratings Wise)
# -----------------------------
plt.figure(figsize=(12,6))
plt.bar(df['name'], df['ratings'], color='orange')
plt.xticks(rotation=90)
plt.title("Bar Chart: Company Ratings")
plt.xlabel("Company")
plt.ylabel("Rating")
plt.show()

# -----------------------------
# 5. LINE CHART (Years Wise)
# -----------------------------
df_sorted_years = df.sort_values(by='years_clean')

plt.figure(figsize=(12,6))
plt.plot(df_sorted_years['name'], df_sorted_years['years_clean'], marker='o', linestyle='-', color='green')
plt.xticks(rotation=90)
plt.title("Line Chart: Company Age (Years)")
plt.xlabel("Company")
plt.ylabel("Years")
plt.show()