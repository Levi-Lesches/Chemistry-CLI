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
```

```
$ python.exe -m bin.balance
Enter a chemical equation to balance: H2O + CO2 --> C6H12O6 + O2
6H2O + 6CO2 --> C6H12O6 + 6O2
```