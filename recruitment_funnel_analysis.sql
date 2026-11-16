-- Portfolio demonstration query: recruitment funnel
-- Table name assumed: recruitment_funnel_sample

SELECT
    stage_order,
    stage,
    candidate_count,
    ROUND(100.0 * candidate_count /
          NULLIF(LAG(candidate_count) OVER (ORDER BY stage_order), 0), 1)
          AS conversion_from_previous_pct,
    ROUND(100.0 * candidate_count /
          FIRST_VALUE(candidate_count) OVER (ORDER BY stage_order), 1)
          AS conversion_from_sourced_pct
FROM recruitment_funnel_sample
ORDER BY stage_order;
