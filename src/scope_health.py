import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ScopeMetric:
    completion_percentage: float
    deviation_from_original_scope: float
    pending_approvals: int

class ScopeHealthDashboard:
    def __init__(self):
        self.metrics = {}

    def update_metrics(self, project_id: str, metrics: ScopeMetric):
        self.metrics[project_id] = metrics

    def get_metrics(self, project_id: str) -> ScopeMetric:
        return self.metrics.get(project_id)

    def get_all_metrics(self) -> Dict[str, ScopeMetric]:
        return self.metrics

    def to_json(self) -> str:
        metrics_dict = {project_id: {
            'completion_percentage': metric.completion_percentage,
            'deviation_from_original_scope': metric.deviation_from_original_scope,
            'pending_approvals': metric.pending_approvals
        } for project_id, metric in self.metrics.items()}
        return json.dumps(metrics_dict)
