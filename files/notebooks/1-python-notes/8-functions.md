# Python Functions

## 1. Fundamentals of Functions 🛠️

* **What is a Function?** Definition, purpose (modularity, code reuse, abstraction).
* **Defining a Function:**
    * Using the `def` keyword.
    * Function signature (name, parameters).
    * The function body and indentation.
    * The **Docstring** (`"""..."""`) and its importance (brief explanation of what it is and how to access it with `__doc__` or `help()`).
* **Calling/Invoking a Function:** Syntax and execution flow.
* **The `return` Statement:**
    * Returning a single value.
    * Returning **multiple values** (as a tuple).
    * Functions that don't explicitly return anything (they implicitly return `None`).

***

## 2. Function Parameters and Arguments 🔄

* **Parameters vs. Arguments:** Clarifying the difference.
* **Types of Arguments (How arguments are passed):**
    * **Positional Arguments:** Order matters.
    * **Keyword Arguments (KWA):** Order doesn't matter, but name is necessary (e.g., `func(a=1, b=2)`).
    * **Default Arguments:** Assigning a default value to a parameter in the definition (e.g., `def greet(name, message='Hello')`).
        * **⚠️ Mutable Default Argument Pitfall:** Crucial note on why mutable objects (like lists, dictionaries) shouldn't be used as default arguments.
* **Arbitrary Arguments (Variable-Length Arguments):**
    * **Positional:** `*args` (collected into a **tuple**).
    * **Keyword:** `**kwargs` (collected into a **dictionary**).
* **Argument Unpacking:** Using `*` and `**` when *calling* a function to unpack iterables (lists/tuples) or dictionaries.
* **Positional-Only and Keyword-Only Arguments (Python 3.8+):** Using the `/` and `*` in the parameter list to enforce how arguments must be passed.

***

## 3. Scope and Lifetime of Variables 🔭

* **Local Scope:** Variables defined inside a function.
* **Global Scope:** Variables defined outside any function.
* **Enclosing (Nonlocal) Scope:** Variables in an outer function (for nested functions/closures).
* **The LEGB Rule:** The order of scope resolution (Local, Enclosing, Global, Built-in).
* **`global` Keyword:** Used to modify a global variable from within a local scope.
* **`nonlocal` Keyword:** Used to modify a variable in an enclosing scope (for nested functions).

***

## 4. Advanced Function Concepts 🧠

* **First-Class Functions:**
    * Treating functions as data (assigning to variables).
    * Passing functions as arguments to other functions.
    * Returning functions from other functions.
* **Nested Functions:** Defining a function inside another function.
* **Closures:** A nested function that remembers and accesses variables from its enclosing scope, even after the outer function has finished execution.
* **Recursion:**
    * Definition and concept (a function calling itself).
    * **Base Case:** The condition to stop the recursion.
    * Examples: Factorial, Fibonacci.
* **Lambda Functions (Anonymous Functions):**
    * Syntax: `lambda arguments: expression`.
    * Use cases (typically for simple, single-expression functions, often with `map`, `filter`, `sorted`).
* **Type Hinting (Optional):** Adding type annotations to parameters and return values (e.g., `def add(a: int, b: int) -> int:`).

***

## 5. Decorators 🎩

* **Prerequisites:** Understanding first-class functions and closures.
* **What is a Decorator?** Definition and purpose (modifying or enhancing a function without changing its source code).
* **Decorator Syntax:** Using the `@decorator_name` syntax.
* **How Decorators Work:** Explanation of the underlying process (wrapping a function).
* **Common Use Cases:** Logging, timing execution, access control.
* **The `functools.wraps` Decorator:** Why it's necessary to preserve the decorated function's metadata (name, docstring).

***

## 6. Generators and Iterators ⚙️ (Closely Related)

* **Iterators vs. Iterables:** Brief distinction.
* **Generators:**
    * Functions that use the **`yield`** keyword instead of `return`.
    * How `yield` pauses and resumes execution, saving state.
    * Memory efficiency and lazy evaluation.
* **Generator Expressions:** A concise way to create generators (similar to list comprehensions but using parentheses).

***

## 7. Built-in Higher-Order Functions 📈

* **`map()`:** Applying a function to all items in an input list/iterable.
* **`filter()`:** Creating a list of elements for which a function returns true.
* **`zip()`:** Pairing elements from multiple iterables.
* **`reduce()` (from `functools`):** Cumulatively applying a function to the items of an iterable.
* **`sorted()`:** Using the `key` parameter (often with a `lambda`) for custom sorting.