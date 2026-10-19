# Quote Chatbot

A command-line chatbot that quotes a MacBook repair. It collects the
customer's details, asks which MacBook they have, asks which service they
need, and prints a receipt with the total cost.

I'm building this in stages to practise Python and, later, DevOps. Each
stage is a separate commit so the history shows how the project grew.

## Features

- Greets the customer when the chatbot starts
- Collects first name, surname, phone number and email
- Lets the user pick a MacBook model from a menu
- Lets the user add several services to one quote (screen repair,
  battery replacement, water damage, keyboard replacement), with prices
  in rand and no duplicates
- Re-asks until the user enters a valid choice
- Prints a final receipt listing the customer, MacBook, every service
  and the total cost

## Requirements

- Python 3 (no extra packages needed)

## How to run

```
git clone https://github.com/Kwezu/Quote-Chatbot.git
cd Quote-Chatbot
python3 chatbot.py
```

## Example output

```
=============================================
Welcome to the MacBook Repair Quote Chatbot!
I'll collect your details, then help you build a quote.
=============================================

--- Final Receipt ---
Customer: Randy Marsh
MacBook:  MacBook Pro 2021
Services:
  - Screen Repair: R200
  - Battery Replacement: R500
Total Cost: R700
```
## Project structure

| File | Purpose |
|---|---|
| `chatbot.py` | The chatbot |
| `LEARNING_LOG.md` | What I changed at each stage and what I learned |
| `index.html` | Prototype chat interface in HTML and JavaScript, built by a friend. It currently keeps its own copy of the menus and isn't connected to `chatbot.py` yet. |

## How to add a MacBook model or a service

Menus and prices are defined once, at the top of `chatbot.py`, in the
`MODELS` and `SERVICES` dictionaries. Add one line to either and the menu
and prompts update automatically.

## Git workflow

- `main` always holds the latest working version of the chatbot.
- `ui-development` is a separate branch where the web interface is being
  built in collaboration with a friend, so the working code on `main`
  stays safe while the UI is in progress.
- Changes from `ui-development` come back to `main` through a pull request
  after review.
- The tag `v0-original-console` marks the original console version, before
  any refactoring.
- Each stage is a small commit with a descriptive message, and
  `LEARNING_LOG.md` records what changed and why.
  - Features are built on short-lived branches and merged through pull
  requests, for example the greeting and multi-service work
  ([closed pull requests](https://github.com/Kwezu/Quote-Chatbot/pulls?q=is%3Apr+is%3Aclosed)).

## Roadmap

- [x] Working console version
- [x] Menus and prices moved into `MODELS` and `SERVICES`
- [x] Program flow wrapped in `main()` with a `__name__` guard
- [x] Greeting at startup
- [x] Several services per quote
- [ ] Customer details as a dictionary instead of a tuple
- [ ] One reusable menu function
- [ ] Separate quote logic from `input()` and `print()`
- [ ] Web interface
- [ ] Automated tests (`pytest`)
- [ ] CI with GitHub Actions
- [ ] Docker and deployment

See [LEARNING_LOG.md](LEARNING_LOG.md) for the reasoning behind each step.