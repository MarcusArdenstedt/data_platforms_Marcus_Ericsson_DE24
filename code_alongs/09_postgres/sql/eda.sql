SELECT
    utbildningsnamn,
    utbildningsområde,
    "yh-poäng",
    beslut,
    "utbildningsanordnare administrativ enhet",
    kommun
FROM
    myh_2024
WHERE
    beslut = 'Beviljad'
    AND utbildningsområde = 'Data/IT';
------------------------------------------------------------------------------------------------------------------------------
SELECT
    COUNT(*)
FROM
    it_educations;
--------------------------------------------------------------------------------------------------------------------------------
SELECT
    *
FROM
    it_educations
WHERE
    LOWER(utbildningsnamn) LIKE '%data eng%';
--------------------------------------------------------------------------------------------------------------------------------

SELECT
    utbildningsnamn,
    "utbildningsanordnare administrativ enhet",
    beslut 
FROM
    it_educations
WHERE 
    LOWER(utbildningsnamn) LIKE '%data eng%'
    AND beslut = 'Beviljad';
------------------------------------------------------------------------------------------------------------------------------------
SELECT
    utbildningsnamn,
    utbildningsområde,
    beslut,
    kommun
FROM 
    devops_educations
WHERE 
    LOWER(kommun) LIKE '%st%';

SELECT 
    utbildningsnamn,
    COUNT(beslut) as number_approved
FROM 
    it_educations
WHERE 
    LOWER(utbildningsnamn) LIKE '%data eng%'
    AND beslut = 'Beviljad'
GROUP BY
    utbildningsnamn;

--------------------------------------------------------------------------------------------------------------------------------------
SELECT 
    utbildningsnamn,
    COUNT(beslut) AS number_that_got_approved
FROM 
    it_educations
WHERE 
    beslut = 'Beviljad'
GROUP BY 
    utbildningsnamn
ORDER BY 
    number_that_got_approved DESC;
---------------------------------------------------------------------------------------------------------------------------------------

SELECT 
    kommun,
    COUNT(kommun) as  number_approved
FROM 
    it_educations
WHERE 
    beslut = 'Beviljad'
GROUP BY  
    kommun
ORDER BY
    number_approved ASC;
------------------------------------------------------------------------------------------------------------------------------------------
WITH utbildningar_total AS (
    SELECT utbildningsnamn, COUNT(*) AS total_beslut FROM it_educations GROUP BY utbildningsnamn
)

SELECT 
    i.utbildningsnamn,
    COUNT(i.beslut) AS antal_beviljade,
    ROUND(100.0 * COUNT(i.beslut) / u.total_beslut, 2) AS percentage
FROM 
    it_educations i
JOIN utbildningar_total u ON i.utbildningsnamn = u.utbildningsnamn
WHERE 
    i.beslut = 'Beviljad'
GROUP BY
    i.utbildningsnamn, u.total_beslut;


