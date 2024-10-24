-- 데이터베이스 목록 조회
show databases; 

-- 작업 데이터베이스 선택(변경)
use bookstore;

-- 테이블 목록 조회
show tables;

-- 테이블 구조 조회
desc book;


-- 모든 도서 조회
select bookid, bookname, publisher, price
from book;

select *
from book;

-- 모든 도서의 도서명, 출판사, 가격 조회
select bookname, publisher, price
from book;

-- 출판사 조회 ( 중복 제거 )
-- select publisher
select distinct publisher
from book;

-- 대한미디어에서 출간한 도서 조회
select *
from book
where publisher = '대한미디어';

-- 대한미디어에서 출간한 가격이 30000 이상인 도서 조회
select *
from book
where publisher = '대한미디어' and price >= 30000;

-- 가격이 20000 ~ 30000인 도서 조회 1
select *
from book
where price >= 20000 and price <= 30000;

-- 가격이 20000 ~ 30000인 도서 조회 2
select *
from book
where price between 20000 and 30000;

-- 가격이 20000 이하 또는 30000 이상인 도서 조회 1
select *
from book
where price <= 20000 or price >= 30000;

-- 가격이 20000 이하 또는 30000 이상인 도서 조회 2
select *
from book
where price not between 20000 and 30000;

-- 도서를 가격순으로 조회 (낮은 가격 -> 높은 가격)
select *
from book
order by price; -- asc 생략 : 오름차순 정렬

-- 도서를 가격순으로 조회 (높은 가격 -> 낮은 가격)
select *
from book
order by price desc; -- desc : 내림차순 정렬

-- 도서를 출판사 및 가격순으로 조회
select *
from book
order by publisher asc, price desc;

-- 주문 데이터 조회
select *
from orders;

-- 매출액 조회 (주문 총액)
select sum(saleprice) as "주문 총액"
from orders;

select 
	sum(saleprice) as "구매 총액",
	avg(saleprice) as "구매 평균",
    max(saleprice) as "최고구매액",
    min(saleprice) as "최소구매액",
    count(saleprice) as "구매건수"
from orders;

-- 고객별 구매액 (총액, 평균) 조회
select 
	custid,
	sum(saleprice) "총구매액",
	avg(saleprice) "평균구매액"
from orders
group by custid;

-- 고객별 구매액 (총액, 평균) 조회
select 
	custid,
	sum(saleprice) "총구매액",
	avg(saleprice) "평균구매액"
from orders
-- where sum(saleprice) >= 30000
group by custid
having sum(saleprice) >= 30000;

-- 축구 관련 도서 조회
select *
from book
-- where title = '축구';
where bookname like '%축구%';

--  전화번호를 등록하지 않은 고객 조회
select * 
from customer
-- where phone = NULL;
where phone IS NULL;









