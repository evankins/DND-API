# GZG Personal Project

## Description

This project serves as a database designed to catalog the tables and attendees participating in the annual GZG tabletop convention. It aims to provide an organized inventory of available gaming tables and the individuals engaging in various tabletop games.

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
