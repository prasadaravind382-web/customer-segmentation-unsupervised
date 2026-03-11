df['armed'].fillna("Unknown", inplace=True)
df['flee'].fillna("Unknown", inplace=True)
df['race'].fillna("Unknown", inplace=True)

# Fill age with median
df['age'].fillna(df['age'].median(), inplace=True)

print(df.isnull().sum())
