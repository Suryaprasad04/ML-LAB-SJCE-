def knn_on_dummy_fruit():
    # Create dummy fruit data
    data = {
        'weight': [150, 180, 120, 160, 200, 170, 130],
        'color_score': [0.8, 0.7, 0.6, 0.9, 0.85, 0.88, 0.65],
        'fruit_type': [1, 1, 2, 1, 3, 3, 2]  # 1=Apple, 2=Orange, 3=Banana
    }
    df = pd.DataFrame(data)

    X = df[['weight', 'color_score']]
    y = df['fruit_type']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Fruit Dataset Accuracy:", accuracy_score(y_test, predictions))

knn_on_dummy_fruit()
