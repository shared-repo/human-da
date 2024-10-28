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

-- 고객과 고객의 주문에 정보 조회
select c.custid, c.name, o.bookid, o.saleprice, o.orderdate
from customer c
inner join orders o
on c.custid = o.custid
order by c.custid;

-- 고객과 고객의 주문 정보 조회 + 도서 이름
select c.custid, c.name, b.bookid, b.bookname, o.saleprice, o.orderdate
from customer c
inner join orders o
on c.custid = o.custid
inner join book b
on o.bookid = b.bookid
order by c.custid;

-- cross join
select *
from customer c
cross join orders o
order by c.custid;

-- 고객별 주문 총액 조회 (고객 이름 표시)
select c.custid, c.name, ifnull(sum(o.saleprice), 0) 주문총액
from customer c
-- inner join orders o
left outer join orders o
on c.custid = o.custid
group by c.custid, c.name
order by c.custid;

-- ------------------------------------------

-- subquery 또는 join을 사용해서 아래에 해당하는 sql을 작성하세요

-- 가장 비싼 도서의 이름을 보이시오
select bookname, max(price)
from book
group by bookname;

select max(price) from book; -- 최고가격

select *
from book
-- where price = 최고가격;
where price = ( select max(price) from book );

-- 도서를 구매한 적이 있는 고객의 이름을 검색하시오
select *
from customer c 
where c.custid in ( select distinct o.custid from orders o );

select distinct c.*
from customer c
inner join orders o
on c.custid = o.custid;

-- 대한미디어에서 출판한 도서를 구매한 고객의 이름을 보이시오
select *
from customer c
inner join orders o
on c.custid = o.custid 
where o.bookid in ( select bookid 
                    from book 
                    where publisher = '대한미디어' );









