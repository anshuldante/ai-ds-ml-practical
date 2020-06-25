# Machine Learning Algorithms

## Foundations

* ### Model vs Algorithm

  * An algorithm is a mathematical technique or equation i.e. a framework, the variables and everything is generic and there will be some work required to use the algorithm anywhere. E.g. y = mx + c.
  * In contrast, a model is an equation that is formed by using data to find parameters in the equation of an algorithm. E.g. y = 0.5x + 10.

## Logistic Regression

* ### What

  * Regression is a statistical process for estimating the relationship between variables, often used to predict something.
  * ![Linear Regression](images/linear_regression.png)
  * Logistic regression is a form of regression where the target variable is binary.
  * Linear regression cant work too well if the target variable can be only within 0 and 1.
  * ![Linear vs logistic regression for binary classification](images/linear_vs_logistic.png)

| When to use                                                           | When not to use                                                                  |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Binary target variable                                                | Continuous target variables                                                      |
| Transparency is important or interested in significance of predictors | Massive data (rows or columns) and not for short and fat or skinny and tall data |
| Fairly well behaved data                                              | Unwieldy data (missing, too many outliers or complex relationships)              |
| Need a quick initial benchmark                                        | Performance is the only thing that matters                                       |

* ## Hyper parameters to consider

  * We don't always use all of the hyper parameters available in an algorithm, we use the ones which will have the largest impact.
  * Here we'll only focus on the value of C. C is a regularization parameter that controls how closely the model fits the training data.
  * Regularization is a technique used to reduce overfitting by discouraging overly complex models in some way.
  * C is proportional to reverse of regularization, which means higher the C value, lower the regularization, higher the complexity which can lead to an overfit model.
  * And lower the C value, higher the regularization which can lead to an underfit model.
  * ![Effect of various C values on the flower petal dataset](images/c_value_model.png)

## Support Vector Machine

* ### What

  *