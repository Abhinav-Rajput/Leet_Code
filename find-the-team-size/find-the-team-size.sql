# Write your MySQL query statement below


# lesson here is, you don't want to calculate cummulative sum/count and to do that, just use partition by 

select employee_id , count(employee_id) over( partition by team_id ) team_size
from employee
group by 1
order by 1;



