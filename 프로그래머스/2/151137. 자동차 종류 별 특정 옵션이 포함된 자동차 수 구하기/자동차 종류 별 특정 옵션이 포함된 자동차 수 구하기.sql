-- 코드를 입력하세요
# MySQL 버전
# 정규표현식 사용
SELECT CAR_TYPE, COUNT(car_type) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS REGEXP '통풍시트|열선시트|가죽시트'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;

# LIKE 연산자 사용
SELECT CAR_TYPE, COUNT(car_type) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;


# Oracle 버전
# LIKE 연산자도 사용 가능
# 정규표현식 사용
SELECT CAR_TYPE, COUNT(car_type) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE REGEXP_LIKE(OPTIONS, '통풍시트|열선시트|가죽시트')
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;
