---
layout: post
title:  "Python – note plan"
author: Dipak Pulami Magar
date:   2025-08-20 10:12:45 +0545
categories: note-plans
status: draft
---

# Python Fundamenatals/Basics
## 1.1. Introduction to Python
- **What is Python?**
  - High-level, interpreted, {dynamically typed}, general-purpose programming language.
  - Key Features: Simple syntax, dynamic typing, vast standard library, cross-platform, portable
  - History and evolution/versions
    -  Differences between Python 2 and Python 3, current version relevance (Python 3.x as of 2025).
  - History: Key milestones, such as creation by Guido van Rossum, major versions (Python 2 vs. Python 3 differences, end-of-life for Python 2).
  - Philosophy: (e.g., readability, simplicity via the Zen of Python)
  - Application and use cases: Web Development, Data Science, Automation
  - Advantages over other languages.
## 1.2. Installation and Setup/Setting up the Environment**
  - Installing Python (using the official installer or environments like Anaconda)
  - Downloading from python.org, using package managers like Anaconda or Miniconda, virtual environments with venv or virtualenv.
  - Using the Python IDLE (Integrated Development and Learning Environment).
  - Using the Python Interactive Shell (REPL)
  - The Python Interpreter (REPL)
  - Integrated Development Environments (IDEs) vs. Code Editors (e.g. **VS Code**, PyCharm, Sublime Text, ___, **Jupyter Notebook**, etc.)

   - **Installation and Setup**: How to install Python, set up an IDE (e.g., PyCharm, VS Code) or use environments like Jupyter Notebook.
   - **Running Python Code**: Using the Python interpreter, scripts (.py files), and interactive environments.
   - Running Python code: Interactive mode (REPL via python command), writing and executing scripts (.py files), using IDEs like VS Code, PyCharm, or Jupyter Notebooks.

## 1.3. **Basics/Python Syntax and Structure**
   - **Basic Syntax**: Indentation rules, comments (# for single-line, """ for multi-line), and line continuation.
   - **Variables and Identifiers**: Naming conventions (e.g., PEP 8), reserved keywords, and variable declaration.
   - **Statements and Expressions**: Understanding single statements, multi-line statements, and expressions.

---

- **Basics: Running Python Code**
  - Running scripts from the command line/script excution: `python script.py`
  - Running Python code (interactive shell, script execution)
  - Executing a simple "Hello World" program.
  - - Writing your first Python program: `print("Hello, World!")`
  - **Comments**
    - Single-line (#): `# This is a comment`
    - Multi-line (triple quotes): `''' This is a multi-line comment '''`
      - docstrings/`"""docstrings"""`)
  - **(Code) Indentation and Formatting/Sytax overview**: 
    - Python uses whitespace (tabs or spaces) to define code blocks (loops, functions, classes). This is **non-negotiable**.
    - Indentation and code blocks: Role in defining scope, common errors related to whitespace.
  - **Input/Ouput**
    - `input()` function
    - The `print()` and formatting output
    - String interpolation (f-strings, `%`, `.format()`): Quite advanced, see later
    - Input and output: Using input() for user input, print() with formatting options (f-strings, .format(), % operator).

## 2. **Module 1: Variables and Data Types/Structure**
- **Variables**
  - What are variables?: Labels pointing to a value in memory.
  - Defining and naming variables??
  - Variable Assignment: `name = "Alice"`
  - Reassignment and Multiple assignment 
  - Dynamic Typing: A variable can hold a value of any type. (type determined at runtime); consider difference: Declaring a variable (`int a;`, `a = 5;` or `int a = 5;` in other programming languages)
  - Rules for variable names (identifiers): 
    - start with a letter/underscore, 
    - contain letters/numbers/underscores, 
    - case-sensitive
  - Naming conventions (PEP 8 standards).
  - Variables: Declaration, naming conventions (snake_case), dynamic typing, assignment statements.
- **Python keywords and identifiers**
  - **Keywords**
    - List of reserved words in Python (`if`, `for`, `while`, `def`, `class`, etc.). 
    - You cannot use these as variable names. 
    - List all Python keywords using:
      - >`import keyword;` 
      `print(keyword.kwlist)`
  - **Identifiers**:
    - dfsf
    - dfs

- **Built-in/Basic?/Primitive Data Types**
  - **Numeric:**
    - `int`: Integer numbers (e.g., `5`, `-10`, `1000`).
    - `float`: Floating-point numbers (e.g., `3.14`, `2.0`, `-0.5`).
    - `complex`: Complex numbers (e.g., `1+2j`).
  - **Text:** (brief)
    - `str`: String of characters (e.g., `"hello"`, `'world'`).
    - `str` (strings) and character encoding (Unicode).
    - `str` (strings, escape characters, raw strings, string methods).
    - strings (str) including single/double/triple quotes and escape sequences,
  - **Boolean:**
    - `bool`: Represents `True` or `False`.
  - **None/NoneType:**
    - `None`: Represents the absence of a value.
- **Other Data Types**: will be dealt in Module: X in detail
  - **Sequence:**
    - `list`: Ordered, mutable collection. `[1, "a", 3.14]`
    - `tuple`: Ordered, **immutable** collection. `(1, "a", 3.14)`
    - `range`: Immutable sequence of numbers. `range(5)`
  - **Mapping:**
    - `dict`: Unordered collection of key-value pairs. `{"name": "Bob", "age": 30}`
  - **Set:**
    - `set`: Unordered collection of **unique** objects. `{1, 2, 3}`
    - `frozenset`: Immutable version of a set.
  - **Binary types** (`bytes`, `bytearray`, `memoryview`)
- **Checking Type with `type()`**
  - The `type()` and `id()` functions
- **Type Conversion (Casting)**: 
  - Converting between types: `int()`, `float()`, `str()`, `bool()`, `list()`, etc.
  - Implicit vs. explicit type casting (e.g., `int()`, `str()`, `float()`).
  - Using int(), float(), str(), bool() functions, 
  - implicit vs. explicit conversion.
- Mutable vs Immutable objects??
- **Mutable vs. Immutable Types**: Understanding mutability (e.g., lists are mutable, tuples are immutable).

---

## 3. Operators and Expressions
- **Arithmetic Operators:** `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus/modulo), `**` (exponent-iation).
- **Comparison/Relational Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`.
- **Assignment Operators:** `=`, `+=`, `-=`, `*=`, `/=`.
- **Logical Operators:** `and`, `or`, `not`.
- **Identity Operators:** `is`, `is not` (check if two variables point to the same object).
- **Membership Operators:** `in`, `not in` (check if a value is present in a sequence).
- **Bitwise Operators**: `&`, `|`, `^`, `~`, `<<`, `>>` (with examples of binary operations).
- Operator precedence and associativity: Using parentheses for clarity.
- Expressions and evaluation order
- Identity and Membership Operators

---

## 4. Control Flow Statements
- **Conditional Statements**
  - Boolean expressions and truthiness
	- `if` statement
	- `if...else` statement
	- `if...elif...else` statement/ladder. (syntax and use cases)
	- Nested conditions
	- Ternary operators: conditional expressions, `x if condition else y`
- **Loops/Iteration/Loop constructs**
- **`for` loop**: with `range()`, iterables
  	- `range()` function
  	- for loops (iterating over sequences like range(), lists)
  	- Iterating over sequences and iterables (list, tuple, string, dictionary, range).
    	- Using `for i in range(5):`
      - Using `for item in my_list:`
	- **`while` loop**: 
  	- Condition-based iteration/repeats as long as a condition is true.
  	- Indefinite looping based on a condition.
  	- Infinite loops and how to avoid them.
- **Loop Control Statements**
	- `break`: Exit loop; Exit the loop entirely.
  - `continue`: Skip iteration; Skip the rest of the current iteration and move to the next.
  - `pass`: Placeholder; A null statement; a placeholder for future code.
- **Loop `else` clause**
  - The `else` clause with loops (unique usage).
  - `for...else`
  - `while...else`
- **Practical patterns**:
  - Counting, summing, filtering loops
  - Iterating over lists, dicts, sets, etc.
- Common patterns: Looping with enumerate(), zip(), and range() for indices and multiple iterables.
- **Comprehensions:**
  - List Comprehensions.
  - Dictionary and Set Comprehensions.
  - (e.g., `[x**2 for x in range(5)]`).

---

## 5. Data Structures (Collections)
### 5.1 Strings (`str`)
- Definition:
- Features:
  - Immutability (of strings)
  - 
- Creation (single, double, triple quotes) 
- **String Operations/Manipulation**:
  - String concatenation (+) 
  - String repetition (*)
  - String Indexing: accessing strings
    - `string[0]`
    - Negative Indexing
  - String Slicing: 
    - (start:stop), [start:end:step]
      - `string[2:5]`:
    - (start:stop, step), [start:end:step]
      - `string[2:15:2]`
- **Common String Methods**: 
  - `.lower()`: 
  - `.upper()`: 
  - `.title()`:
  - `.capitalize()`: 
  - `.strip()`:
  - `.split()`:  
  - `.join()`:
  - `.find()`: 
  - `.replace()`:

- String Formatting/Formatted Strings:
    - f-strings (Python 3.6+): `f"Hello, {name}!"`
    - `str.format()` method.
    - %-formatting (old style)/`%` operator.
- Escape sequences (`\n`, `\t`, etc.)

- **Regular Expressions**: basics
  - Basic introduction to `re` module for pattern matching.
  - Introduction to re module for pattern matching (match, search, findall).

### 5.2. Lists (`list`)
- Definition:
- Feature: 
  - mutability 
  - ordered
- List Operations: 
  - Creating lists: Literal syntax [], list() constructor.
  - Accessing elements/indexing list
  - Slicing elements/subsetting: 
  - Modifying elements:
  - Adding new items
    - `append`
    - `insert`
    - `extend` 
  - removing (
    - `remove`
    - `pop`
- Common List Methods: 
  - `sort()`, 
  - `reverse()`, 
  - `index()`, 
  - `count()`, 
  - `copy()`, 
  - [`len()`]
- Slicing and copying: Shallow vs. deep copies (using copy module).
- Multidimensional lists: Nested lists for matrices or grids.
- List Comprehensions:
  - Nested lists and list manipulation.
- Syntax for concise list creation, with conditionals and nested comprehensions.
- `[x*2 for x in range(5)]`

### 5.3. Tuples (`tuple?`):
- Definition
- Features: 
  - Immutability/immutable
    - Immutability and its implications.
    - immutability advantages.
  - order/sequences
- When to use tuples over lists
  - tuples vs lists
  - use cases (e.g., function returns, as dictionary keys)
- Tuple operations: 
  - Creating tuple with ()/tuple creation: 
  - Indexing
  - Slicing
  - Concatenation
  - Packing/unpacking tuples

### 5.4 Dictionaries (`dict`): [done]
- Definition
- Features: 
  - Mutability
  - unordered nature (ordered since Python 3.7+)
  - Key-value pairs (keys must be immutable)
- Dictionary Operations: 
  - Creating dictionaries: 
    - Literal syntax {key: value}
    - dict() constructor.
  - Accessing values 
    - by key: `my_dict["key"]`.
    - (get(), []), 
  - Modifying/updating values
  - Adding new items
  - Removing/deleting existing items/key-value pairs.
    - `del`
    - `.pop()`
- Common Dictionary Methods: 
  - `.keys()`:  
  - `.values()`:  
  - `.items()`: 
  - `.get()`: 
  - `.update()`: 
  - `.pop()`:
  - `clear()`: 
- Dictionary comprehensions: Similar to list comprehensions.
- Nested dictionaries: Handling complex structures like JSON-like data.

### 5.5. Sets
- Definition:
  - Unordered collections of unique items.
- Features
  - Unordered, 
  - unique elements, 
  - creation with {} or set(), 
  - Useful for membership testing and removing duplicates.
  - Creating sets
- Set Operations/methods: 
  - Union (`|`):
  - Intersection (`&`):
  - Difference (`-`): 
  - Symmetric Difference(^):
- Common Set Methods: 
  - operations like add(), remove(), discard(), pop().
  - .`add()`:
  - `.discard()`: 
  - `.clear()`, etc.
  - issubset(), 
  - issuperset().

### 5.7. Frozen sets: Immutable sets for dictionary keys.
- **Common Operations**: Length (`len()`), iteration, and membership testing.

---

## 6. Functions and Modularity
- **Introduction**:
  - What is a Function?
  - Why use it?
  - When use it?
- **Defining a Function**: 
  - `def` keyword, parameters, return statements.
  - def keyword, function name, parameters, docstrings (""" """).
  - `def function_name(parameters)`

- **Calling a Function**: 
  - `function_name(arguments)`

- **The `return` Statement**: 
  - `return value` (a function returns `None` by default).
  - Single/multiple returns, None as default.
- **Docstrings** (and how to use `help()`).

- **Argument vs Parameter**
  - sdf
  - dfs
- **Argument Types**:
  - Positional arguments
  - Keyword arguments
  - Default arguments (with the mutable default argument pitfall)
  - Variable-length/Arbitrary?? arguments: `*args` (non-keyword/positional), `**kwargs` (keyword)
    - *args (variable positional)
    - **kwargs (variable keyword)
  - Positional-only and keyword-only agruments (Python 3.8+)

- **Variable Scope/Scope and lifetime of variables**:  
  - (local, global, nonlocal)
  - LEGB rule (Local, Enclosing, Global, Built-in).
  - Local vs. Global scope.
  - The `global` and `nonlocal` keywords.
  - Local vs. global variables, `global` and `nonlocal` keywords.
  - Local vs. global variables, nonlocal keyword
 
### 6.3. Advanced Function Concepts:
- **Lambda Functions** 
  - Small anonymous functions (with lambda keyword)
  - `lambda x: x*2`
  - `lambda x: x**2`)
  - use in map(), filter(), sorted().
- **Recursion**: 
  - Writing recursive functions, base case, and recursive case.
  - Base case, recursive case, examples like factorial or Fibonacci, recursion depth limits.
  - Generators (using the `yield` keyword). ??


  - Documentation and docstrings ??

---

## 7. Module x: File Handling (and I/O)
- **Opening and closing files**: 
  - `open()` function
  - Reading and writing text files
  - File modes: `'r'`, `'w'`, `'a'`, `'rb'`, `'b'`, `'r+'`, `'wb'` etc.
  - Modes: `'r'` (read), `'w'` (write), `'a'` (append), `'r+'` (read/write).
  - The importance of closing files.
  - Using `with` statement for file operations
  - **The `with` Statement (Context Managers):** Preferred method for guaranteed resource cleanup.
  - The `with` statement (context manager) for safe file handling.
  - * Using `with` statement for safe file handling
- **Reading (from) Files**: `.read()`, `.readline()`, `.readlines()`.
- **Writing (to) Files**: `.write()`, `.writelines()`.
- Working with directories (`os` and `pathlib` modules)
- Exception handling in file operations
- **Working with CSV, JSON, and other formats (brief mention).**

- Opening files: open() function with modes (r, w, a, b for binary).
- Reading files: read(), readline(), readlines(), iterating over file objects.
- Writing files: write(), writelines().
- Context managers: with statement for automatic closing.
- 
- File paths: Absolute vs. relative, using os.path for manipulation.
- Handling CSV/JSON: csv module basics, json module (load, dump).

---

## Module 8. Error Handling and Exceptions
- Syntax Errors vs. Exceptions.
- **Types of Errors:** 
  - **What are Exceptions?** (Runtime errors).
- Built-in exception types: 
- **Common (buit-in) Exceptions:** 
  - `ZeroDivisionError`, 
  - `IndexError`, 
  - `KeyError`, 
  - `TypeError`, 
  - `ValueError`, 
  - `FileNotFoundError`, 
  - `IOError`, 
  - `NameErro?`, 
  - `SyntaxError?` etc.

- **Exception Handling:**
  - Syntax: `try`, `except`, `else`, `finally` 
  - The `try...except` block.
  - Catching specific exceptions (e.g., `ValueError`, `KeyError`).
  - Accessing the exception object (`as e`).
  - The `else` and `finally` blocks.
  - 
- **Handling Exceptions with `try...except` blocks.**
  - `try`, `except`, `else`, `finally` blocks.
  - Try-except blocks: try, except (specific or general), else (no exception), finally (cleanup).
  - 
- **Using `else` and `finally` clauses.**
- `try`, `except`, `finally`, `else`

- **Raising Exceptions manually**: Custom Exceptions
  - The `raise` keyword/statement.
  - raise statement, custom exceptions via class inheritance from Exception.
  - Using `raise` to trigger exceptions.
  - Creating custom exceptions (subclassing `Exception`)
  - Defining user-defined exception classes.
  - Defining user-defined exceptions with `class`.
  - 
- Assertions: assert statement for debugging.

---

## Module 9. Object Oriented Programming (OOP) Basics
- **Core Concepts**:
  - Classes and objects
  - Attributes and methods
- Four Pillers of OOP:
  - Abstraction, 
  - Encapsulation, 
  - Inheritance, 
  - Polymorphism.
- **Classes and Objects**:
  - Defining a Class: (`class` keyword) `class ClassName:`
  - Creating an Object (Instance): `obj = ClassName()`
  - The `__init__` method/constructor
  - The `self` parameter
- **Attributes and Methods**:
  - Instance variables vs. Class variables.
    * Instance methods, Class methods (`@classmethod`), and Static methods (`@staticmethod`).
    * Class variables and methods (`@classmethod`)
    * Static methods (`@staticmethod`)
    * Instance Attributes vs. Class Attributes.
    * Instance variables and methods
    * Instance methods, `self`, class vs. instance attributes.
    * Attributes and methods: Instance variables, class variables, instance methods, class methods (@classmethod), static methods (@staticmethod).
- **Methods:**
    - Instance methods (and the `self` parameter).
    - `__str__` method for user-friendly string representation.

- **Inheritance**
  - Creating subclasses, overriding methods.
  - Defining subclasses.
  * The `super()` function for calling parent methods.
  * Single inheritance, super() for parent calls, method overriding.
- **Polymorphism**: 
  - Method overriding and overloading concepts.
  - Method overriding, operator overloading basics (e.g., __str__, __add__).
- Encapsulation
  - Private attributes (using `_` or `__`), getters/setters.
- Encapuslation and abstraction concepts
  - Private attributes (__name), name mangling.
- **Special Methods (Dunder Methods):**
  - Examples: `__str__`, `__repr__`, `__len__`, etc
  - Magic methods (dunder methods): Overview of common ones like __repr__, __len__.

---

## Module 10. Modules and Packages
- **What is a Module?** 
  - A file containing Python code.
- **Importing modules**: 
  - Importing modules: import statement
    - `import <module>`: `import math`
    - `from <module> import <function>`: `from math import sqrt` 
  - **Alias usage**: `import <module> as <alias>`, 
    - from ... import ..., as alias
    - `import math as m`.

- **Standard (built-in) Library overview**: 
- **Datetime**: Working with dates and times (`datetime`, `timedelta`).
  * `datetime`: for date and time
  * `math`:  
    * `sqrt()`, `ceil()`), `random` 
  * `statistics`: for numeric work
  * `random`: for randomness
    * `randint()`, `choice()`).
  * `os` and `sys`: for system tasks
  - **OS and Sys**: Interacting with the operating system (`os.path`, `sys.argv`).
  * `json` and `csv` for data formats
- collections (e.g., defaultdict, Counter)
- **Itertools and Collections**: Useful tools for advanced iteration and data structures.

- Creating and using custom modules
- Using `__name__ == "__main__"` idiom
- **What is a Package?/Packages** 
  - A collection of modules in a directory.
  - Organizing multiple modules into directories.
- Installing and using external packages with `pip`
- `pip` and installing packages
- **Pip:** The package installer for Python (`pip install package_name`).

- **Virtual Environments (Crucial Topic):** The importance of `venv` or Conda for dependency management.
- **Importing Modules**: `import`, `from ... import`, aliasing (`import numpy as np`).
- **Standard Library**: Overview of useful modules (e.g., `math`, `random`, `datetime`, `os`).
- **Creating Modules**: Writing and importing custom modules.
- **Packages**: Structure and importing from packages.
- Creating modules: Writing custom .py files, __name__ == "__main__" idiom.
- Packages: Directory structure with __init__.py, relative imports.
- Third-party packages: Brief mention of pip for installation (though not installing in notes).

---

### Additional Fundamentals
- List comprehensions extensions: Set and dictionary comprehensions, generator expressions ().
- Iterators and generators: iter(), next(), yield keyword for generators, use in memory-efficient loops.
- Built-in functions: Common ones like len(), type(), id(), dir(), help(), map(), filter(), reduce() from functools.
- Performance basics: Time complexity for common operations (e.g., list append O(1), dictionary lookup O(1)).
- Best practices: PEP 8 style guide, virtual environments, debugging tips (print statements, pdb module).

### **13. Virtual Environment and Package Management**
* Why use virtual environments
* Creating and activating venv (`venv`, `virtualenv`)
* Installing packages (`pip install`)
* Freezing requirements (`pip freeze > requirements.txt`)
* Dependency management

### **Bonus / Next Steps**
*   **Virtual Environments:** Using `venv` to manage project dependencies.
<!-- *   **Pip:** The package installer for Python (`pip install package_name`). -->
*   **List Comprehensions, Dictionary Comprehensions, Generator Expressions.**
<!-- *   **Lambdas:** Small anonymous functions. `lambda x: x*2` -->
*   **The `main` function and `if __name__ == "__main__":` idiom.**

### 14. **Best Practices and Style Guidelines**
   - **PEP 8**: Python style guide (naming conventions, indentation, line length).
   - **Code Readability**: Writing clear, maintainable code with comments and docstrings.
   - **Virtual Environments**: Using `venv` or `virtualenv` for project isolation.
   - **Debugging Tips**: Using `print()`, `pdb`, or IDE debugging tools.


### **18. Practice and Mini Projects**
* Calculator program
* Simple bank app
* File analyzer
* Student grade tracker
* To-do list manager
* Number guessing game

---

### **12. Advanced Function Concepts**
* Higher-order functions
* Closures
* Decorators (function decorators, `@decorator`)
* Generators (`yield`, generator expressions)
* Iterators and the `iter()` / `next()` functions

---

### **14. Input/Output and Command Line Arguments**
* Taking user input (`input()`)
* Command-line arguments using `sys.argv`
* Formatted outputs (`print()` formatting options)
* **Console I/O**: `input()` for user input, `print()` for output, formatting options.
- **File Handling**:
 - Reading/writing files using `open()`, modes (`r`, `w`, `a`, `rb`, `wb`).
 - Context managers (`with` statement) for safe file handling.
 - Working with text and binary files.
---

### **15. Debugging and Logging**
* Using `print()` debugging
* The `assert` statement
* The `logging` module (levels, handlers, formatters)
* The `pdb` debugger (basics)

---

### **16. Pythonic Concepts**
* List comprehensions and dictionary comprehensions
* The `zip()` and `enumerate()` functions
* Unpacking (`*` and `**`)
* Type hinting (Python 3.5+)
* The `with` statement and context managers


### 13. **Miscellaneous Essentials/Additional Topics***
- **Iterators and Generators**: `iter()`, `next()`, and `yield` for memory-efficient iteration.
- **Decorators**: Basics of function and class decorators.
- **Context Managers**: Beyond file handling (e.g., custom context managers with `__enter__` and `__exit__`).
- **Basic Concurrency**: Introduction to `threading` and `asyncio` for parallel tasks.
- `map()`, `filter()`, `reduce()`
- `zip()` and `enumerate()`


### 15. **Basic Data Analysis and Libraries (Optional Intro)**
   - **NumPy**: Introduction to arrays and basic operations.
   - **Pandas**: Basics of DataFrames and Series for data manipulation.
   - **Matplotlib**: Simple plotting (line plots, bar charts) for visualization.

### Notes Structure Recommendations
- **Organize by Section**: Use headings for each major topic (e.g., "Data Types," "Control Flow").
- **Include Examples**: Provide concise code snippets for each concept (e.g., `for x in range(5): print(x)`).
- **Explain Key Terms**: Define terms like "mutable" or "scope" clearly.
- **Highlight Common Pitfalls**: Note common errors (e.g., modifying a list while iterating).
- **Add Practice Exercises**: Suggest small coding tasks (e.g., "Write a function to reverse a string").
- **Reference PEP 8**: Emphasize readable, standardized code.