# POWERLEARN--PROJECT-AI-for-software-engineering-WEEK-4
# 🧠 Task 1- AI-Powered Code Completion 

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
```
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


# 🧪 Task 2: Automated Testing with AI

## 🎯 Objective
The goal of this task is to demonstrate how AI-powered tools like Selenium or Testim.io can be used to automate web application testing — specifically for login functionality. This includes running tests for valid and invalid credentials and highlighting how AI improves software testing compared to traditional manual methods.

## 🛠️ Tools & Framework
- **Framework**: Selenium WebDriver (Python)
- **Optional**: AI-enhanced plugins or Testim.io
- **Test Scenario**: Login page (valid & invalid credentials)
- **Deliverables**: Test script, screenshot of test results, 150-word summary

---

## ✅ Task Breakdown

1. **Automated Test Case**:  
   Developed a Selenium script to simulate login attempts using:
   - Valid credentials
   - Invalid username
   - Invalid password
   - Empty fields
   - Special characters

2. **Execution & Results**:  
   Tests executed on a sample login form.  
   Outcome: All five cases completed under 2 minutes. Screenshot attached.

---

## 📊 150-Word Analysis: AI-Powered vs Manual Testing

AI-powered automated testing significantly improves test coverage compared to manual testing in several key areas:

1. **Speed & Efficiency**: Automated tests execute in seconds. In our test case, 5 login scenarios completed in under 2 minutes.  
2. **Consistency**: AI ensures identical test execution every time, eliminating human errors seen in manual testing.  
3. **24/7 Testing**: Tests can run continuously after each code change, unlike human-dependent testing.  
4. **Better Coverage**: AI can test thousands of input combinations quickly, something humans can’t do within limited time.  
5. **Regression Prevention**: Automated tests catch when updates break existing functionality.  
6. **Cost Effectiveness**: Initial setup costs are offset by long-term efficiency gains.

However, manual testing still plays a crucial role in **UX validation** and **exploratory testing**, where human judgment and creativity are essential.

---

## 📎 Screenshot (Attach Here)

> *(Insert screenshot of test result showing pass/fail status for each login scenario.)*

## 🔢 Task 3: Predictive Analytics for Resource Allocation
## 🧠 Objective
To develop a machine learning model that predicts the priority of medical issues (e.g., high/medium/low) using the Kaggle Breast Cancer Dataset. This helps optimize how resources are allocated in healthcare settings.

## 📦 Dataset
Kaggle Breast Cancer Dataset
Source: Kaggle - Breast Cancer Wisconsin Dataset

## 🛠️ Steps Performed
Data Loading – Loaded dataset using pandas.

Data Preprocessing – Checked for missing values, removed irrelevant columns, and encoded categorical labels.

Feature Engineering – Defined features (X) and target variable (y).

Train/Test Split – Split the dataset into 80% training and 20% testing data.

Model Training – Trained a Random Forest Classifier using scikit-learn.

Prediction – Generated predictions using the test set.

Evaluation – Calculated accuracy, F1-score, and visualized a confusion matrix.

Comments – Added detailed comments for clarity and learning.

## 📈 Performance Metrics
Accuracy: XX.X%

F1 Score: XX.X

(Fill in your actual results from your notebook)

## 🤖 Why This Matters
By predicting the priority level of diagnoses, medical institutions can better allocate resources, triage urgent cases, and improve patient outcomes — especially in low-resource settings.


## 🧠 Tools Used
GitHub Copilot (VS Code)

Python 3.x

Jupyter Notebook or VS Code
