# Quote Chatbot

A command-line chatbot that quotes a MacBook repair. It collects the
customer's details, asks which MacBook they have, asks which service they
need, and prints a receipt with the total cost.

I'm building this in stages to practise Python and, later, DevOps. Each
stage is a separate commit so the history shows how the project grew.

## Features

- Collects first name, surname, phone number and email
- Lets the user pick a MacBook model from a menu
- Lets the user pick a service (screen repair, battery replacement,
  water damage, keyboard replacement) with prices in rand
- Re-asks until the user enters a valid choice
- Prints a final receipt with the customer, service and total cost

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
--- Final Receipt ---
Customer: Thabo Nkosi
select_service: Keyboard Replacement
Total Cost: R300
```

## Project structure

| File | Purpose |
|---|---|
| `chatbot.py` | The chatbot |
| `LEARNING_LOG.md` | What I changed at each stage and what I learned |

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

## Roadmap

- [x] Working console version
- [x] Menus and prices moved into `MODELS` and `SERVICES`
- [x] Program flow wrapped in `main()` with a `__name__` guard
- [ ] Customer details as a dictionary instead of a tuple
- [ ] One reusable menu function
- [ ] Separate quote logic from `input()` and `print()`
- [ ] Web interface
- [ ] Automated tests (`pytest`)
- [ ] CI with GitHub Actions
- [ ] Docker and deployment

See [LEARNING_LOG.md](LEARNING_LOG.md) for the reasoning behind each step.