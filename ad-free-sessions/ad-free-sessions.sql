# Write your MySQL query statement below
# select session_id from playback p  left join ads  a on
# p.customer_id = a.customer_id
# where a.timestamp not  between start_time and end_time
# group by 1


SELECT session_id
FROM 
    Playback 
    LEFT JOIN Ads 
    ON Playback.customer_id = Ads.customer_id AND timestamp BETWEEN start_time AND end_time 
WHERE Ads.customer_id IS NULL