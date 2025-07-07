# POWERLEARN--PROJECT-AI-for-software-engineering-WEEK-4
# 🧠 AI-Powered Code Completion – Task 1

## 🎯 Task Objective

Use **GitHub Copilot** to generate a Python function that sorts a list of dictionaries by a given key. Then manually write your own version of the function, compare both approaches, and reflect on their performance and learning value.

---

## 📄 Task Description

Given a list of student dictionaries:

```python
students = [
    {"name": "Alice", "score": 91},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 78}
]

# AI-Suggested Function (GitHub Copilot)
python
Copy
Edit
def sort_dict_list_by_key(data, key):
    return sorted(data, key=lambda x: x[key])
✅ Explanation:
sorted() is a Python built-in function.

key=lambda x: x[key] tells Python how to sort: by dictionary value at the given key.

# Manually Written Function (Beginner-Friendly)
python
Copy
Edit
def sort_dict_list_by_key(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data
# 📝 Explanation:
This is a simple version of bubble sort.

It compares and swaps items if they are out of order.

🔬 Output Comparison
python
Copy
Edit
students = [
    {"name": "Alice", "score": 91},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 78}
]

# Copilot version
print("AI version:", sort_dict_list_by_key(students, "score"))

# Manual version
print("Manual:", sort_dict_list_by_key(students, "score"))
📊 200-Word Comparison – Copilot vs Manual
In this task, I used GitHub Copilot to generate a Python function that sorts a list of dictionaries by a given key. Copilot suggested a very concise and efficient implementation using Python’s built-in sorted() function with a lambda function. The code was just one line and very readable.

In contrast, I manually wrote a version using nested loops, similar to a bubble sort. While this helped me understand sorting better, it was longer, less efficient, and more prone to bugs.

The AI-generated code is better for real-world projects because it is optimized (Python uses Timsort internally), easier to read, and less error-prone. It also took much less time to write using Copilot.

However, writing the manual version was still helpful for learning. It showed me how sorting works under the hood and deepened my understanding.

In conclusion, AI tools like GitHub Copilot are powerful for boosting productivity and writing clean code quickly. But manual coding builds core skills. The best approach is using both together: rely on AI for speed, but understand the logic for mastery.

📁 Deliverables
 Python code for AI and manual implementation

 Side-by-side comparison

 200-word reflection analysis


## 🧪 AI-Powered Automated Testing Summary - task 2

AI-powered automated testing significantly improves test coverage compared to manual testing in several key areas:

1. **Speed & Efficiency**: Automated tests execute in seconds. In our test case, 5 login scenarios (valid and invalid credentials) completed in under 2 minutes.
2. **Consistency**: AI ensures identical test execution every time, eliminating human errors often seen in manual processes.
3. **24/7 Testing**: Tests can run continuously, detecting issues right after code changes—something not possible with human-only testing.
4. **Better Coverage**: AI can test thousands of combinations systematically. Manual testing is inherently limited by time and mental capacity.
5. **Regression Prevention**: Automated scripts instantly flag issues when new code unintentionally affects existing features.
6. **Cost Effectiveness**: Though setup requires effort, automation significantly reduces long-term testing costs.

That said, **manual testing remains essential** for UX validation and exploratory testing, where human intuition and perception play a critical role.

✅ *Tool used: Selenium (with optional AI plugin support)*


🧠 Tools Used
GitHub Copilot (VS Code)

Python 3.x

Jupyter Notebook or VS Code
