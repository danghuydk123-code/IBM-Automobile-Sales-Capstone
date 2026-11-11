"""Optional extension: classify recession status from economic indicators.
Run: python code/classification_analysis.py
The course dataset is synthetic; scores are educational.
"""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)
target = "Recession"
features = ["GDP", "unemployment_rate", "Consumer_Confidence", "Price",
            "Seasonality_Weight", "Advertising_Expenditure", "Competition"]
X, y = df[features], df[target].astype(int)

# Chronological split to reduce leakage between adjacent monthly observations.
order = pd.to_datetime(df["Date"]).sort_values().index
X, y = X.loc[order], y.loc[order]
cut = int(len(X) * 0.8)
X_train, X_test = X.iloc[:cut], X.iloc[cut:]
y_train, y_test = y.iloc[:cut], y.iloc[cut:]

prep = ColumnTransformer([("numeric", Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
]), features)])
models = {
    "Logistic Regression": LogisticRegression(max_iter=2000, class_weight="balanced"),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42, class_weight="balanced"),
    "Random Forest": RandomForestClassifier(n_estimators=300, random_state=42, class_weight="balanced")
}
for name, model in models.items():
    pipe = Pipeline([("prep", prep), ("model", model)])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    print("\\n" + name)
    print("Accuracy:", round(accuracy_score(y_test, pred), 4))
    print(classification_report(y_test, pred, zero_division=0))
    print("Confusion matrix:\\n", confusion_matrix(y_test, pred))
