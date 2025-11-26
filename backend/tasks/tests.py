from django.test import TestCase
from .views import calculate_priority

class PriorityTests(TestCase):

    def test_overdue_task_scores_higher(self):
        dep = {}
        task = {"title": "A", "due_date": "2020-01-01", "estimated_hours": 3, "importance": 5}
        score = calculate_priority(task, dep)
        self.assertGreater(score, 80)

    def test_high_importance_task_scores_higher(self):
        dep = {}
        task1 = {"title": "A", "due_date": "2030-01-01", "estimated_hours": 5, "importance": 10}
        task2 = {"title": "B", "due_date": "2030-01-01", "estimated_hours": 5, "importance": 1}
        self.assertGreater(calculate_priority(task1, dep), calculate_priority(task2, dep))

    def test_dependency_weight_increases_score(self):
     dep = {"A": 2}
     task = {"title": "A", "due_date": "2030-01-01", "estimated_hours": 5, "importance": 5}

     score_with_dep = calculate_priority(task, dep)
     score_without_dep = calculate_priority(task, {})

     self.assertGreater(score_with_dep, score_without_dep)
