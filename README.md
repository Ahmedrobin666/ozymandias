
# Ozymandias 1.0

A Python-based tool for performing various web security tests, including URL injection, route fuzzing, form testing, and file upload testing.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Options](#options)
6. [Examples](#examples)


---

## Features

This tool provides the following features:
- **URL Injection Testing**: Test for vulnerabilities by injecting payloads into URLs.
- **Route Fuzzing**: Discover hidden routes and endpoints by fuzzing.
- **Form Testing (POST Injection)**: Test forms for vulnerabilities like SQL injection or XSS.
- **File Upload Testing**: Upload files (e.g., PHP) by disguising them as images.

---

## Requirements

To run this script, you need the following:
- Python 3.x
- Libraries:
  - `requests`
  - `bs4` (BeautifulSoup)
  - `urllib`

Install the required libraries using:
```bash
pip install requests bs4
```

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ahmedrobin666/ozymandias.git
```

2. Navigate to the project directory:
```bash
cd Ozymandias
```

---

## Usage

Run the script using Python:
```bash
python main.py
```
You will be presented with a menu to choose from the available options.

---

## Options

The script provides the following options:

- **Test Payloads (URL Injection)**:
  - Test a website for URL injection vulnerabilities.
  - Requires:
    - Base URL of the site.
    - Path to a payloads file.

- **Test Routes (Fuzzing)**:
  - Discover hidden routes by fuzzing.
  - Requires:
    - Base URL of the site.
    - Path to a routes file.

- **Find and Test Forms (POST Injection)**:
  - Test forms for vulnerabilities like SQL injection or XSS.
  - Requires:
    - Base URL of the site.

- **Upload File (Image Upload)**:
  - Upload a file (e.g., PHP) by disguising it as an image.
  - Requires:
    - Base URL of the site.
    - Path to the file to upload.
    - Name of the file upload field.

---
## Payload lists
https://github.com/payloadbox/sql-injection-payload-list
https://github.com/payloadbox/xss-payload-list
https://github.com/danielmiessler/SecLists/tree/master
## Examples

### Example 1: Test Payloads
```bash
Enter your choice: 1
Enter the base URL of the site: https://example.com
Enter the path to the payloads file: payloads.txt
```

### Example 2: Upload File
```bash
Enter your choice: 4
Enter the base URL of the site: https://example.com/upload
Enter the path to the file to upload: /path/to/file.php
Enter the name of the file upload field: file
```
