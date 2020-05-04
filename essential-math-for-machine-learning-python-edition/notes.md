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

## Vectors and matrices
* **Vectors**
    * Magnitude of a vector  = square root of the sum of the squares of all of its coordinates
    * Angle of a vector = tan inverse of y/x
    * Rules to calculate theta:
        * Both x and y are positive: Use the tan-1 value.
        * x is negative, y is positive: Add 180 to the tan-1 value.
        * Both x and y are negative: Add 180 to the tan-1 value.
        * x is positive, y is negative: Add 360 to the tan-1 value.
    * In vector addition, you just have to add the individual components of the vectors
    * Multiplication in vectors:
        * Scalar multiplication: 
            * Results in another vector.
            * You just have to multiply the individual components of the vector by the scalar.
        * Dot product of vectors: 
            * Results in a scalar value
            * Just multiply the corresponding values and add.
        * Cross Product of vectors:
            * The result is a vector, perpendicular to the 2 original vectors.
                ```
                    r = a x b
                    * r1 = a2*b3 - a3*b2
                    * r2 = a3*b1 - a1*b3
                    * r3 = a1*b2 - a2*b1
                ```
* **Matrices**
    * Matrices of the same size can be added/subtracted by just adding the corresponding elements.
    * Matrices negation just negates the sign of all values
    * Matrix transposition rotates the matrix while keeping 0,0 the same:
        ```
            A = 3 5 1
                1 4 3
            AT = 3 1
                 5 4
                 1 3
        ```
    * Multiplication
        * Scalar: multiplying by a scalar
            * Just multiply the elements by the scalar
        * Dot product: multiplying 2 matrices
            * The number of columns in the first matrix should be equal to the number of rows in the second matrix.
            * The result of a(m,n). b(n,p) is a vector with dimensions: r(m,p)
            * r(0,0) = sum of (a(0, i)*b(i,0))
    * Identity Matrix
        * I is the equivalent of the number 1 in matrix terms.
        * D.I = D
    * Matrix division
        * Can't exactly divide matrices, but we can use the fact that division = multiplication by the reciprocal.
        * So to divide a matrix A by matrix B
            * Equal to multiplying by B(-1) or B-Inverse.
            * Find the inverse of B.
                * For (2,2): 
                    ``` 
                    A = a b
                        c d
                    determinant = ad-bc
                    A-1 = 1/det *  d  -b
                                  -c   a
                    ```
                * For (3,3)
                    * Write an identity matrix next to A and use row level operations to convert A into I
                    * The current state of the identity matrix becomes the inverse matrix.
                        ```
                        A = 3  0  2    1  0  0
                            2  0 -2 x  0  1  0 
                            0  1  1    0  0  1
                        # Add row 2 to row 1
                        # divide row 1 by 5
                        # multiple row 1 by 2 and subtract from row 2
                        # Multiply row 2 by -1/2
                        # Swap row 2 and row 3
                        # Subtract row 3 from row 2
    * Order is VERY IMPORTANT in matrix multiplication:
        ```
            A . X = C
            A-1 . A . X = A-1 . C (X = A-1 . C)
        ```
    * Matrix transformations:
        ``` 
            T(V) = A . V
    * Quiver plots:
        ```
            %matplotlib inline

            import numpy as np
            import matplotlib.pyplot as plt

            # We'll use a numpy array for our vector
            v = np.array([2,1])

            # and we'll use a quiver plot to visualize it.
            origin = [0], [0]
            plt.axis('equal')
            plt.grid()
            plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
            plt.quiver(*origin, *v, scale=10, color='r')
            plt.show()
        ```
    * Magnitude of a vector:
        ```
            import numpy as np

            vMag = np.linalg.norm(v)
            print (vMag)
        ```
    * Cos(theta) = V . S / ||V|| * ||S||