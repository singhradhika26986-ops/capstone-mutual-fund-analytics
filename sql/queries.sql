-- 1
SELECT fund_house, SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3
SELECT state, COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY state
ORDER BY sip_count DESC;

-- 4
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct<1;

-- 5
SELECT category, AVG(return_1yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

-- 6
SELECT plan, COUNT(*) FROM fact_performance GROUP BY plan;

-- 7
SELECT transaction_type, COUNT(*) FROM fact_transactions GROUP BY transaction_type;

-- 8
SELECT fund_house, COUNT(*) FROM dim_fund GROUP BY fund_house;

-- 9
SELECT MAX(nav) FROM fact_nav;

-- 10
SELECT MIN(nav) FROM fact_nav;