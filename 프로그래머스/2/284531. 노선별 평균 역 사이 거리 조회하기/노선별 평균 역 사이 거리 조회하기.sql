-- 코드를 작성해주세요
# MySQL 버전
# ROUND(열, 1) -> 소수점 첫째자리까지 표시, 둘째자리에서 반올림
# TOTAL_DISTANCE은 km가 붙어있기 때문에 정렬이 이상하게 됨
SELECT ROUTE, CONCAT(ROUND(SUM(D_BETWEEN_DIST),1),'km') AS TOTAL_DISTANCE, CONCAT(ROUND(AVG(D_BETWEEN_DIST),2),'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY SUM(D_BETWEEN_DIST) DESC;
