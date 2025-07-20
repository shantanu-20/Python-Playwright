# 🕷️ Python Playwright Test Framework

This project is a lightweight **Python Playwright test framework** using `pytest`. It supports headless browser automation for UI testing and works perfectly in local environments or GitHub Codespaces.

---

## 📦 Features

- ✅ Playwright automation (Chromium, Firefox, WebKit)
- ✅ Pytest for test execution and reporting
- ✅ Headless mode support for CI or GitHub Codespaces
- ✅ Cross-browser testing capability
- ✅ Easy setup and extensibility

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-playwright-tests.git
cd python-playwright-tests
````

### 2. (Optional) Open in GitHub Codespaces

You can open this repo in [GitHub Codespaces](https://github.com/features/codespaces) for a pre-configured cloud development environment.

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
python -m playwright install
```

---

## 🧪 Run Tests

### Run all tests:

```bash
pytest
```

### Run with verbose output:

```bash
pytest -v
```

### Run a specific test file:

```bash
pytest tests/test_example.py
```

---

## 🌐 Example Test

Here’s a sample test located in `tests/test_example.py`:

```python
from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example Domain" in page.title()
        browser.close()
```

---

## 📁 Project Structure

```
.
├── .devcontainer/         # Codespaces / dev container setup (optional)
├── tests/
│   └── test_example.py    # Sample test case
├── requirements.txt       # Python dependencies
├── README.md              # Project overview and instructions
```

---

## ⚙️ Requirements

* Python 3.8 or higher
* pip (Python package manager)
* Playwright
* Pytest

---

## 📌 Tips

* Always run `python -m playwright install` after cloning or creating a new Codespace.
* Use `headless=True` and add `--no-sandbox` when running inside Codespaces or Docker.
* Add more test files under the `tests/` folder.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

Made with ❤️ using [Playwright](https://playwright.dev/python/docs/intro)

```

---

Let me know if you'd also like:
- A `requirements.txt` file
- A `.devcontainer` setup for GitHub Codespaces
- GitHub Actions CI workflow to run tests on push

I can generate them instantly.
```
