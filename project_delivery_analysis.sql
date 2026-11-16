-- Portfolio demonstration query: sprint delivery health
-- Table name assumed: project_sprint_metrics
SELECT
    sprint,
    planned_story_points,
    completed_story_points,
    ROUND(100.0 * completed_story_points / NULLIF(planned_story_points, 0), 1) AS completion_rate_pct,
    blockers_raised,
    carryover_items
FROM project_sprint_metrics
ORDER BY CAST(SUBSTRING(sprint, 8) AS INTEGER);

-- Overall delivery summary
SELECT
    SUM(planned_story_points) AS planned_points,
    SUM(completed_story_points) AS completed_points,
    ROUND(100.0 * SUM(completed_story_points) / NULLIF(SUM(planned_story_points), 0), 1) AS weighted_completion_rate_pct,
    AVG(blockers_raised * 1.0) AS avg_blockers_per_sprint
FROM project_sprint_metrics;
