create database practice;
create table prog_stu(
student_name  varchar(100),
courses    varchar(20),
marks   int,
attendence  varchar(10),
depart   varchar(20));
insert into prog_stu(student_name,courses,marks,attendence,depart)
values
('Ravi','Maths',90,'Present','CAD'),
('Ram','Maths',92,'Present','CAD'),
('Revanth','Maths',85,'Present','CAD'),
('Pretham','Maths',80,'Present','CAD'),
('Likith','Science',0,'Absent','CAD'),
('Navadeep','Sciencce',0,'Absent','CAD');





select * from prog_stu;
select courses,attendence from prog_stu;
select courses,student_name from prog_stu
where attendence = 'Absent';

