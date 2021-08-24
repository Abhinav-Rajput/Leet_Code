# Write your MySQL query statement below


#select  visited_on, sum(amount) over(order by  visited_on) amount, avg(amount) over (order by  visited_on) average_amount 
#from Customer;


SELECT visited_on, amount, average_amount FROM
(SELECT visited_on, 
SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as amount,
ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) as average_amount,
ROW_NUMBER() OVER (ORDER BY visited_on) as row_num
FROM 
(
   SELECT visited_on, SUM(amount) AS amount FROM Customer group by 1
) a
ORDER BY 1) result
WHERE row_num >= 7;