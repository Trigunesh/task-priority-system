import json
from datetime import datetime, date
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# ------------------- CORE PRIORITY ALGORITHM -------------------

def calculate_priority(task, dependency_map, strategy="smart"):
    today = date.today()
    due_date = datetime.strptime(task["due_date"], "%Y-%m-%d").date()

    days_left = (due_date - today).days

    # Urgency Score
    if days_left < 0:
        urgency = 100  # punishment for overdue tasks
    else:
        urgency = max(0, 50 - days_left)

    # Importance Score
    importance = int(task.get("importance", 5)) * 10

    # Effort Score (lower hours = higher score)
    effort = max(0, 30 - int(task.get("estimated_hours", 5)) * 2)

    # Dependency Weight
    dep_count = dependency_map.get(task["title"], 0) * 15

    # Strategy cases
    if strategy == "fast":
        return effort + urgency / 2
    if strategy == "impact":
        return importance
    if strategy == "deadline":
        return urgency * 1.5

    # Smart Balance (default)
    return urgency + importance + effort + dep_count


def detect_cycles(tasks):
    graph = {task["title"]: task.get("dependencies", []) for task in tasks}
    visited, stack = set(), set()

    def visit(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for dep in graph.get(node, []):
            if visit(dep):
                return True

        stack.remove(node)
        return False

    return any(visit(task) for task in graph)


# ------------------- MAIN API ENDPOINT -------------------

@csrf_exempt
def analyze_tasks(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    data = json.loads(request.body)
    tasks = data.get("tasks", [])
    strategy = data.get("strategy", "smart")

    if detect_cycles(tasks):
        return JsonResponse({"error": "Circular dependency detected"}, status=400)

    # Count how many tasks depend on each task
    dependency_map = {}

    for task in tasks:
        for dep in task.get("dependencies", []):
            dependency_map[dep] = dependency_map.get(dep, 0) + 1

    # Calculate scores
    for task in tasks:
        task["score"] = round(calculate_priority(task, dependency_map, strategy), 2)
        task["explanation"] = f"Urgency + Importance + Effort + Dependencies ({strategy})"

    tasks.sort(key=lambda x: x["score"], reverse=True)

    return JsonResponse({"sorted_tasks": tasks})


@csrf_exempt
def suggest_tasks(request):
    today = date.today()

    response = analyze_tasks(request)
    data = json.loads(response.content)

    top = data["sorted_tasks"][:3]

    reasons = []
    for t in top:
        reasons.append({
            "task": t["title"],
            "reason": f"High urgency, importance = {t['importance']}, effort = {t['estimated_hours']}"
        })

    return JsonResponse({"suggested": top, "reasons": reasons})
