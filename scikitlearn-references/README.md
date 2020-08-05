# Sklearn Reference

| Method                                                                   | Description                                              |
| ------------------------------------------------------------------------ | -------------------------------------------------------- |
| model = linear_model.LinearRegression()                                  | linear regression                                        |
| results = model.fit(X, y)                                                | fit a model                                              |
| results.intercept_, results.coef_                                        | y intercept and coefficients for Linear Regression model |
| tree.DecisionTreeClassifier()                                            | classification decision tree                             |
| tree.plot_tree(clf)                                                      | plots the tree                                           |
| graphviz.Source(tree.export_graphviz(clf, out_file=None)).render("iris") | Render and save the tree as PDF using graphviz           |