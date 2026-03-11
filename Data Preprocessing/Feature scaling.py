scaler = MinMaxScaler()

df[['age']] = scaler.fit_transform(df[['age']])

print(df[['age']].head())
