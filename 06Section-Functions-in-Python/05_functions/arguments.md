### 🔹 Parameters vs Arguments in **Python**

## ✅ Parameters kya hote hain?

👉 **Function banate time** jo variables likhte ho, unko **parameters** kehte hain.

📌 _Ye sirf placeholders hote hain (empty boxes)_

### Example:

```python
def greet(name):
    print("Hello", name)
```

👉 Yahan `name` **parameter** hai
Kyuki function **define** karte waqt likha gaya hai.

---

## ✅ Arguments kya hote hain?

👉 **Function call karte time** jo actual value dete ho, usko **argument** kehte hain.

📌 _Ye real data hota hai_

### Example:

```python
greet("Chinmay")
```

👉 Yahan `"Chinmay"` **argument** hai
Kyuki function ko **call** karte waqt diya gaya hai.

---

## 🧠 Yaad rakhne ka simple rule:

- **Parameter = variable**
- **Argument = value**

---

## 🍵 Chai Example (Python style)

```python
def make_chai(sugar, tea_type):
    print(f"{tea_type} chai with {sugar} spoons sugar")
```

- `sugar`, `tea_type` → **Parameters**

```python
make_chai(2, "Ginger")
```

- `2`, `"Ginger"` → **Arguments**

---

## 🔁 Short Table:

| Parameter                  | Argument                 |
| -------------------------- | ------------------------ |
| Function define karte time | Function call karte time |
| Variable name hota hai     | Actual value hoti hai    |

---

## 🔥 Interview one-liner:

> **Parameters are variables in function definition, arguments are values passed while calling the function.**
