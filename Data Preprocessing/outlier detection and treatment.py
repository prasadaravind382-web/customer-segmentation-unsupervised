Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['age'] >= lower) & (df['age'] <= upper)]

print("Dataset after removing outliers:", df.shape)
