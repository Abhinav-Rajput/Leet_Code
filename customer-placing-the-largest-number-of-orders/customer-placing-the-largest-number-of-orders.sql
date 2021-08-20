# Write your MySQL query statement below

select customer_number from( 
select customer_number ,rank() over(order by count(*) desc)rn1 from orders group by 1
    )as t where t.rn1=1