# Write your MySQL query statement below


select num as ConsecutiveNums  from
(
select lag(num,1) over(order by id) lag_num, num, lead(num,1) over(order by id) lead_num from logs
    
)as t
where lag_num=num and num=lead_num
group by 1