print("Top Armed Types")
print(df['armed'].value_counts().head())

print("\nAverage Age by Race")
print(df.groupby('race')['age'].mean())
