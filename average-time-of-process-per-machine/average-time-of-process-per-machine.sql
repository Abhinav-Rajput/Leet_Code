# Write your MySQL query statement below


select machine_id,round(avg(processing_time),3)processing_time from ( 
select machine_id , process_id ,sum(case when activity_type='start' then -timestamp 
                                   when activity_type='end' then timestamp end) as processing_time
    from Activity 
                                   group by 1,2) as t
                                   group by 1