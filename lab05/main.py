from dep import *
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv("IRIS.csv")

df['species'] = df['species'].astype('category').cat.codes

X0 = df[['sepal_length', 'sepal_width']].values
X1 = df[['sepal_length', 'petal_width']].values
X2 = df[['petal_length', 'sepal_width']].values
X3 = df[['petal_length', 'petal_width']].values
X4 = df[['sepal_width', 'petal_width']].values
X5 = df[['sepal_length', 'petal_length']].values
y = df['species'].values

feature_sets = [X0, X1, X2, X3, X4, X5]
feature_set_names = ['Sepal Length vs Sepal Width', 'Sepal Length vs Petal Width',
                     'Petal Length vs Sepal Width', 'Petal Length vs Petal Width',
                     'Sepal Width vs Petal Width', 'Sepal Length vs Petal Length']

# Iterate over the feature sets
for i, (X, name) in enumerate(zip(feature_sets, feature_set_names)):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    p = Perceptron(X.shape[1], 0.1)
    p.fit(X_train, y_train, 100)

    predictions = p.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    print(f"Perceptron classification accuracy for {name}: {accuracy * 100:.2f}%")

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.scatter(X_train[:, 0], X_train[:, 1], marker='o', c=y_train)

    x0_1 = np.amin(X_train[:, 0])
    x0_2 = np.amax(X_train[:, 0])

    x1_1 = (-p.weights[0] * x0_1 - p.bias) / p.weights[1]
    x1_2 = (-p.weights[0] * x0_2 - p.bias) / p.weights[1]

    ax.plot([x0_1, x0_2], [x1_1, x1_2], 'k')

    ymin = np.amin(X_train[:, 1])
    ymax = np.amax(X_train[:, 1])
    ax.set_ylim([ymin - 3, ymax + 3])

    ax.set_title(name)

plt.show()
