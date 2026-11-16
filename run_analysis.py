"""
Rebuild the portfolio charts and summary tables from the synthetic CSV files.
Run from the repository root:
    python analysis/run_analysis.py
All records are illustrative and are not employer/client data.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHARTS = ROOT / "assets" / "charts"
OUTPUTS = ROOT / "outputs"
CHARTS.mkdir(parents=True, exist_ok=True)
OUTPUTS.mkdir(parents=True, exist_ok=True)

# Project delivery
sprints = pd.read_csv(DATA / "project_sprint_metrics.csv")
weighted_completion = 100 * sprints["completed_story_points"].sum() / sprints["planned_story_points"].sum()
avg_blockers = sprints["blockers_raised"].mean()
sprints["completion_rate_pct"] = 100 * sprints["completed_story_points"] / sprints["planned_story_points"]
sprints.to_csv(OUTPUTS / "project_sprint_analysis.csv", index=False)

fig, ax = plt.subplots(figsize=(9, 5))
x = range(len(sprints))
ax.bar([i - 0.18 for i in x], sprints["planned_story_points"], width=0.36, label="Planned")
ax.bar([i + 0.18 for i in x], sprints["completed_story_points"], width=0.36, label="Completed")
ax.set_xticks(list(x), sprints["sprint"])
ax.set_ylabel("Story points")
ax.set_title("Sprint commitment vs. completion (synthetic data)")
ax.legend()
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(CHARTS / "sprint_delivery.png", dpi=160)
plt.close(fig)

# Sales pipeline
sales = pd.read_csv(DATA / "sales_pipeline_sample.csv")
stage_order = ["Prospect","Qualified","Discovery","Proposal","Negotiation","Closed Won","Closed Lost"]
stage_summary = sales.groupby("stage", as_index=False).agg(
    opportunities=("opportunity_id","count"),
    deal_value_inr=("deal_value_inr","sum"),
    weighted_value_inr=("deal_value_inr", lambda s: 0)
)
# Apply per-row stage probability before aggregation
sales["weighted_value_inr"] = sales["deal_value_inr"] * sales["stage_probability_pct"] / 100
stage_summary = sales.groupby("stage", as_index=False).agg(
    opportunities=("opportunity_id","count"),
    deal_value_inr=("deal_value_inr","sum"),
    weighted_value_inr=("weighted_value_inr","sum")
)
stage_summary["stage"] = pd.Categorical(stage_summary["stage"], categories=stage_order, ordered=True)
stage_summary = stage_summary.sort_values("stage")
stage_summary.to_csv(OUTPUTS / "sales_stage_summary.csv", index=False)

source_summary = sales.groupby("lead_source", as_index=False).agg(
    opportunities=("opportunity_id","count"),
    won_opportunities=("stage", lambda s: (s == "Closed Won").sum()),
    won_revenue_inr=("deal_value_inr", lambda s: s[sales.loc[s.index, "stage"] == "Closed Won"].sum())
)
source_summary["win_rate_pct"] = 100 * source_summary["won_opportunities"] / source_summary["opportunities"]
source_summary.to_csv(OUTPUTS / "sales_source_summary.csv", index=False)

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(stage_summary["stage"].astype(str), stage_summary["opportunities"])
ax.set_ylabel("Number of opportunities")
ax.set_title("Opportunity distribution by pipeline stage (synthetic data)")
ax.tick_params(axis="x", rotation=25)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(CHARTS / "sales_pipeline_stages.png", dpi=160)
plt.close(fig)

# Recruitment funnel
recruitment = pd.read_csv(DATA / "recruitment_funnel_sample.csv")
recruitment.to_csv(OUTPUTS / "recruitment_funnel_analysis.csv", index=False)
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(recruitment["stage"], recruitment["candidate_count"])
ax.set_ylabel("Candidates")
ax.set_title("Recruitment funnel (synthetic data)")
ax.tick_params(axis="x", rotation=25)
ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
fig.savefig(CHARTS / "recruitment_funnel.png", dpi=160)
plt.close(fig)

summary = pd.DataFrame([
    {"metric":"Planned story points","value":int(sprints["planned_story_points"].sum()),"unit":"points"},
    {"metric":"Completed story points","value":int(sprints["completed_story_points"].sum()),"unit":"points"},
    {"metric":"Weighted sprint completion","value":round(weighted_completion,1),"unit":"percent"},
    {"metric":"Average blockers per sprint","value":round(avg_blockers,1),"unit":"blockers"},
    {"metric":"Total sample sales opportunities","value":len(sales),"unit":"opportunities"},
    {"metric":"Closed-won sample opportunities","value":int((sales["stage"]=="Closed Won").sum()),"unit":"opportunities"},
    {"metric":"Sample placed candidates","value":int(recruitment.iloc[-1]["candidate_count"]),"unit":"candidates"},
])
summary.to_csv(OUTPUTS / "portfolio_metrics_summary.csv", index=False)
print(summary.to_string(index=False))
