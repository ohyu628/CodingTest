-- 코드를 작성해주세요
# 함수 사용
SELECT ROUND(AVG(IFNULL(LENGTH, 10)),2) AS AVERAGE_LENGTH
FROM FISH_INFO;

# CASE문 사용
SELECT ROUND(AGV(CASE
  WHEN LENGTH IS NULL THEN 10
  ELSE LENGTH END),2) AS AVERAGE_LENGTH
FROM FISH_INFO;
