日本語で読む: [README.ja.md](README.ja.md)

# Zodiac Checker

### Table of Contents

- [Overview](#overview)
- [Usage](#usage)
  - [Requirements](#requirements)
  - [Windows](#windows)
  - [macOS / Linux](#macos--linux)
- [Directory Structure](#directory-structure)

## Overview

A simple web application that determines your zodiac sign based on your birthday.
It is built with Python and Flask, and can be accessed through a web browser.
This project was created as practice for Python and web application development.

## Usage

### Requirements

- Python 3.10 or higher
- pip (Python's package management tool)

### Windows

1. Install Python

   - Download the latest version of Python from the [official website](https://www.python.org/downloads/) and install it
   - Be sure to check "**Add Python to PATH**" during installation

2. Clone this repository

  ```powershell
  git clone https://github.com/kotonekanno/zodiac-checker.git
  cd zodiac-checker
  ```

3. Create a virtual environment

  ```powershell
  py -m venv venv
  .\venv\Scripts\activate
  ```

4. Install Flask

  ```powershell
  pip install flask
  ```

5. Run the app

  ```powershell
  py app.py
  ```

6. Open http://127.0.0.1:5000 in your browser


### macOS / Linux

1. Install Python
   - Install the latest version of Python3 from the [official website](https://www.python.org/downloads/) and Install it

2. Clone this repository

  ```bash
  git clone https://github.com/kotonekanno/zodiac-checker
  cd zodiac-checker
  ```

3. Create a virtual environment

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

4. Install Flask

  ```bash
  pip install flask
  ```

5. Run the app

```bash
python app.py
```

6. Open http://127.0.0.1:5000 in your browser


## Directory Structure

```
zodiac-checker/
├── static/          # Images and CSS
├── templates/       # HTML templates
│   └── index.html  
├── app.py           # Main application file
├── README.en.md     # This file
└── README.ja.md     
```