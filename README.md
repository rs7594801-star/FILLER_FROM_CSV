# 📄 CSV Form Data Extractor — Code Explanation

This project is a Python-based automation script that extracts **form fields from a website** and saves them into a structured CSV file.

---

## 🧠 Core Idea

The script:

1. Opens a webpage using Playwright
2. Extracts HTML content
3. Parses it using BeautifulSoup
4. Identifies form fields (input, select, text area)
5. Finds their labels intelligently
6. Saves everything into a CSV file

---

## 📦 Libraries Used

```python
import csv
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
```

* `csv` → to create and write CSV files
* `BeautifulSoup` → to parse HTML content
* `Playwright` → to automate browser and load webpage

---

## 🌐 Target URL

```python
TARGET_URL = "https://www.digitalunite.com/practice-webform-learners"
```

This is the website from which form fields are extracted.

---

## 💾 Function: save_to_csv()

```python
def save_to_csv(data, filename="website_structure.csv"):
```

### 🔹 Purpose:

Stores extracted form data into a CSV file.

### 🔹 How it works:

* Opens/creates a CSV file
* Writes column headers:

  * Field Name
  * Selector
  * Type
  * Your Answer
* Iterates over extracted data
* Writes each field as a row

### 🔹 Output:

```csv
Field Name, Selector, Type, Your Answer
Name, #name, text,
Email, #email, email,
```

---

## 🏷️ Function: get_preceding_label()

```python
def get_preceding_label(field, soup):
```

### 🔹 Purpose:

Finds the **label (name)** associated with a form field.

### 🔍 Logic Breakdown:

1. **Check label using `for` attribute**

```python
label = soup.find("label", attrs={"for": field_id})
```

2. **Check if input is inside a label**

```python
parent = field.find_parent("label")
```

3. **Check text before field**

* Looks at previous sibling elements
* Extracts meaningful text

4. **Check grandparent**

* Handles complex HTML structures

5. **Fallback options**

```python
field.get("aria-label")
field.get("placeholder")
```

### 🔹 Why needed?

Websites use different structures → this makes extraction **robust**

---

## 🔍 Function: extract_fields()

```python
def extract_fields(html):
```

### 🔹 Purpose:

Extracts all usable form fields from HTML.

### 🔹 Steps:

1. Parse HTML:

```python
soup = BeautifulSoup(html, "html.parser")
```

2. Initialize:

* `seen` → avoids duplicate labels
* `fields` → stores results

3. Skip unwanted inputs:

```python
skip_types = {"hidden", "submit", "button", "reset", "image"}
```

4. Loop through fields:

```python
soup.find_all(["input", "select", "textarea"])
```

5. Get label:

```python
label = get_preceding_label(field, soup)
```

6. Avoid duplicates:

```python
if not label or label in seen:
    continue
```

7. Determine selector:

```python
# Prefer ID
"#id"

# Else use name
[name='field_name']
```

8. Store data:

```python
fields.append({
    "label": label,
    "selector": selector,
    "type": field_type,
})
```

---

## 🎮 Function: main()

```python
def main():
```

### 🔹 Purpose:

Controls the entire execution flow.

### 🔹 Steps:

1. Start Playwright:

```python
with sync_playwright() as p:
```

2. Launch browser:

```python
browser = p.chromium.launch(headless=True)
```

3. Open page:

```python
page.goto(TARGET_URL)
```

4. Wait for page to load:

```python
page.wait_for_selector("form, input, select, textarea")
```

5. Extract fields:

```python
data = extract_fields(page.content())
```

6. Save to CSV:

```python
save_to_csv(data)
```

7. Print results:

python
for item in data:
    print(item["label"])


8. Handle errors:

python


9. Close browser:

python
browser.close()


## ▶️ Entry Point

python
if __name__ == "__main__":
    main()


This ensures the script runs only when executed directly.



## 🔄 Full Workflow

text
Start Script
   ↓
Open Website (Playwright)
   ↓
Get HTML Content
   ↓
Parse HTML (BeautifulSoup)
   ↓
Extract Form Fields
   ↓
Find Labels Smartly
   ↓
Store Data
   ↓
Save CSV File
   ↓
End


## ⚡ Key Concepts Used

* Web Automation
* HTML Parsing
* DOM Traversal
* Data Extraction
* File Handling (CSV)

---

## 🧠 Summary

This script is a **mini automation tool** that converts any web form into a structured dataset, making it useful for:

* Form automation
* Testing
* Data entry systems

---
