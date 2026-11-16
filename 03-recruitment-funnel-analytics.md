# Case Study 03 — Recruitment Funnel & Hiring Operations Analytics

**Category:** Business Analytics · Recruitment Operations · Process Improvement  
**Scenario:** A technical recruitment team wants to identify candidate drop-off between sourcing, screening, client submission, interviews, offers, and placements.  
**Data:** Synthetic funnel counts. No candidate-level or ATS data is included.

## 1. Business problem

Recruitment teams often track activity at each stage, but a list of candidate statuses may not show where the process is losing momentum. Funnel reporting helps distinguish sourcing volume from qualified pipeline and completed placements.

The objective is to map the candidate journey, quantify stage-to-stage conversion, and suggest process improvements.

## 2. Funnel dataset

The file [`recruitment_funnel_sample.csv`](../data/recruitment_funnel_sample.csv) contains illustrative counts:

| Stage | Candidates |
|---|---:|
| Sourced | 500 |
| Screened | 320 |
| Qualified | 210 |
| Submitted to client | 150 |
| Interviewed | 100 |
| Offer | 80 |
| Placed | 65 |

![Recruitment funnel](../assets/charts/recruitment_funnel.png)

## 3. Key metrics

- **64.0%** of sourced candidates reached screening.
- **65.6%** of screened candidates were classified as qualified.
- **66.7%** of submitted candidates reached interview.
- **81.3%** of offers converted to placements.
- **13.0%** of sourced candidates reached placement.
- **20.3%** of screened candidates reached placement.

These percentages are calculations from the synthetic sample, not actual personal or employer results.

## 4. Interpretation

The largest absolute reduction occurs between sourcing and screening: 180 of the 500 sourced candidates do not appear in the screened count. The next largest reduction is between screening and qualification: 110 candidates.

This does not automatically mean the sourcing channel or recruiter is underperforming. It may reflect duplicate profiles, candidate availability, compensation mismatch, location or work-authorisation constraints, incomplete profiles, timing, or a mismatch between the job description and screening criteria. Those reasons need to be captured in the ATS before corrective action is selected.

## 5. Recommendations

| Priority | Recommendation | Suggested measure |
|---|---|---|
| High | Standardise role intake and must-have criteria with the hiring manager | Requisition completeness; screening rejection reasons |
| High | Use role-specific screening rubrics | Qualified-to-submitted conversion by role |
| High | Capture a structured reason for every candidate rejection or withdrawal | Drop-off reason distribution |
| Medium | Set interview scheduling and feedback SLAs | Time from submission to interview; feedback turnaround |
| Medium | Keep ATS stages and candidate records updated | Records with complete status and next action |
| Medium | Review conversion by role family and sourcing channel | Stage conversion by role and source |

## 6. Example operational controls

- Confirm job requirements, priority skills, compensation range, and interview stages during intake.
- Keep one agreed definition for each ATS stage.
- Track candidate owner, client owner, next action, and next-action date.
- Record interview feedback and rejection reasons promptly.
- Review ageing candidates and open requisitions in a weekly operations meeting.
- Use a consistent evaluation rubric while allowing role-specific criteria.

## 7. Technical files

- [Synthetic recruitment funnel data](../data/recruitment_funnel_sample.csv)
- [SQL funnel query](../sql/recruitment_funnel_analysis.sql)
- [Python analysis script](../analysis/run_analysis.py)
- [Generated funnel summary](../outputs/recruitment_funnel_analysis.csv)

## 8. Limitations and next iteration

This is an aggregate funnel, not candidate-level cohort data. It does not include role, source, recruiter, date entered, date exited, withdrawal reason, interview round, or time-to-fill. A production analysis should use cohort-based conversion so that candidates have enough time to progress through all stages. It should also avoid comparing recruiters or channels without controlling for role difficulty and hiring-manager responsiveness.

## 9. Relevant experience

My resume states that I screened **300+ candidates** and contributed to **72 technical placements**, created screening and evaluation rubrics for **15+ engineering roles**, coordinated interview workflows and candidate follow-ups, maintained ATS records, and supported an ATS migration initiative. Those figures are separate resume facts. They are not the synthetic dataset or the result of this case-study analysis.
