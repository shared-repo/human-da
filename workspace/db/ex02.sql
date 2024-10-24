-- 판매가격이 8,000원 이상인 도서를 구매한 고객에 대하여 고객별 주문 도서의 총 수량을 구하시오.  
-- 단, 두 권 이상 구매한 고객만 구한다
select custid, count(custid)
from orders
where saleprice >= 8000
group by custid
having count(custid) >= 2;

select * from book where bookid in(1, 6, 10);
select * from orders where saleprice <8000;

-- 박지성의 총 구매액
select custid 
from customer where name = '박지성'; -- '박지성' 고객의 custid 찾기

select '박지성' 고객, sum(saleprice) 구매액 
from orders 
where custid = 1;

-- 박지성이 구매한 도서의 수
select count(*) from orders where custid = 1;

-- 도서의 총 개수
select count(*) from book;

-- 도서를 출고하는 출판사의 총 개수
select count(distinct publisher) from book;
