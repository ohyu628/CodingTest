-- 코드를 입력하세요
# MySQL 버전
# 날짜 형식을 그대로 사용하면 산술 형식으로 계산되어 따옴표를 꼭 써줘야 함
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE,"%Y-%m-%d") AS OUT_DATE,
    CASE
        WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
        WHEN OUT_DATE >= '2022-05-01' THEN '출고대기'
        WHEN OUT_DATE IS NULL THEN '출고미정'
    END AS "출고여부"
FROM FOOD_ORDER
ORDER BY ORDER_ID;

# Oracle 버전
