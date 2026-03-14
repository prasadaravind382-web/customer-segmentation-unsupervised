# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Extract year and month
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Count incidents per year
year_counts = df.groupby('year').size()

print(year_counts)

# Plot yearly trend
year_counts.plot(kind='line', marker='o')
plt.title("Time-Based Segmentation (Incidents per Year)")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()
