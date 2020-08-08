# Sklearn Reference

| Method                                                                                   | Description                                                |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| model = linear_model.LinearRegression()                                                  | linear regression                                          |
| results = model.fit(X, y)                                                                | fit a model                                                |
| results.intercept_, results.coef_                                                        | y intercept and coefficients for Linear Regression model   |
| tree.DecisionTreeClassifier()                                                            | classification decision tree                               |
| tree.plot_tree(clf)                                                                      | plots the tree                                             |
| graphviz.Source(tree.export_graphviz(clf, out_file=None)).render("iris")                 | Render and save the tree as PDF using graphviz             |
| X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) | split the dataset into train-test                          |
| metrics.mean_absolute_error(y_test, y_pred)                                              | Mean absolute error                                        |
| metrics.mean_squared_error(y_test, y_pred)                                               | Mean squared error                                         |
| np.sqrt(metrics.mean_squared_error(y_test, y_pred))                                      | Root mean squared error                                    |
| explained_variance_score(y_test, y_pred, multioutput='uniform_average')                  | explained variance score                                   |
| KNeighborsClassifier(k, weights=weights)                                                 | K-nearest neighbors                                        |
| r2_score(df_japan['mpg'], f(df_japan['weight']))                                         | R-squared (regression score function)                      |
| model = linear_model.LinearRegression()                                                  | Basic Linear Regression model                              |
| PCA(), pca.explained_variance_ratio_                                                     | Principal Component Analysis and explained variance ratios |
| DecisionTreeRegressor                                                                    | Decision Tree Regressor                                    |
| DecisionTreeClassifier                                                                   | Decision Tree Classifier                                   |
| tree_clf.score(X_test, y_test)                                                           | Score for a classifier                                     |
| sklearn.neural_network.MLPClassifier                                                     | Multi Level Perceptron (neural net)                        |
| sklearn.neighbors.KNeighborsClassifier                                                   | K-nearest neighbors classifier (supervised)                |


```python
# Outlier removal techniques
ort = IsolationForest(contamination=0.1)
ort = EllipticEnvelope(contamination=0.01)
ort = LocalOutlierFactor()
ort = OneClassSVM()
yhat = ort.fit_predict(X_train)
X_train = X_train[yhat!=-1].reset_index(drop=True)
y_train = y_train[yhat!=-1].reset_index(drop=True)
```
