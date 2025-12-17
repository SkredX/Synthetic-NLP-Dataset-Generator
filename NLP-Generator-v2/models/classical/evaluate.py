from sklearn.metrics import accuracy_score, classification_report

def evaluate(model, X_test_vec, y_test):
    preds = model.predict(X_test_vec)

    print("Accuracy:", accuracy_score(y_test, preds))
    print()
    print(classification_report(y_test, preds))

    return preds
