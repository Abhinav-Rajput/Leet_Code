# Write your MySQL query statement below

-- -  1st try
# select Name, mail from  users where user_id in(
# select gold_medal from contests group by 1
#     having count(distinct contest_id) >=3
# )
# group by 1,2
# union 

# SELECT user_id ,COUNT(*) cnt FROM
# (
#     SELECT gold_medal  as user_id FROM contests UNION ALL
#     SELECT silver_medal  FROM contests UNION ALL  
#     SELECT bronze_medal FROM contests UNION ALL 
   
# )k
# GROUP BY user_id
# having


# )

with cte1 as(
select contest_id, gold_medal as candidates from contests union All
    select contest_id, silver_medal as candidates from
    contests union all
select contest_id, bronze_medal as candidates from
    contests 
 ),
 cte2 as (
select candidates from cte1 where (contest_id-1,candidates) in (select * from cte1)
and (contest_id+1,candidates) in (select * from cte1)
group by 1),

cte3 as(
select gold_medal as candidates  from contests
    group by 1 having count(*) >=3)
    
    select name, mail from users 
where user_id in (
select * from cte2
    union
select * from cte3
)