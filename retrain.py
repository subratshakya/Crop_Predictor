import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pickle

# Load your dataset
data = pd.read_csv('your_dataset.csv')

# Define your features (X) and target (y)
X = data.drop('target', axis=1)
y = data['target']

# Train your models
dt_model = DecisionTreeClassifier()
rf_model = RandomForestClassifier()

dt_model.fit(X, y)
rf_model.fit(X, y)

# Fit your scalers
sc = StandardScaler()
mx = MinMaxScaler()

sc.fit(X)
mx.fit(X)

# Save the models and scalers
with open('model.pkl', 'wb') as model_file:
    pickle.dump(rf_model, model_file)

with open('standscaler.pkl', 'wb') as sc_file:
    pickle.dump(sc, sc_file)

with open('minmaxscaler.pkl', 'wb') as mx_file:
    pickle.dump(mx, mx_file)

print("Models and scalers saved successfully.")
