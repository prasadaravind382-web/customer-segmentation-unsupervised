df_encoded = df.copy()

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df_encoded['gender'] = le.fit_transform(df_encoded['gender'])
df_encoded['race'] = le.fit_transform(df_encoded['race'].astype(str))

corr = df_encoded[['age','gender','race']].corr()

plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
