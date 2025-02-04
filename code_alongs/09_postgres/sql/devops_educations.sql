SELECT
    utbildningsnamn,
    utbildningsområde,
    beslut,
    kommun 
INTO 
    devops_educations
FROM
    myh_2024
WHERE
    utbildningsnamn = 'DevOps Engineer';