-- Battery Degradation Analysis
SELECT
    Cycle,
    AVG(SOH) AS avg_soh
FROM battery_dataset
GROUP BY Cycle
ORDER BY Cycle;

-- Battery Health Summary
SELECT
    BatteryID,
    AVG(SOH) AS avg_soh,
    AVG(Capacity) AS avg_capacity
FROM battery_dataset
GROUP BY BatteryID;

--  Environmental Impact Analysis
SELECT
    Temperature,
    AVG(SOH) AS avg_soh
FROM battery_dataset
GROUP BY Temperature;

--  KPI Query
SELECT
    AVG(SOH),
    AVG(Voltage),
    AVG(Current),
    AVG(Temperature)
FROM battery_dataset;
