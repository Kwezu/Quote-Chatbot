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
  ## Customer details as a dictionary
- Before: get_user_info() returned a tuple and main() used positions
  like user_info[0], which breaks silently if the order changes.
- Change: it now returns a dictionary with labels (name, surname, phone,
  email), and main() reads user_info["name"] and so on.
- Tested: swapped the order inside the dictionary and the receipt stayed
  correct.
- Learned: labelled data is safer than positional data.