# Write your MySQL query statement below
select d.name as Department,t.name as Employee, Salary
from
( 
select name, DepartmentId , salary, rank() over( partition by DepartmentId  order by salary desc) rn1
from employee) as t
join Department d
on t.DepartmentId=d.id
where t.rn1=1