-- a) -------------------------------------------------------------
SELECT 
    utbildningsnamn,
    beslut,
    "utbildningsanordnare administrativ enhet"
FROM 
    data_engineer
WHERE 
    LOWER(utbildningsnamn) LIKE '%data engi%';

--b)--------------------------------------------------------------------

SELECT 
    utbildningsnamn,
    "utbildningsanordnare administrativ enhet",
    COUNT(beslut) AS nr_approved
FROM
    data_engineer
WHERE 
    beslut = 'Beviljad'
    AND LOWER(utbildningsnamn) LIKE '%data eng%'
GROUP BY
    utbildningsnamn, "utbildningsanordnare administrativ enhet";

-------------------------------------------------------------------------------------
-- c) 
SELECT 
    utbildningsområde,
    COUNT(beslut) AS nr_approved
FROM 
    data_engineer
WHERE 
    LOWER(beslut) = 'beviljad'
GROUP BY
    utbildningsområde;

--------------------------------------------------------------------------------------
-- d)
SELECT 
    kommun,
    COUNT(utbildningsnamn) AS nr_approved_program
FROM 
    myh_2024
WHERE 
    beslut = 'Beviljad'
GROUP BY    
    kommun
ORDER BY
    nr_approved_program DESC;
    
---------------------------------------------------------------------------------------------
-- e)
with all_count AS (
    SELECT utbildningsnamn, COUNT(*) AS total_amount FROM data_engineer GROUP BY utbildningsnamn
)

SELECT 
    d.utbildningsnamn,
    ROUND(100.0 * COUNT(d.beslut) / a.total_amount, 2) AS percentage
FROM data_engineer d
INNER JOIN all_count a ON d.utbildningsnamn = a.utbildningsnamn
WHERE 
    d.beslut = 'Beviljad'
GROUP BY 
    d.utbildningsnamn, a.total_amount;
