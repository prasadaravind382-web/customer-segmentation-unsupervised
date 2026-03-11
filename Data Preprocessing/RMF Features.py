df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y')

snapshot_date = df['date'].max() + pd.Timedelta(days=1)

rfm = df.groupby('state').agg({
    'date': lambda x: (snapshot_date - x.max()).days,
    'id': 'count',
    'age': 'mean'
})

rfm.columns = ['Recency','Frequency','Monetary']

print(rfm.head())
