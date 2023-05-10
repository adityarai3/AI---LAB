from sklearn.metrics import accuracy_score

# Define the ground truth labels and predicted labels
y_true = [0, 1, 0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 1, 0, 1, 1, 0]

# Calculate the accuracy
accuracy = accuracy_score(y_true, y_pred)

print("Accuracy: {:.2f}".format(accuracy))
