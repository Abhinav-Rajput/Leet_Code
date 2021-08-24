# Write your MySQL query statement below


with cte1 as(

    select year, Wimbledon as player_id from Championships 
    union all
    select year ,Fr_open from Championships
    union all
     select year ,US_open  from Championships
    union all
    select year ,AU_open  from Championships
)
select p.player_id ,p.player_name , count(*) grand_slams_count   from cte1
join Players p
on p.player_id=cte1.player_id
group by 1