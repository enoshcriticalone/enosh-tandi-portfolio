# Case Study 01 — Agile Project Delivery & Sprint Health

**Category:** IT Project Management · Agile Delivery · PMO Support  
**Scenario:** A cross-functional product team wants better visibility into sprint commitments, delivery consistency, blockers, and carryover.  
**Data:** Synthetic, eight-sprint sample. No employer or client data is used.

## 1. Business problem

A project manager can see individual tickets in a task board, but still struggle to answer basic delivery questions:

- Are sprint commitments realistic?
- Is the team consistently completing planned work?
- Which sprints experienced the greatest blocker load or carryover?
- What should be discussed in the next stand-up, review, or retrospective?

The objective is to turn sprint-level tracking into a repeatable delivery review.

## 2. Objective

Build a lightweight sprint health view that combines planned story points, completed story points, blockers raised, and carryover items. Use the analysis to identify where a project coordinator should investigate and what should be escalated.

## 3. Dataset and measures

The file [`project_sprint_metrics.csv`](../data/project_sprint_metrics.csv) contains eight illustrative sprint records.

| Measure | Definition |
|---|---|
| Sprint completion rate | Completed story points ÷ planned story points |
| Weighted completion rate | Total completed points ÷ total planned points |
| Blockers raised | Number of blockers recorded during a sprint |
| Carryover items | Items moved into a later sprint |

## 4. Results from the sample

- **322** story points were planned across eight sprints.
- **282** story points were completed.
- The weighted sprint completion rate was **87.6%**.
- The sample averaged **5.25 blockers per sprint**.
- Sprint 5 had the lowest completion rate (**81.0%**) and the highest blocker count (**8**) and carryover count (**8**).
- Sprint 7 had the lowest blocker count (**3**) and a completion rate of **90.9%**.

![Sprint planned vs completed](../assets/charts/sprint_delivery.png)

These are calculated results from the synthetic dataset only. They do not represent delivery performance at The Cloudrix Technologies or any other employer.

## 5. Interpretation

The overall completion rate is a useful starting point, not a standalone measure of team performance. Sprint 5 is the clearest review candidate because lower completion coincides with more blockers and carryover. The data does not explain why this happened; the coordinator should validate causes with the team rather than assume a capacity or performance problem.

A useful review would check whether Sprint 5 was affected by unclear acceptance criteria, unplanned work, late dependencies, environment issues, estimation uncertainty, or changes in priority.

## 6. Recommended project-coordination actions

| Priority | Action | Owner to involve | Evidence to review |
|---|---|---|---|
| High | Review Sprint 5 carryover and blockers item by item | Scrum Master, Developers, QA | Impediment log, ticket history |
| High | Make dependency owners and due dates visible before sprint start | Project Manager, technical leads | RAID log, dependency tracker |
| Medium | Compare planned capacity with leave, support work, and unplanned requests | Scrum Master, team | Capacity plan, sprint backlog |
| Medium | Check acceptance criteria and Definition of Done before work starts | Product Owner, QA, Developers | Product backlog, DoD |
| Medium | Track blocker age, not only blocker count | Project Coordinator | Impediment log with opened/resolved dates |

## 7. Example delivery cadence

**Before sprint planning:** confirm priority, capacity, dependencies, and acceptance criteria.  
**During the sprint:** update the board, capture blockers, assign owners, and escalate ageing dependencies.  
**At sprint review:** compare committed and completed work and record stakeholder feedback.  
**At retrospective:** select one or two measurable improvement actions with owners and due dates.

## 8. Example PM artifacts

- [Sample RAID log](../project-management/raid-log.csv)
- [Weekly project status report template](../project-management/project-status-report-template.md)
- [Sprint retrospective template](../project-management/sprint-retrospective-template.md)
- [SQL analysis](../sql/project_delivery_analysis.sql)
- [Python analysis script](../analysis/run_analysis.py)

## 9. Limitations and next iteration

Eight sprint snapshots are not enough to diagnose root causes or assess long-term predictability. The sample also lacks sprint duration, team capacity, story-level detail, defect/rework data, unplanned work, and blocker resolution time.

A production version should connect to Jira or the team's delivery tool, retain ticket-level history, and trend cycle time, throughput, ageing work, escaped defects, and dependency delays alongside sprint completion.

## 10. Relevant experience

My resume describes coordinating multiple IT projects, supporting sprint planning, daily stand-ups, sprint reviews and retrospectives, tracking tasks and milestones, following up on blockers and risks, and maintaining status reports, meeting notes, action trackers, and project documentation. This case study demonstrates how I would structure that coordination information into a delivery review.
