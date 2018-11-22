import numpy as np
import pandas as pd

# Machine learning algorithm
from sklearn.ensemble import RandomForestClassifier
# Import function
from sklearn.model_selection import train_test_split
# Used to write model to file
from sklearn.externals import joblib


# Disable Pandas alerts
pd.options.mode.chained_assignment = None

data = pd.read_csv("titanic_train.csv")
# print(data.head())

median_age = data['age'].median()
# print("Median age is {}".format(median_age))

data['age'].fillna(median_age, inplace=True)

data_inputs = data[["pclass", "age", "sex"]]
# print(data_inputs.head())

expected_output = data[["survived"]]
# print(expected_output.head())

data_inputs["pclass"].replace("3rd", 3, inplace=True)
data_inputs["pclass"].replace("2nd", 2, inplace=True)
data_inputs["pclass"].replace("1st", 1, inplace=True)

data_inputs["sex"] = np.where(data_inputs["sex"] == "female", 0, 1)
# print(data_inputs.head())

inputs_train, inputs_test, expected_output_train, expected_output_test = train_test_split(
    data_inputs, expected_output, test_size=0.33, random_state=42
)

# print(inputs_train.head())
# print(expected_output_train.head())

rf = RandomForestClassifier(n_estimators=100)
rf.fit(inputs_train, expected_output_train)

accuracy = rf.score(inputs_test, expected_output_test)
print("Accuracy = {}".format(accuracy * 100))

# joblib.dump(rf, "titanic_model1", compress=9)
#
# rf = joblib.load("titanic_model2")
# pred = rf.predict(data)

