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