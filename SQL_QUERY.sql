CREATE DATABASE college_attendence;
USE college_attendence;
CREATE TABLE student(
student_id INT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
department VARCHAR(50),
year int);
CREATE TABLE subject(
sub_id int primary key,
subject_name varchar(100) not null);
CREATE TABLE attendance(
attendance_id int auto_increment PRIMARY KEY,
student_id INT,
subject_iD INT,
attendance_date DATE,
period INT,
status ENUM('PRESENT','ABSENT'),
FOREIGN KEY (student_id) REFERENCES student(student_id),
FOREIGN KEY (student_id) REFERENCES student(student_id),
UNIQUE (student_id,attendance_date,period));

INSERT INTO student 
(student_id,name,department,year)
VALUES
(101,'Ravi','CSE',2),
(102,'Ram','CAD',2),
(103,'Pretham','CSE',2),
(104,'Vishnu','CSE',3),
(105,'Revanth','CAD',2),
(106,'Nithin','CIVIL',4);

INSERT INTO subject
(sub_id,subject_name)
VALUES
(1,'Python'),
(2,'DBMS'),
(3,'ADSA'),
(4,'C++'),
(5,'English'),
(6,'Maths');
SHOW TABLES;
DROP TABLE attendence;