-- 작업 데이터베이스 변경

use bookstore;

desc book;

-- 데이터 삽입 (생성)
insert into book (bookid, bookname, publisher, price)
values (101, '혼자 공부하는 데이터 분석', '한빛미디어', 26000);

select * from book;

-- 데이터 삽입 (생성) 2
insert into book
values (102, '혼자 공부하는 머신러닝', '한빛미디어', 26000);
select * from book;

-- 데이터 삽입 (생성) 3
insert into book (bookid, bookname)
values (103, '수학으로 만드는 기초 AI');
select * from book order by bookid desc;

-- 데이터 삽입 (생성) 4
insert into book (bookid, bookname)
values 	(104, '신규 도서 4'),
		(105, '신규 도서 5'),
		(106, '신규 도서 6'),
		(107, '신규 도서 7'),
		(108, '신규 도서 8');
select * from book order by bookid desc;

-- 데이터 삽입 (생성) 5
insert into book (bookid, bookname)
values (109, '삽입 실패 도서1111111111111111111111111111111111111111111111111111111111111111111111111111111');
select * from book order by bookid desc;

-- 데이터 수정 1
update book
set price = 50000;

select * from book;

-- 데이터 수정 2
update book
set price = 70000
where bookid > 100;

select * from book;

-- 데이터 수정 3
update book
set price = 80000, bookname = '수정된 도서'
where bookid = 101;

select * from book order by bookid desc;

-- 데이터 삭제
delete from book
where bookid > 100;

select * from book order by bookid desc;

-- ---------------

-- 테이블 만들기 : book2 이름으로 book과 유사하게
create table book2
(
	bookid integer primary key auto_increment,
    bookname varchar(100) not null,
    publisher varchar(100) not null,
    price integer not null,
    pubdate date not null,
    regdate datetime default (now())
);

create table customer2
(
	custid integer auto_increment,
    name varchar(50) not null,
    address varchar(100) null,
    phone varchar(20) null,
   
    -- primary key (custid)
    constraint pk_customer2 primary key (custid)
);

create table orders2
(
	orderid integer auto_increment,
    custid integer not null,
    bookid integer not null,
    saleprice integer not null,
    orderdate date not null,
    
    constraint pk_orders2 primary key (orderid),
    constraint fk_orders2_customer2 foreign key (custid) references customer2(custid),
    constraint fk_orders2_book2 foreign key (bookid) references book2(bookid)
);

-- 테이블 수정

desc book2;
alter table book2
add isbn char(13) null;
desc book2;

alter table book2
modify isbn varchar(50) null;
desc book2;

alter table book2
drop column isbn;
desc book2;

--  테이블 삭제 - 자식이 있는 부모테이블 삭제 불가
drop table book2;

--  테이블 삭제 2
drop table orders2;
drop table book2;
drop table customer2;

-- 
-- 테이블 만들기 : member
-- 컬럼 : memberId(문자열, 20, pk), 
-- 	passwd(문자열, 100, not null)
-- 	email(문자열, 100, not null), 
-- 	usertype(문자열, 기본값:user), 
-- 	deleted(boolean, 기본값:false), 
-- 	regdate(날짜, 기본값:now())


-- 테이블 만들기 : board
-- 컬럼 : boardno(숫자, pk, 자동증가), 
-- 	title(문자열, 100, not null)
-- 	content(문자열, 2000, not null), 
-- 	writer(문자열, 20, 외래키-member의 memberid 참조), 
-- 	deleted(boolean, 기본값:false), 
-- 	regdate(날짜, 기본값:now())
    
-- member 테이블에 데이터 삽입
-- board 테이블에 데이터 삽입

create table member
(
	memberid varchar(20) primary key,
	passwd varchar(100) not null,
	email varchar(100) not null,
	usertype varchar(20) default('user'),
	deleted boolean default(false),
	regdate date default(now())
);

create table board
(
	boardno integer primary key auto_increment,
	title varchar(100) not null,
	content varchar (2000) not null,
	writer varchar(20) not null,
	deleted boolean default (false),
	regdate date default (now()),
	constraint fk_board_member foreign key (writer) references member(memberid)
);

insert into member (memberid, passwd, email) values('johndoe', 'iamuserone', 'iamuserone@example.com');
insert into board (title, content, writer) values ('첫 번째 게시글', '처음 쓰는 게시글 연습', 'johndoe');

select * from member;
select * from board;






