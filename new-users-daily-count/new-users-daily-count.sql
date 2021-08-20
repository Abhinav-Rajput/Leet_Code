# Write your MySQL query statement below

# ----------  first try
# with t1 as(
# select user_id, min(activity_date) first_login_date from traffic
#     where activity='login' group by 1
# )

# select activity_date login_date , count(user_id) user_count from
# traffic where (user_id,activity_date) in (select user_id,first_login_date from t1 where first_login_date>'2019-03-30' )and activity='login'  and
# activity_date between '2019-03-30' and '2019-06-30'
# group by 1
#order by 1





with cte as 
    (
    select user_id, min(activity_date) as login_date
    from Traffic
    where activity = 'login'
    group by user_id
    )

select login_date, count(user_id) as user_count
from cte
where datediff('2019-06-30', login_date) <= 90
group by login_date
order by login_date


# select date login_date , count(user_id) user_count
# from
# (select user_id, min(activity_date) date
# from traffic 
# where activity="login"
# group by user_id
# ) a
# where timestampdiff(day, date, "2019-06-30")<=90
# group by 1
# order by 1