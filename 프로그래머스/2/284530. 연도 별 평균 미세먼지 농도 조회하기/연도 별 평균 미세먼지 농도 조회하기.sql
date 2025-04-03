-- 코드를 작성해주세요
# MySQL 버전
# ROUND(열이름, 자릿수) -> 반올림 함수로 소수는 양수, 정수는 음수로 표현
# 별칭 사용 시 .이 있을 경우 ''를 사용해야함
SElECT YEAR(YM) AS YEAR, ROUND(AVG(PM_VAL1),2) AS PM10, ROUND(AVG(PM_VAL2),2) AS 'PM2.5'
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY YEAR(YM)
ORDER BY YEAR;

# Oracle 버전
# 별칭 사용 시 .이 있을 경우 ""를 사용해야함
SELECT TO_CHAR(YM, 'YYYY') AS YEAR, ROUND(AVG(PM_VAL1), 2) AS PM10, ROUND(AVG(PM_VAL2), 2) AS "PM2.5"
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY TO_CHAR(YM, 'YYYY')
ORDER BY 1;
