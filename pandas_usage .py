import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("exam_scores.csv")



#BAR CHART #Vertical

plt.figure(figsize=(10, 5,), num="Vertical Bar Chart")
plt.bar(df["Student"], df["Midterm Exam"], color="red")
plt.xlabel("Student Names")
plt.ylabel("Student Scores")
plt.title("Student Exam Score")
plt.show()


#Horizontal Bar


plt.figure(figsize=(10, 5), num="Horizontal Bar Chart")
plt.barh(df["Student"], df["Midterm Exam"], color="red",)
plt.xlabel("Student Names")
plt.ylabel("Student Scores")
plt.title("Student Exam Score")
plt.show()

#Line graph

plt.figure(figsize=(10, 5), num="Line Graph")
plt.plot(df["Student"], df["Midterm Exam"], marker="o")
plt.xlabel("Student Names")
plt.ylabel("Student Scores")
plt.title("Student Exam Score")
plt.show()


































# 1. show the dataframe entirely
# print(df)

# 2. See the top 5
# print(df.head())

# 3. Basic stats- min/max/avg
# print(df.describe())

# #4. Grab names only
# print(df["Student"])

# 5. Grab only scores

# print(df["Final Exam"])

# print(df["Final Exam"].mean())
# print(df["Final Exam"].min())
# print(df["Final Exam"].max())


# 6. Grab Students Who got above 80

print(df[df["Final Exam"]>80])

# print(df[df["Final Exam"]==100])