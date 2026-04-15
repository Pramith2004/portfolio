import pandas as pd

# Sample dataset (you can replace with CSV file)
data = {
    "Name": ["Alice", "Bob", "alice", "Charlie", None],
    "Age": [25, None, 25, 30, 22],
    "City": ["New York", "Los Angeles", "new york", None, "Chicago"]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)

# 1. Handle Missing Values
# Fill missing Age with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing Name and City with 'Unknown'
df["Name"].fillna("Unknown", inplace=True)
df["City"].fillna("Unknown", inplace=True)

# 2. Remove Duplicates
df.drop_duplicates(inplace=True)

# 3. Standardize Text
# Convert to lowercase and strip spaces
df["Name"] = df["Name"].str.lower().str.strip()
df["City"] = df["City"].str.lower().str.strip()

# Optional: Capitalize properly
df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()

print("\nCleaned Data:\n")
print(df)