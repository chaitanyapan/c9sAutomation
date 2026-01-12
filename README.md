# c9sAutomation **Playwright + pytest in GitHub Codespaces**.

---

````markdown
# Playwright + Pytest Setup in GitHub Codespaces

This repository demonstrates how to set up and run **Playwright with pytest** inside a **GitHub Codespace** for browser-based test automation using Python.

---

## 🚀 Prerequisites

- A GitHub account
- GitHub Codespaces enabled
- Basic knowledge of Python and pytest

---

## 🛠️ Tech Stack

- **Python 3**
- **Playwright (Python)**
- **pytest**
- **GitHub Codespaces**

---

## 📦 Setup Instructions

### 1️⃣ Create and Open a Codespace
1. Go to the repository.
2. Click **Code → Codespaces → Create codespace on main**.
3. Wait for the Codespace to start.

---

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
````

---

### 3️⃣ Upgrade pip

```bash
pip install --upgrade pip
```

---

### 4️⃣ Install Dependencies

```bash
pip install pytest playwright
```

---

### 5️⃣ Install Playwright Browsers

```bash
playwright install
```

(Optional – Chromium only)

```bash
playwright install chromium
```

---

### 6️⃣ Install System Dependencies

Required for running browsers in Codespaces:

```bash
playwright install-deps
```

---

## 🧪 Running Tests

### Example Test Structure

```
tests/
└── test_example.py
```

### Example Test (`tests/test_example.py`)

```python
from playwright.sync_api import sync_playwright

def test_example_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example Domain" in page.title()
        browser.close()
```

---

### Run Tests

```bash
pytest
```

Expected output:

```
1 passed in X.XXs
```

---

## 📁 Save Dependencies

Generate a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Install later using:

```bash
pip install -r requirements.txt
playwright install
```

---

## ❗ Troubleshooting

### Browser launch issues

```bash
playwright install-deps
```

### `pytest` command not found

Make sure the virtual environment is activated:

```bash
source .venv/bin/activate
```

---

## 📚 Useful Resources

* Playwright Docs: [https://playwright.dev/python/](https://playwright.dev/python/)
* pytest Docs: [https://docs.pytest.org/](https://docs.pytest.org/)
* GitHub Codespaces: [https://docs.github.com/codespaces](https://docs.github.com/codespaces)

---

Happy Testing! 🎭🐍
