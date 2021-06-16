# Python Chemistry
A collection of python scripts and packages to help with chemistry tasks. 

### Running scripts 

All the user-side scripts are in the `bin` directory, and all the data classes and helper functions are in the `lib` directory. Since Python makes `import` statements so difficult, you have to run these commands using the terminal (from inside the directory):

```bash
$ python -m bin.<script> 
```

Note that there is no `.py` when using `python -m`.

### Running tests

You can also run the tests, to make sure the code is still working. Not every part of the code is covered by tests, but the main components should be. The tests use `pytest`, which you may need to install first.

```bash
$ pip install pytest
$ pytest
```

## Features
- **Balancing chemical equations**. Simply enter your chemical equation and get the balanced result!
    ```
    $ python -m bin.balance
    Enter a chemical equation to balance: H2 + O2 --> H2O
    2H2 + O2 --> 2H2O
    
    $ python.exe -m bin.balance
    Enter a chemical equation to balance: H2O + CO2 --> C6H12O6 + O2
    6H2O + 6CO2 --> C6H12O6 + 6O2
    ```

- **Significant figures**. A program that can count significant figures in an expression. You can enter a number or a complete arithmetic expression.

    ```
    $ python -m bin.sigfigs
    Enter 1 to count sigfigs, or 2 to evaluate an arithmetic expression
    1
    Enter a number: 123.450
    That number has 6 significant figures

    What would you like me to do? python.exe -m bin.sigfigs
    Enter 1 to count sigfigs, or 2 to evaluate an arithmetic expression
    2
    NOTE: Order of operations are not implemented. Use parentheses if needed
    NOTE: All operators are limited to two operands. Use parentheses when needed
      Example: 1 + (2 + 3) instead of 1 + 2 + 3

    Enter an expression: 1.2 + (2.3 / 3.4)

    1.9
    ```

- **The Cheerios problem**. How high would a mole of Cheerios cover the Earth? Find out here!

    ```
    $ python -m bin.cheerios
    ```
    

- **Coming soon**: Ionization energies, naming molecules, Hess’s law, drawing Lewis Dot Structures
