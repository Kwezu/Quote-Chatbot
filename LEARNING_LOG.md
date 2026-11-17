# Learning log

## Stage 0: working console version
- Built a quote chatbot with functions, dictionaries, and loops.
- Fixed 14 Pylance errors caused by leftover pasted code after `select_service()`.

## Experiment: what happens when the file is imported?
- Created `try_it.py` containing only `import chatbot`.
- Ran `python3 try_it.py`.
- Result: "Enter your first name:" appeared straight away, even though
  I only imported the file.
- Why: `user_info = get_user_info()` sits at the top level, so it runs
  as soon as the file loads.
- Why it matters: a web app, tests, and GitHub Actions can't reuse code
  that asks for input on load.
- Next: Step 2, wrap the flow in `main()`.
## Realisation: code should be written with testing in mind
- My first version works, but functions mix input(), print() and calculations.
- That makes it hard to test automatically.
- Plan: separate logic from display, one small step at a time.
## Step 1a: MODELS moved to the top
- Before: the MacBook menu lived inside select_macbook_model().
- Change: created a MODELS constant at the top of the file and made
  the function read from it.
- Result: the menu is defined in one place. Adding a model means
  editing one spot.
  ## Step 1b: SERVICES moved to the top, prompts built from data
- Before: the services menu lived inside select_service(), and prompts like
  "Enter 1, 2 or 3" were typed by hand, so they went out of date whenever
  I added an item.
- Change: SERVICES is now a top-level constant, and the prompts are built
  with ", ".join(MODELS) and ", ".join(SERVICES).
- Result: adding a model or service is a one-line change and the prompts
  update themselves.
- Also fixed a comment that described the wrong function.

## Step 2: main() and the __name__ guard
- Before: loose lines at the left margin ran as soon as the file loaded, so
  importing it started the questions and "user information" printed twice.
- Saw the chatbot run twice while the old lines and main() both existed,
  which showed exactly what main() contains.
- Change: removed the loose lines and added
  if __name__ == "__main__": main().
- Result: python3 chatbot.py runs once from start to receipt, and
  python3 try_it.py prints nothing.
- Learned: __name__ is "__main__" when a file is run directly and the
  file's name when it is imported.
  ## Greeting
- Added greet() and called it first in main().
- Learned: new behaviour goes inside functions, not loose at the left
  margin, or it would run on import again.
  ## Several services per quote
- Added ask_add_another() (y/n, loops until valid).
- main() keeps the chosen services in a list (order_items) and loops until
  the customer says no; the same service can't be added twice.
- The receipt loops over the list and adds up the total.
- Learned: lists, append(), looping over a list, a running total, and that
  a function only runs when something calls it.
  ## Step 3: Customer details as a dictionary
- A tuple stores values by position (user_info[0]); a dictionary stores them by
  label (user_info["name"]). Labels make code readable and harder to break
  when the order changes.
- Changing what a function returns means updating every place that uses it
  (here, main() in two spots).
- Git has two stages: `git add` picks what goes in, `git commit` saves it.
  Committing without adding does nothing.
- ^C / KeyboardInterrupt is me stopping the program with Ctrl+C, not a bug.

  ## Step 4: One reusable menu function
- Two near-identical functions (select_macbook_model, select_service) became
  one: choose_from_menu(title, options, describe).
- The parts that differed became inputs: a title, the options dictionary, and
  a small "describe" function that says how to display one option.
- A lambda (lambda model: model) is a tiny unnamed function, handy for
  one-line jobs like "show this exactly as it is".
- I added the new function first, tested it alone in try_it.py, swapped one
  menu at a time in main(), and deleted the old code only after each swap
  worked.
- When deleting a function, remove the whole thing: the def line plus
  everything indented under it. A leftover body causes an IndentationError,
  and deleting a function that is still called causes a NameError.
- A function call stored in a variable (user_info = get_user_info()) catches
  the function's return value.
  ## Step 5: Separate quote logic from input()/print() (in progress)
- Idea: the code that does the maths should not also talk to the customer,
  so it can be tested alone.
- Done so far: calculate_total(order_items) and add_service(order_items,
  service_name, price). Both return a value and print nothing.
- Still to do: build_receipt(), so main() only asks, calls and shows.
  ## To revisit: the running-total loop (accumulator pattern)
Where it lives: calculate_total() in chatbot.py

```python
total = 0
for item in order_items:
    total = total + item["price"]
```
## To revisit: the running-total loop (accumulator pattern)
Where it lives now: calculate_total() in chatbot.py

My original version, as it first appeared in main(), with my comments:

```python
    # Start the running total at zero.
    total = 0
    # Go through the cart one service at a time.
    for item in order_items:
        # Add this service's price to the total (200, then 200 + 500, and so on).
        total = total + item["price"]

        or

total = 0
for item in order_items:
    total = total + item["price"]
```

An experiment to watch it work (try_it.py):

```python
cart = [{"price": 200}, {"price": 500}, {"price": 300}]

total = 0
for item in cart:
    total = total + item["price"]
    print("added", item["price"], "-> total is now", total)
```

What I want to understand properly:
- Why total starts at 0 before the loop
- How total changes on each pass (0, then 200, then 700, and so on)
- Why item["price"] works (item is a dictionary, "price" is its label)

A shorter version exists, to learn once I'm comfortable with the loop:

```python
total = sum(item["price"] for item in order_items)
```
## Step 6: Automated tests (pytest)
Code: test_chatbot.py
- A test is a function that calls my code and uses `assert` to say what
  must be true. If it isn't, pytest fails and shows the expected and actual values.
- These tests work because the logic is separate from input()/print(): no
  customer has to type anything.
- Each test checks one behaviour: empty cart, adding up prices, a new
  service, a duplicate, and what the receipt contains.
- Test names say what should happen; docstrings say why it matters.
