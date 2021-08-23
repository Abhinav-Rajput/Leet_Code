# Write your MySQL query statement below



#1   CTE method
with t1 as (
    select employee_id 
    from employees
    where manager_id = 1
),

t2 as (
    select employees.employee_id
    from employees, t1
    where manager_id = t1.employee_id
)

select distinct employees.employee_id
from employees,t2
where manager_id = t2.employee_id and employees.employee_id != 1;




#2  sub-query method
#  select employee_id from employees where manager_id in (
#  select employee_id from employees where manager_id in (
# select employee_id from employees where manager_id = 1
#  )
# ) 
# and employee_id <> 1
# ;


#3   left join method
# select e.employee_id
# from employees e
# left join employees m1
#     on e.manager_id = m1.employee_id
# left join employees m2
#     on m1.manager_id = m2.employee_id
# left join employees m3
#     on m2.manager_id = m3.employee_id
# where least(m1.employee_id, m2.employee_id, m3.employee_id) = 1
#     and e.employee_id != 1
;