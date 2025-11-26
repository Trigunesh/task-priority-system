# Smart Task Priority Management System

This project is a smart task management application that analyzes tasks and assigns priority scores based on urgency, importance, effort, and dependencies. It helps users decide what task to work on first using intelligent decision logic.

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Trigunesh/task-priority-system.git
cd task-priority-system
2. Backend Setup (Django)
### Move to backend folder:

cd backend


# Activate the virtual environment:

venv\Scripts\activate


# 0Install dependencies:

pip install django djangorestframework


# Run migrations:

python manage.py migrate


# Start the server:

python manage.py runserver


### Backend will run at:

http://127.0.0.1:8000

#### 3. Frontend Setup

Open the frontend folder.

Simply open:

index.html


in your browser.

```

---

---

🧠 Algorithm Explanation (Priority Scoring)

This system calculates task priority using four intelligent evaluation factors:

1. Urgency (Due Date)

Tasks that are close to their due date receive higher priority. Overdue tasks are penalized heavily. The urgency score decreases as more days remain before the due date. Tasks due today or overdue gain maximum urgency points, ensuring deadlines are respected.

2. Importance (User Rating)

Each task is assigned a user-defined importance rating (1–10). This value directly influences the score and ensures that critical tasks are treated appropriately. A task with importance 10 has significantly higher priority than one rated 3, even if due dates are similar.

3. Effort (Estimated Hours)

Lower effort tasks receive a slight boost in priority to encourage completion of quick wins. Tasks with fewer hours provide psychological momentum and productivity increase. While effort is less significant than urgency or importance, it provides fine adjustment between similarly ranked tasks.

4. Dependencies

Tasks that block other tasks receive a significant bonus. If a task is required for dependent tasks to start, its priority automatically increases. Circular dependencies are detected and avoided to prevent infinite dependency loops.

Final Score (Smart Balance Strategy):

The system uses weighted scoring:

Urgency Weight: 40%

Importance Weight: 35%

Effort Weight: 15%

Dependency Bonus: 10%

This balanced strategy ensures urgent and important tasks dominate while still rewarding efficiency and workflow
structure.

---

---

⚖ Design Decisions
Why weighted scoring?

It provides flexibility and balance among multiple factors while avoiding dominance by a single variable.

Why no database?

The project focuses on analysis logic, not long-term storage. Tasks are passed through API calls for processing.

Why Django REST Framework?

It provides a clean structure, better input validation, and professional-grade API implementation.

Why frontend is simple?

The goal is to focus more on algorithm correctness than UI complexity.

⏱ Time Breakdown
Task Time Spent
Backend Setup 45 mins
Algorithm Implementation 40 mins
API Endpoints 20 mins
Frontend Development 45 mins
Testing & Debugging 30 mins
README 20 mins

Total ≈ 3.5 hours

---

---

🚀 Future Improvements

User authentication system

Task persistence in database

Role-based priority scoring

Drag-and-drop UI

AI-based prediction model

Mobile version

Calendar integration

Visualization using charts

Smart reminders and notifications
