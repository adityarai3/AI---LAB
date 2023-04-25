from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import BayesianRidge
dataset = load_boston()
X, y = dataset.data, dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15, random_state = 42)
model = BayesianRidge()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
print(f"r2 Score Of Test Set : {r2_score(y_test, prediction)}")
