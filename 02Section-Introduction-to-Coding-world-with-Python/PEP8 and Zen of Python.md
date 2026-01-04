# 🐍 PEP 8 — Python Style Guide (Summary)

Welcome to the **PEP 8 cheat sheet** — the official Python style guide that helps you write **cleaner, more readable, and consistent Python code**. 💡

PEP 8 stands for **Python Enhancement Proposal 8** and is the _de facto_ standard style guide used by Python developers around the world. It focuses on readability and maintaining a consistent coding style across projects.

Official spec 👉 https://peps.python.org/pep-0008/ 📄

---

## 🧠 What is PEP 8?

PEP 8 is a set of **coding conventions** for Python that covers:

- Naming conventions
- Indentation & whitespace
- Maximum line length
- Import formatting
- Comments & documentation
- Code layout & style

Following PEP 8 helps your code be:
✅ Easy to read  
✅ Consistent with community standards  
✅ Easier for teams and open-source collaboration

---

## 🛠️ Key Guidelines

### 🧹 1. **Indentation**

Use **4 spaces** per indentation level  
❌ Don’t mix tabs and spaces

```python
def foo():
    value = 10
```

---

### 📏 2. **Maximum Line Length**

Limit all lines to **79 characters**  
For docstrings and comments, prefer **72 characters**

---

### 📦 3. **Imports**

- Standard libraries first
- 3rd-party libraries next
- Local application imports last

```python
import os
import requests
from myproject.utils import helper
```

---

### 🧷 4. **Whitespace Rules**

Avoid extra whitespace around:

- inside parentheses
- before commas
- around operators

✔ Good:

```python
x = (a + b) * (c + d)
```

❌ Bad:

```python
x =( a+ b )* ( c + d )
```

---

### 🏷️ 5. **Naming Conventions**

| Type                | Style                         |
| ------------------- | ----------------------------- |
| Variables/Functions | `lower_case_with_underscores` |
| Classes             | `CapWords`                    |
| Constants           | `UPPER_CASE_WITH_UNDERSCORES` |
| Private Members     | `_single_leading_underscore`  |

---

### 💬 6. **Comments & Docstrings**

- Use `#` for inline comments
- Use triple-quoted strings for docstrings
- Write clear and descriptive comments

```python
def add(x, y):
    """Return the sum of x and y."""
    return x + y
```

---

### 🧱 7. **Blank Lines**

Use blank lines to separate:

- Functions
- Classes
- Logical sections of code

---

### 🎯 8. **Avoid Trailing Spaces**

Remove trailing whitespace — keeps diffs clean!

---

## 📚 Why PEP 8 Matters

Writing code that follows PEP 8:
✨ Improves readability  
🤝 Boosts collaboration in teams  
📦 Makes open-source contributions easier  
🧪 Helps new developers learn best practices

---

## 👨‍💻 Recommended Tools

Use these to enforce PEP 8 automatically:

- 🛠️ `flake8`
- 🖊️ `black` (auto-formatter!)
- 📏 `pylint`
- 🧼 `isort` for import sorting

---

## 🚀 Quick Example (Before → After)

Before 🧨

```python
def add(x,y):return x+y
```

After 🎯

```python
def add(x, y):
    """Return the sum of x and y."""
    return x + y
```

---

## 💡 TL;DR

> “Write Python code the way _the Python community expects_.”  
> → PEP 8 gives you the rules to do it ✨
