from google.colab import files 
dataupload = files.upload()
import pandas as pd
import plotly.express as px
df  = pd.read_csv("data106.csv")
fig = px.scatter(df, x= "student_id", y= "level", color = "attempt" , size = "attempt")
fig.show()
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(mean)
