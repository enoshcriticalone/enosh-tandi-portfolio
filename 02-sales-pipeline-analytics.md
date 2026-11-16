# Case Study 02 — Sales Pipeline & Revenue Operations Analytics

**Category:** Business Analytics · Sales Operations · Client Development  
**Scenario:** A technology services team needs a simple view of opportunity distribution, deal value, weighted pipeline, and lead-source activity.  
**Data:** Synthetic, 42-opportunity sample. Not actual NIOS IT Solutions data.

## 1. Business problem

A pipeline can contain many opportunities without giving leadership a clear view of forecast quality. A stage label alone does not show whether next steps are current, whether opportunity values are realistic, or where leads may be stalling.

The objective is to create a basic pipeline snapshot that supports weekly reviews and more disciplined follow-up.

## 2. Questions to answer

1. How many opportunities sit in each pipeline stage?
2. What is the total open pipeline value?
3. What is the probability-weighted open pipeline?
4. How do opportunity counts and wins vary by lead source?
5. What process changes would improve visibility and follow-through?

## 3. Method

The sample dataset [`sales_pipeline_sample.csv`](../data/sales_pipeline_sample.csv) contains 42 opportunities, with an illustrative deal value, segment, source, stage, and stage probability.

Weighted value is calculated as:

`Deal value × stage probability`

The sample probabilities are fixed assumptions for demonstration: Prospect 10%, Qualified 25%, Discovery 40%, Proposal 60%, Negotiation 80%, Closed Won 100%, and Closed Lost 0%.

## 4. Results from the sample

- **42** total opportunities.
- **5** marked Closed Won and **6** marked Closed Lost.
- **₹16.90 million** total value across open opportunities.
- **₹7.37 million** probability-weighted open pipeline.
- **₹2.14 million** value marked Closed Won in this sample.

![Opportunity distribution by stage](../assets/charts/sales_pipeline_stages.png)

### Lead-source snapshot

The sample contains 11 Referral opportunities, 11 Website opportunities, 10 LinkedIn opportunities, and 10 Outbound Email opportunities. Referral and Website each have two and one closed wins respectively, while LinkedIn and Outbound Email each have one win. With such a small, synthetic sample, these differences should not be used to rank real channels.

## 5. Interpretation

Weighted pipeline is more useful than simply adding every deal value, but it is still a forecast assumption rather than guaranteed revenue. A stage probability should be validated against the organisation's historical win rates and adjusted for segment or deal type where enough data exists.

The most important operational gap in this dataset is not a demonstrated performance issue; it is the absence of fields such as next action, next action date, stage-entry date, close date, loss reason, and opportunity owner. Without these, pipeline reviews can become subjective.

## 6. Recommendations

| Priority | Recommendation | Why it helps |
|---|---|---|
| High | Make opportunity owner, next step, and next-step date mandatory | Creates clear accountability and reduces forgotten follow-ups |
| High | Add stage-entry date and calculate days in stage | Exposes opportunities that may be stalled |
| High | Record structured closed-lost reasons | Helps distinguish pricing, timing, fit, competition, and no-response losses |
| Medium | Compare stage conversion by segment and source over a larger time period | Supports better targeting without overreacting to small samples |
| Medium | Review probability assumptions quarterly against historical conversion | Improves forecast reliability |
| Medium | Separate new pipeline, existing pipeline, won revenue, and weighted forecast | Prevents different measures from being mixed in reports |

## 7. Example weekly pipeline review

- Review opportunities with no activity or no next step.
- Confirm stage evidence before moving an opportunity forward.
- Review proposal and negotiation deals with close dates in the current period.
- Capture client questions, technical dependencies, and internal owners.
- Assign action items with due dates and revisit them at the next review.

## 8. Technical files

- [Sample pipeline data](../data/sales_pipeline_sample.csv)
- [SQL queries](../sql/sales_pipeline_analysis.sql)
- [Python analysis script](../analysis/run_analysis.py)
- [Generated stage summary](../outputs/sales_stage_summary.csv)
- [Generated source summary](../outputs/sales_source_summary.csv)

## 9. Limitations and next iteration

The sample does not include actual customer identities, historical stage transitions, sales cycle duration, deal owner, close dates, or loss reasons. The stage probabilities are illustrative, not statistically estimated. A live version should use CRM history and clearly distinguish bookings, revenue recognition, pipeline, and forecast.

## 10. Relevant experience

My resume describes managing and monitoring a sales pipeline, tracking opportunities and follow-ups, reporting on conversion progress and revenue performance, coordinating client requirements with technical teams, redesigning elements of an API product sales funnel, and delivering product demonstrations. This case study translates those business-development workflows into a structured analytics exercise.
