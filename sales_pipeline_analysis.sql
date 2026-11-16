-- Portfolio demonstration queries: sales pipeline health
-- Table name assumed: sales_pipeline_sample

-- Opportunity mix and value by stage
SELECT
    stage,
    COUNT(*) AS opportunity_count,
    SUM(deal_value_inr) AS total_deal_value_inr,
    SUM(deal_value_inr * stage_probability_pct / 100.0) AS weighted_value_inr
FROM sales_pipeline_sample
GROUP BY stage
ORDER BY CASE stage
    WHEN 'Prospect' THEN 1 WHEN 'Qualified' THEN 2 WHEN 'Discovery' THEN 3
    WHEN 'Proposal' THEN 4 WHEN 'Negotiation' THEN 5
    WHEN 'Closed Won' THEN 6 ELSE 7 END;

-- Lead-source performance snapshot
SELECT
    lead_source,
    COUNT(*) AS opportunities,
    SUM(CASE WHEN stage = 'Closed Won' THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN stage = 'Closed Won' THEN deal_value_inr ELSE 0 END) AS won_revenue_inr,
    ROUND(100.0 * SUM(CASE WHEN stage = 'Closed Won' THEN 1 ELSE 0 END)
          / NULLIF(COUNT(*), 0), 1) AS observed_win_rate_pct
FROM sales_pipeline_sample
GROUP BY lead_source
ORDER BY won_revenue_inr DESC;
