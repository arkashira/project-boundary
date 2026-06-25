import pytest
from scope_health import ScopeHealthDashboard, ScopeMetric

def test_update_metrics():
    dashboard = ScopeHealthDashboard()
    project_id = 'project-1'
    metrics = ScopeMetric(50.0, 10.0, 2)
    dashboard.update_metrics(project_id, metrics)
    assert dashboard.get_metrics(project_id) == metrics

def test_get_metrics():
    dashboard = ScopeHealthDashboard()
    project_id = 'project-1'
    metrics = ScopeMetric(50.0, 10.0, 2)
    dashboard.update_metrics(project_id, metrics)
    assert dashboard.get_metrics(project_id).completion_percentage == 50.0

def test_get_all_metrics():
    dashboard = ScopeHealthDashboard()
    project_id1 = 'project-1'
    project_id2 = 'project-2'
    metrics1 = ScopeMetric(50.0, 10.0, 2)
    metrics2 = ScopeMetric(75.0, 5.0, 1)
    dashboard.update_metrics(project_id1, metrics1)
    dashboard.update_metrics(project_id2, metrics2)
    all_metrics = dashboard.get_all_metrics()
    assert len(all_metrics) == 2
    assert all_metrics[project_id1].completion_percentage == 50.0
    assert all_metrics[project_id2].completion_percentage == 75.0

def test_to_json():
    dashboard = ScopeHealthDashboard()
    project_id = 'project-1'
    metrics = ScopeMetric(50.0, 10.0, 2)
    dashboard.update_metrics(project_id, metrics)
    json_string = dashboard.to_json()
    assert json_string == '{"project-1": {"completion_percentage": 50.0, "deviation_from_original_scope": 10.0, "pending_approvals": 2}}'

def test_get_metrics_non_existent_project():
    dashboard = ScopeHealthDashboard()
    project_id = 'non-existent-project'
    assert dashboard.get_metrics(project_id) is None
