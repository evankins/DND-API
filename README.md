# DND Personal Project

## Description

This project uses Python and PostgreSQL to manage and interact with DND character data, including their skills, abilities, and proficiencies. The application provides an API for accessing and manipulating this data, allowing users to create, read, update, and delete characters and their associated attributes. This project is a great way to combine a passion for D&D with software development, and serves as a practical exercise in database management, API development, and Python programming.

## Table of Contents

- [Requirments](#requirements)
- [How to run it](#how-to-run-it)
- [How to test it](#how-to-test-it)

## Requirements

- Python 3.9.13
- pgAdmin4

## How to run it

1. Clone the repository and go to the root directory.
2. Check you are running Python 3.9.13 in your terminal with `python --version`
3. Execute `pip install -r requirements.txt`
4. Create a new user and database in pgAdmin4
5. Create `db.yml` file in config file, following the format of example.yml with your information from step 4
6. Execute `python src/server.py`
7. Open in your browser `http://127.0.0.1:5000`

## How to test it

1. Make sure the server is running
2. Execute `python -m unittest`
