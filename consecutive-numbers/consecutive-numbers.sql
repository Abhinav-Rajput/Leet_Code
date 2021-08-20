# Write your MySQL query statement below

select num ConsecutiveNums from (
select lag(num) over(order by id) lag_num, num, lead(num) over(order by id) lead_num from logs
    )as t 
    where t.lag_num=t.num and t.num=t.lead_num
    group by 1