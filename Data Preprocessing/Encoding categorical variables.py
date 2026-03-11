encoder = LabelEncoder()

df['gender'] = encoder.fit_transform(df['gender'])
df['race'] = encoder.fit_transform(df['race'])
df['state'] = encoder.fit_transform(df['state'])

print(df[['gender','race','state']].head())
