# Write your MySQL query statement below


select Department , Employee, Salary  from(
select  e.name as Employee, d.name as Department, salary, dense_rank() over( partition by e.DepartmentId  order by salary desc) rn1 from employee e join  department d on
    e.DepartmentId = d.id

)as t
where t.rn1<=3