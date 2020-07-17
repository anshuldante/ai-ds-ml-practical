# Python data analysis

## **Jupyter Help**

* Enclose formulas to have them formatted properly between $ signs. Eg. $\sqrt(1 + x)$
* Esc-c to copy a cell
* Esc-v to paste it
* Esc-x to cut it
* ctrl-m->d-> to delete the selected cell
* Jupyter notebooks can be run on azure cloud as well.

## **NumPy**

* The **fundamental package for scientific computing with Python**
* Fast, memory-efficient N-dimensional arrays
* Excellent choice for large homogeneous data sets
* A foundation for many mathematical packages and to integrate python with C and Fortran
* Variables in python are just labels, the actual values are scattered across memory and 1 value can have multiple labels attach to it.
* This also allows Python data structures to have heterogenous values.
* This is good for normal programs, but not efficient when we have to work with large sets of similar values.
* NumPy reserves space in memory and stores the values side-by-side.
* ![NumPy memory management](images/numpyStorage.png)
* NumPy Data Types:
  * Integers:
    * numpy.int8
    * numpy.int16
    * numpy.int32
    * numpy.int64
  * Unsigned integers:
    * numpy.int8
    * And more...
  * Floating point numbers:
    * numpy.float32
    * numpy.float64
    * numpy.float128
  * Complex numbers
    * numpy.complex64
    * And more...
  * bool
  * Fixed length str
  * numpy.void (record arrays)
  * Object
* Numpy constructs:

## **Pandas**

* Overview
  * NumPy tables with labels
  * Powerful indexing
  * Modify table structure
  * Handles many data formats
  * Deals with missing data
  * Database operations
  * Plots
* Dataframes have multiple columns but series have just one column
* ![Pandas data/file formats](images/pandasDataFormats.png)
