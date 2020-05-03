## Equations, Graphs and functions
* Plotting linear equations:
    ```
    import pandas as pd

    # Create a dataframe with an x column containing values from -10 to 10
    df = pd.DataFrame ({'x': range(-10, 11)})

    # Add a y column by applying the solved equation to x
    df['y'] = (3*df['x'] - 4) / 2

    #Display the dataframe
    df
    %matplotlib inline
    from matplotlib import pyplot as plt

    plt.plot(df.x, df.y, color="grey", marker = "o")
    plt.xlabel('x') # label for x-axis
    plt.ylabel('y')  # Label for y-axis
    plt.grid() # creates a square grip in the plot
    plt.axhline() # x-axis line at 0,0
    plt.axvline() # y-axis line at 0,0

    plt.annotate('x-intercept',(1.333, 0)) # can be used to annotate a point in the plot
    plt.show() # show the graphs
    ```
* Mathematical operation in Python
    ```
    import math
    # Square root
    math.sqrt(9)
    9 ** 1/2
    # Cube root
    64 ** (1/3)
    # log
    math.log(64, 4)

    # plot y = 3 * x Pow 3
    df = pd.DataFrame({'x': range (-10, 10)})
    df['y'] = 3 * df['x'] ** 3
    # plot y = 2 pow x

    # Method to plot the amount gained every year given principle, interest and term
    def plotFinalAmount(principle, interest, term):
        df = pd.DataFrame({'x' : range(1, term + 1)})
        df['y'] = principle * ((1.0 + interest/100.0) ** df['x'])
        
        plt.plot(df['x'], df['y'], color="pink")
        plt.xlabel('Number of Years')
        plt.ylabel('Final Amount')
        plt.grid()
        plt.axhline()
        plt.axvline()
        plt.show()
    ```
* Plotting polynomials
    ```
    # y = (12/2x)2
    plt.plot(x, [f(a) for a in x], "Blue")
    plt.axhline()
    plt.axvline()
    plt.xlabel('x')
    plt.ylabel('f(x)')

    # plot an empty circle to show the undefined point
    plt.plot(0,f(0.0000001), color='purple', marker='o', markerfacecolor='w', markersize=8)

    plt.plot()
    # plotting scatter plots
    def k(x):
    if x == 0:
        return 0
    elif x == 100:
        return 1

    # Create an array of x values from -100 to 100
    x = range(-100, 101)
    # Get the k(x) values for every value in x
    y = [k(a) for a in x]

    # Set up the graph
    plt.xlabel('x')
    plt.ylabel('k(x)')
    plt.grid()

    # Plot x against k(x)
    plt.scatter(x, y, color='purple')

    plt.show()
    ```
* Method to find the value of a function on a given point:
    * Graph
    * Tables
    * Factorization
    * Substitution
    * Rationalization
## Derivatives and optimization

* Derivative rules:
    ``` if f(x) = g(x) * h(x)
        then f`(x) = g`(x) * h(x) + h`(x) * g(x)
        if f(x) = g(x)/h(x)
        then f`(x) = (g`(x)h(x) - h`(x)g(x)) / h(x)**2
        if f(x) = g(h(x))
        then f`(x) = g`(h(x)) h`(x)
    ```
* A function is derivative at a point if it's continuous at that point, the tangent line shouldn't be vertical and it should be smooth at that point i.e. it shouldn't change direction suddenly.
* Points at which the derivative ios zero or does not exist are called critical points.
* If the derivative is constant at zero, means the function has a constant value.
* If it crosses zero from positive to negative, that means a maxima.
* If it crosses zero from negative to positive, that means a minima.
* If it only touches zero, that means the function has an inflation points i.e. flattens out and resumes changing in the same direction.
* If the double derivative is positive: minima, if the double derivative is negative: maxima.