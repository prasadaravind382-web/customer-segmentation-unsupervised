plt.figure()
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure()
sns.boxplot(x='gender', y='age', data=df)
plt.title("Age vs Gender")
plt.show()

plt.figure()
sns.boxplot(x='race', y='age', data=df)
plt.title("Race vs Age")
plt.show()

plt.figure()
sns.countplot(x='armed', hue='gender', data=df)
plt.title("Armed Status by Gender")
plt.show()

sns.pairplot(df[['age','gender','race']], hue='gender')
plt.show()
