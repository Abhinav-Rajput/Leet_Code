# Write your MySQL query statement below

select name,ifnull(travelled_distance,0)travelled_distance  from users as a left join
(select user_id, sum(distance) as travelled_distance  from rides group by 1) as b
on a.id=b.user_id
group by 1,2
order by 2 desc,1