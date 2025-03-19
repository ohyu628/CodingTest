-- 코드를 입력하세요
# MySQL 버전
# IF함수 사용
SELECT ANIMAL_ID, NAME, 
    IF(SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%', 'O', 'X') AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

# CASE문, 정규표현식 사용
SELECT ANIMAL_ID, NAME, 
    CASE 
        WHEN REGEXP(SEX_UPON_INTAKE, 'Neutered|Spayed') THEN 'O'
        ELSE 'X'
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;


# Oracle 버전
# CASE문, LIKE 연산자 사용
SELECT ANIMAL_ID, NAME, 
    CASE
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
        ELSE 'X'
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

# CASE문, 정규표현식 사용
SELECT ANIMAL_ID, NAME, 
    CASE 
        WHEN REGEXP_LIKE(SEX_UPON_INTAKE, 'Neutered|Spayed') THEN 'O'
        ELSE 'X'
    END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
