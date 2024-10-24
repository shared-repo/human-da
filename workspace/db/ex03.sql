-- 작업 데이터베이스 변경
use bookstore;

-- 박지성 고객의 총 구매액
select '박지성' 고객, sum(saleprice) 구매액 
from orders 
where custid = (select custid 
				from customer 
                where name = '박지성');
                
-- 구매이력이 있는 고객 정보 조회
select *
from customer
-- where custid in (1, 2, 3, 4);
where custid in (select distinct custid 
				 from orders);
            
-- book과 imported_book 테이블에 있는 도서 갯수 조회 1
select count(*)
from
(
	select * from book
	union all
	select * from imported_book
) a;

-- book과 imported_book 테이블에 있는 도서 갯수 조회 2
select 
	(select count(*) from book) + 
    (select count(*) from imported_book) 도서갯수;


