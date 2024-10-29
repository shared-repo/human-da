-- 작업 데이터베이스 변경
use bookstore;

drop table inc_test;

create table inc_test
(
	idx integer primary key auto_increment,
    c1 varchar(100)
);

insert into inc_test (c1) values('test 1');
insert into inc_test (c1) values('test 2');
insert into inc_test (c1) values('test 3');
insert into inc_test (c1) values('test 4');

select * from inc_test;

-- --------------------------------------------

-- 자기참조테이블 : FK가 같은 테이블의 PK를 참조하는 경우

drop table employees;
CREATE TABLE employees ( 
    employee_id INT PRIMARY KEY, 
    employee_name VARCHAR(50), 
    manager_id INT, 
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id) 
); 

INSERT INTO employees VALUES (1, 'John', NULL); 
INSERT INTO employees VALUES (2, 'Jane', 1); 
INSERT INTO employees VALUES (3, 'Bob', 2); 
INSERT INTO employees VALUES (4, 'Alice', 1); 
INSERT INTO employees VALUES (5, 'Charlie', 3); 

select * from employees;

-- 사원 정보 조회 : 아이디, 이름, 매니저이름
select e1.employee_id, e1.employee_name, e2.employee_name
from employees e1 				-- employee table
left outer join employees e2 	-- manager table
on e1.manager_id = e2.employee_id;



