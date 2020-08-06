# Sklearn Reference

| Method                                                                                   | Description                                              |
| ---------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| model = linear_model.LinearRegression()                                                  | linear regression                                        |
| results = model.fit(X, y)                                                                | fit a model                                              |
| results.intercept_, results.coef_                                                        | y intercept and coefficients for Linear Regression model |
| tree.DecisionTreeClassifier()                                                            | classification decision tree                             |
| tree.plot_tree(clf)                                                                      | plots the tree                                           |
| graphviz.Source(tree.export_graphviz(clf, out_file=None)).render("iris")                 | Render and save the tree as PDF using graphviz           |
| X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) | split the dataset into train-test                        |
| metrics.mean_absolute_error(y_test, y_pred)                                              | Mean absolute error                                      |
| metrics.mean_squared_error(y_test, y_pred)                                               | Mean squared error                                       |
| np.sqrt(metrics.mean_squared_error(y_test, y_pred))                                      | Root mean squared error                                  |
| explained_variance_score(y_test, y_pred, multioutput='uniform_average')                  | explained variance score                                 |