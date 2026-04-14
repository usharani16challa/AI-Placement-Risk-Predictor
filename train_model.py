import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Dummy dataset
data = {
    'cgpa': [7,8,6,9,5,7.5,8.5],
    'internship': [1,1,0,1,0,1,1],
    'college_tier': [2,1,3,1,3,2,1],
    'placement': [1,1,0,1,0,1,1]
}

df = pd.DataFrame(data)

X = df[['cgpa','internship','college_tier']]
y = df['placement']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open('model.pkl','wb'))

print("Model trained and saved!")