# model/train.py
from os import PathLike  
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd
import pathlib
import json, pathlib

df = pd.read_csv(pathlib.Path('data/teen_phone_addiction_dataset.csv'))


UMBRAL = 9.5
y = (df['Addiction_Level'] >= UMBRAL).astype(int)

cols_drop = [c for c in ['ID', 'Name', 'Addiction_Level'] if c in df.columns]
X = df.drop(columns=cols_drop)

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('Training model.. ')
clf = RandomForestClassifier(n_estimators=200, max_depth=None, random_state=0)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=0))

pathlib.Path('model').mkdir(parents=True, exist_ok=True)
with open('model/teen-addiction-features.json', 'w') as f:
    json.dump(list(X.columns), f)

print('Saving model..')
pathlib.Path('model').mkdir(parents=True, exist_ok=True)
dump(clf, pathlib.Path('model/teen-addiction-v1.joblib'))
