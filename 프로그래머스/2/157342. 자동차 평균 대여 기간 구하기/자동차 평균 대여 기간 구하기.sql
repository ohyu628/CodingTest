-- 코드를 입력하세요
# MySQL 버전
# 대여일은 시작 날도 포함해야 하기 때문에 날짜 간의 차이 + 1을 해줘야함
SELECT CAR_ID, ROUND(AVG(TIMESTAMPDIFF(DAY, START_DATE, END_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVG(TIMESTAMPDIFF(DAY, START_DATE, END_DATE)+1) >= 7
ORDER BY 2 DESC, 1 DESC;

# Oracle 버전
