behavior = df.groupby('state').agg({
    'age':'mean',
    'body_camera':'mean'
})

behavior.columns = ['AvgAge','BodyCameraUsage']

print(behavior.head())
