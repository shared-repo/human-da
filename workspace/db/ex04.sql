-- 작업 데이터베이스 변경
use bookstore;

-- 박지성 고객의 구매이력
select * from customer;
select * from orders;

select c.name, o.*
from orders o, customer c
where o.custid = c.custid  	-- join 조건
	  and 
      c.name = '박지성';		-- 일반 조건
      
select c.name, o.*
from orders o
inner join customer c
on o.custid = c.custid  	-- join 조건
where c.name = '박지성';		-- 일반 조건

