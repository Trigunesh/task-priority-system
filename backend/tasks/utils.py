from datetime import datetime

def detect_circular(tasks):
    graph = {t["title"]: t["dependencies"] for t in tasks}
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False
        visited.add(node)
        stack.add(node)
        for dep in graph.get(node, []):
            if dfs(dep):
                return True
        stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False


def calculate_priority(task, tasks):
    today = datetime.today().date()
    due = task["due_date"]

    # Urgency
    days_left = (due - today).days
    urgency_score = max(0, 100 - (days_left * 5))

    # Importance
    importance_score = task["importance"] * 10

    # Effort (lower effort = higher score)
    effort_score = 50 / (task["estimated_hours"] + 1)

    # Dependencies (tasks that block others = higher score)
    blocking_count = sum(task["title"] in t["dependencies"] for t in tasks)
    dependency_score = blocking_count * 20

    score = urgency_score + importance_score + effort_score + dependency_score

    explanation = (
        f"Urgency: {urgency_score}, "
        f"Importance: {importance_score}, "
        f"Effort boost: {effort_score:.2f}, "
        f"Blocks {blocking_count} tasks"
    )

    return score, explanation
