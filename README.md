# 🤖 End-to-End Web Form Automation System

A complete automation pipeline that:

1. 🔍 Extracts form fields from any website
2. 📄 Converts them into a structured CSV
3. ✍️ Uses that CSV to automatically fill and submit forms

---

## 🧠 Project Overview

This project is divided into **two main modules**:

### 🔹 1. Form Structure Extractor

* Scans a webpage
* Detects input fields
* Extracts labels, selectors, and types
* Saves everything into a CSV file

---

### 🔹 2. Automated Form Filler

* Reads the CSV file
* Uses Playwright to open the website
* Fills form fields automatically
* Submits the form multiple times

---

## 🔄 Full Workflow

```text
Target Website
     ↓
[Extractor Script]
     ↓
CSV File (structure)
     ↓ (you fill answers)
[Form Filler Script]
     ↓
Automated Form Submission
     ↓
Screenshots + Logs
```

---

## 📦 Technologies Used

```python
Python
Playwright
BeautifulSoup
CSV Module
```

* **Playwright** → browser automation
* **BeautifulSoup** → HTML parsing
* **CSV** → structured data storage

---

## 📂 Project Structure

```
project/
│
├── extractor.py        # Extracts form fields
├── filler.py           # Fills & submits forms
├── website_structure.csv
├── screenshots/
│   ├── form_filled_1.png
│   ├── form_submitted_1.png
│
└── README.md
```

---

# 🔍 MODULE 1: Form Structure Extractor

## 🎯 Purpose

Extract all form fields from a webpage and store them in CSV format.

---

## ⚙️ How It Works

### Step 1: Open Website

```python
page.goto(TARGET_URL)
```

### Step 2: Get HTML Content

```python
html = page.content()
```

### Step 3: Parse HTML

```python
BeautifulSoup(html, "html.parser")
```

### Step 4: Find Fields

```python
soup.find_all(["input", "select", "textarea"])
```

---

## 🏷️ Label Detection Logic

The script intelligently finds labels using:

1. `<label for="id">`
2. Parent `<label>` wrapping
3. Previous sibling text
4. Grandparent fallback
5. `aria-label` / `placeholder`

---

## 📊 Output CSV

```csv
Field Name, Selector, Type, Your Answer
Name, #name, text,
Email, #email, email,
Country, #country, select,
```

---

# ✍️ MODULE 2: Automated Form Filler

## 🎯 Purpose

Fill and submit forms automatically using CSV data.

---

## ⚙️ How It Works

### Step 1: Load CSV Data

```python
fields = load_answers(CSV_FILE)
```

---

### Step 2: Launch Browser

```python
browser = p.chromium.launch(headless=False)
```

---

### Step 3: Loop for Multiple Submissions

```python
for i in range(1, times + 1):
```

---

### Step 4: Fill Fields

#### 🟢 Text Input

```python
element.fill(answer)
```

#### 🟡 Dropdown

```python
element.select_option(label=answer)
```

#### 🔵 Checkbox/Radio

```python
element.check()
```

---

### Step 5: Take Screenshots

```python
page.screenshot(path="form_filled_1.png")
```

---

### Step 6: Submit Form

```python
submit_btn.click()
```

---

### Step 7: Save Post-Submit Screenshot

```python
page.screenshot(path="form_submitted_1.png")
```

---

## 📊 Output

For each run:

* ✅ Form filled
* 🚀 Form submitted
* 📸 Screenshots saved

---

## 🔁 Execution Flow

```text
Run Extractor
   ↓
Get CSV Template
   ↓
Fill "Your Answer" column
   ↓
Run Form Filler
   ↓
Automated Submissions
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install playwright beautifulsoup4
playwright install
```

---

### 2️⃣ Run Extractor

```bash
python extractor.py
```

---

### 3️⃣ Fill CSV File

* Open `website_structure.csv`
* Enter values in **Your Answer**

---

### 4️⃣ Run Form Filler

```bash
python filler.py
```

---

## 🧠 Key Concepts Covered

* Web scraping
* Browser automation
* DOM parsing
* Data pipelines
* Error handling
* Automation workflows

---

## ⚠️ Limitations

* CAPTCHA-protected forms won’t work
* Dynamic JS-heavy sites may need tweaks
* Requires valid selectors

---

## 🚀 Future Improvements

* Auto-fill without manual CSV editing
* AI-based label detection
* GUI dashboard
* Multi-site automation
* Cloud deployment

---

## 🔥 Summary

This project is a **complete automation pipeline**:

✔ Extract → Structure → Fill → Submit
✔ Minimal manual work
✔ Highly scalable
✔ Real-world automation use cases

---

## 👨‍💻 Author

**Rachit Singh**

---

>
