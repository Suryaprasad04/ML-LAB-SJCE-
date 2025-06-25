from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

def knn_on_dummy_glass():
    # Create dummy glass data
    data = {
        'RI': [1.52, 1.53, 1.54, 1.55, 1.56, 1.52, 1.58],
        'Na': [13.2, 13.1, 13.4, 13.0, 13.3, 13.5, 13.1],
        'Mg': [3.5, 3.4, 3.6, 3.2, 3.8, 3.3, 3.6],
        'Type': [1, 1, 2, 2, 3, 1, 3]  # Glass types as labels
    }
    df = pd.DataFrame(data)

    X = df[['RI', 'Na', 'Mg']]
    y = df['Type']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Glass Dataset Accuracy:", accuracy_score(y_test, predictions))

knn_on_dummy_glass()
