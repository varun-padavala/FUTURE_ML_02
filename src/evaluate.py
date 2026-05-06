from sklearn.metrics import classification_report, accuracy_score

def evaluate(y_true, y_pred):
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("\nReport:\n", classification_report(y_true, y_pred))