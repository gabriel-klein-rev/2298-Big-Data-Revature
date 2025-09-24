create database grade_book;
use grade_book;
create table if not exists students(
    id int primary key,
    name varchar(40) not null unique
);
create table if not exists evals (
    id int primary key,
    studentId int not null,
    evalName varchar(10) not null,
    mark int default 0,
    foreign key(studentId) references students(id),
    constraint mark_check check(mark >= 0), check(mark <= 100)
);

insert into students (id, name) values (1, 'Steve'), (2, 'Jane'), (3, 'Casey');
insert into evals (id, studentId, evalName, mark) values (1, 1, 'quiz 1', 98), (2, 2, 'quiz 1', 80), (3, 3, 'quiz 1', 95), (4, 1, 'test 1', 72), (5, 2, 'test 1', 100), (6, 3, 'test 1', 68);