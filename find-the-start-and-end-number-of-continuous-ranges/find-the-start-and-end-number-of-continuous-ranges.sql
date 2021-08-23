# Write your MySQL query statement below


select 
    min(log_id) as start_id,
    max(log_id) as end_id
    from
    (select 
        log_id,
        log_id - row_number() over (order by log_id) as diff
    from logs) a
    group by a.diff 
    
    
    
    
#     with temp as
# (
# select 
# log_id,
# log_id - row_number() over(order by log_id) grp
# from Logs
# )
# select
# min(log_id) start_id,
# max(log_id) end_id
# from temp
# group by temp.grp


# with ff as
# (
#     select log_id,log_id - dense_rank() over (order by log_id)rnk
#     from logs
# )
# select min(log_id) as start_id,max(log_id) as end_id
# from ff group by rnk