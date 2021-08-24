# Write your MySQL query statement below


select case when from_id < to_id then from_id 
            when from_id>to_id then to_id end as person1,
case when from_id > to_id then from_id 
            when from_id<to_id then to_id end as person2, count(*) as call_count,
            sum(duration) total_duration 
            from calls
            group by 1,2