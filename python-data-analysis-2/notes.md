* ## **Jupyter Help**
    * Enclose formulas to have them formatted properly between $ signs. Eg. $\sqrt(1 + x)$
    * Esc-c to copy a cell
    * Esc-v to paste it
    * Esc-x to cut it
    * ctrl-m->d-> to delete the selected cell
    * Jupyter notebooks can be run on azure cloud as well.

    ----
* ## **Loops**
    * Basic definition:
        ```
        for i in iterator:
            # do something
        ```
    * The most common iterator is ```range([start], stop, [step])```, where stop is exclusive
----
* ## **Lists**
    * list.append to add an element at the end
    * list.extend to add multiple elements at the end of the list
    * List + list to concatenate
    * list.insert(i, elem) to change an element at a given position
    * del list[i] to remove by index
    * list.remove[elem] to remove by value
    * list.sort() to sort in natural order
    * sorted(ducks, reverse=True) to sort in reverse
    * Examples of slicing
        ```
        squares[0:2]
        squares[:4]
        squares[3:]
        squares[:]
        squares[0:7:2]
        squares[-3:-1]
        squares[2:4] = ['four', 'nine']
        del squares[4:6]
        ```
    * Tuples are like lists, except that the elements can't be modified or add new ones
    * Tuples and lists can be passed to functions with multiple variables like \*list or \*tuple
    ----
* ## **Dictionaries and sets**

    * ```capitals[key] = value ``` Can be used to add values to a dictionary
    * ```key in dict ``` Can be used to check if a key exists in a dictionary
    * ```dict1 + dict2``` doesn't work, we need to ```dict1.update(dict2)```
    * Anything hashable can be used as a key in dictionaries
    * ```hash('abcd')``` can be used to check the has of a given key
    * Looping over dictionaries can be done in multiple ways:
        ```
        for key in dict:
        for key in dict.keys()
        for value in dict.values()
        for k,v in dict.items()
        ```
    * dict.keys() is an iterator and can be made into a list using ```list(dict.keys())```
    * Order or insertion is preserved in dicts.
    * Can add to sets using ```continents.add('Antarctica')```
    * Can remove from sets using ```continents.remove('Antarctica')```

    ----
* ## **Comprehensions**
    * Comprehension examples:
        ```
        squares = [i**2 for i in range(1, 11)]
        squares_by_four = [i**2 for i in range(1, 11) if i**2 % 4 == 0]
        squares_dict = {i: i**2 for i in range(1, 11)}
        capitals_by_country = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
        countries_by_capital = {capital: country for country, capital in capitals_by_country.items()}
        # A generator is created if this syntax is used without the curly braces or with braces
        sum(i**2 for i in range(1, 11))
        counting = [j for i in range(1, 11) for j in range(1, i+1)]
        ```

    ----
* ## **Advanced Containers**
    * Named tuples can be created to avoid having to remember the indexes of data elements
        ```
        people = [("Michele", "Vallisneri", "July 15"),
          ("Albert", "Einstein", "March 14"),
          ("John", "Lennon", "October 9"),
          ("Jocelyn", "Bell Burnell", "July 15")]
        persontype = collections.namedtuple('person', ['firstname', 'lastname', "birthday"])
        namedpeople = [persontype(*person) for person in people]
        ```
    * Data-classes are an alternative to named tuples
        ```
        @dataclass
        class personclass2:
            firstname: str
            lastname: str
            birthday: str = 'unknown'
            def fullname(self):
                return self.firstname + ' ' + self.lastname
        
        michele = personclass('Michele', 'Vallisneri')
        michele = personclass(firstname='Michele', lastname='Vallisneri')

        ```
    * Default dicts can be used to pass a function to supply default values for keys.
    * Just querying a key addes it to the default-dict
        ```
        def mydefault():
            return "I don't know"
        questions = collections.defaultdict(mydefault)
        questions['The meaning of life']

    ----
* ## **Advanced Containers**
    * Idioms are code snippets that have become the preferred way to do things. Eg.
        ```
        words = []
        for line in open('words.txt', 'r'):
            words.append(line.strip().lower())
        # strip removes leading and trailing space, lower converts to lowercase
        words = {line.strip().lower() for line in open('words.txt', 'r')}
        words = sorted({line.strip().lower() for line in open('words.txt', 'r')})
        ```
    * Can even read other language words, since python 3 has strings in Unicode by default
    * ```'-'.join(sorted("aaron"))```
    * Anagram sample
        ```
        # make a dict that maps each signature to the set of words with that signature;
        # each signature will map to at least one word

        words_by_sig = collections.defaultdict(set)

        for word in words:
            words_by_sig[signature(word)].add(word)
        # keep only the key/value pairs where the set has more than one element;
        # this is now a regular dict

        anagrams_by_sig = {sig: wordset for sig, wordset in words_by_sig.items() if len(wordset) > 1}
        # handle case when myword's signature is not found, returning the empty set

        def find_anagram_fast(myword):
            sig = signature(myword)

        try:
            return anagrams_by_sig[sig]
        except KeyError:
            return set()

        # list of signatures, sorted by length, longest first
        sorted(anagrams_by_sig.keys(), key=len, reverse=True)
        # list of anagram sets, sorted by signature length
        [anagrams_by_sig[sig] for sig in sorted(anagrams_by_sig.keys(), key=len, reverse=True)]
        # list of anagram sets, sorted by their length, largest first
        sorted(anagrams_by_sig.values(), key=len, reverse=True)
         ```
    * itertools standard library:
        ```
        # list all combinations of two different elements from the set {1,2,3} 
        list(itertools.combinations({1,2,3}, 2))
        ```
    ----
* ## **NumPy**
    * The **fundamental package for scientific computing with Python**
    * Fast, memory-efficient N-dimensional arrays
    * Excellent choice for large homogeneous data sets
    * A foundation for many mathematical packages and to integrate pytho with C and Fortran
    * Variables in python are just labels, the actual values are scattered across memory and 1 value can have multiple labels attach to it.
    * This also allows Python data structures to have heterogenous values.
    * This is good for normal programs, but not efficient when we have to work with large sets of similar values.
    * NumPy reserves space in memory and stores the values side-by-side.
        ![NumPy memory management](images/numpyStorage.png)
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
        ```
        monalisa_bw = np.loadtxt('monalisa.txt')
        # Number of dimensions
        monalisa_bw.ndim
        # Shape
        monalisa_bw.shape
        # Number of elements
        monalisa_bw.size
        # Data type
        monalisa_bw.dtype
        # PyPlot method to display 2-D arrays as images
        pp.imshow(monalisa_bw)
        pp.imshow(monalisa_bw, cmap='gray')
        ```
    * Create a numpy array with: ``` fromlist = np.array([[1,2,3],[4,5,6],[7,8,9]])```
    * 