import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("zomato_dataset.csv")

# Basic cleaning
df = df.dropna(subset=['rate', 'approx_cost(for two people)'])

# Convert rating
df['rate'] = df['rate'].str.replace('/5','')
df['rate'] = df['rate'].astype(float)

# Convert cost
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str).str.replace(',','').astype(float)
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(float)

# -----------------------------
# 1. Top Cuisines
# -----------------------------
top_cuisines = df['cuisines'].value_counts().head(5)

plt.figure(figsize=(8,5))
top_cuisines.plot(kind='bar')
plt.title("Top 5 Cuisines")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_cuisines.png")
plt.show()

# -----------------------------
# 2. Rating Distribution
# -----------------------------
plt.figure(figsize=(8,5))
df['rate'].hist(bins=20)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("rating_distribution.png")
plt.show()

# -----------------------------
# 3. Price vs Rating
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df['approx_cost(for two people)'], df['rate'])
plt.xlabel("Cost for Two")
plt.ylabel("Rating")
plt.title("Price vs Rating")
plt.savefig("price_vs_rating.png")
plt.show()

# -----------------------------
# 4. Best Value Restaurants
# -----------------------------
best = df[(df['rate'] > 4.2) & (df['approx_cost(for two people)'] < 800)]
print(best[['name','rate','approx_cost(for two people)']])
