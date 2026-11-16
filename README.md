# Data dictionary and usage notes

All datasets in this folder are synthetic portfolio examples. They do not represent actual employer, client, candidate, or customer records.

## `project_sprint_metrics.csv`
- `sprint`: Sprint label.
- `planned_story_points`: Planned story points.
- `completed_story_points`: Completed story points.
- `blockers_raised`: Blockers recorded during the sprint.
- `carryover_items`: Items moved to a later sprint.
- `completion_rate_pct`: Completed / planned × 100.

## `sales_pipeline_sample.csv`
- `opportunity_id`: Synthetic opportunity identifier.
- `segment`: Illustrative business segment.
- `lead_source`: Illustrative source channel.
- `stage`: Current sample pipeline stage.
- `deal_value_inr`: Illustrative deal value in INR.
- `stage_probability_pct`: Assumed probability used to calculate weighted value.
- `created_date`, `last_activity_date`: Synthetic dates.

## `recruitment_funnel_sample.csv`
- `stage_order`: Funnel sequence.
- `stage`: Recruitment process stage.
- `candidate_count`: Illustrative candidates at the stage.
- `conversion_from_previous_pct`: Stage conversion from the prior stage.
- `conversion_from_sourced_pct`: Share of initial sourced count remaining at each stage.

## Important
The sample data is designed to demonstrate analytical methods. Do not describe any computed metric as actual historical company performance.
