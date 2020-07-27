# Seaborn Reference

| Method                                                                             | Description                                                                                                 |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| sns.boxplot(x='target',y='thalach', data=df)                                       | box plot                                                                                                    |
| sns.pairplot(iris, hue='species')                                                  | plot all variables against each other                                                                       |
| sns.regplot(x="petal_length", y="petal_width", data=iris, order=2)                 | plot x vs y and add a regression line (order decides the power of input)                                    |
| sns.lmplot(x="petal_length", y="petal_width", data=iris, hue='species')            | plot x vs y and add a regression line with conditionals                                                     |
| sns.residplot(iris['petal_length'], y, lowess=True, color="g")                     | Residual plot (between input and predicted variable)                                                        |
| sns.scatterplot(x=iris['petal_length'], y=iris['petal_width'],hue=iris['species']) | scatterplot between x and y colored by z, in pyplot, the variable values have to be mapped to numbers first |
