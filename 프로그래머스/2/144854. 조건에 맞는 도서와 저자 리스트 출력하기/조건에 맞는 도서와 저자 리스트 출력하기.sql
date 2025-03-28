-- 코드를 입력하세요
# MySQL 버전
SELECT a.BOOK_ID, b.AUTHOR_NAME, DATE_FORMAT(a.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK AS a LEFT OUTER JOIN AUTHOR AS b ON a.AUTHOR_ID = b.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE ASC;

# Oracle 버전
SELECT a.BOOK_ID, b.AUTHOR_NAME, TO_CHAR(a.PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM BOOK a JOIN AUTHOR b ON a.AUTHOR_ID = b.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE;
