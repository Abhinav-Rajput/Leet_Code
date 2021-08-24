# Write your MySQL query statement below



with cte as (
select customer_id, product_id, rank() over(partition by customer_id order by count(*) desc) as frequency
from orders
group by 1,2)

select c.customer_id, c.product_id, p.product_name
from cte c join products p
on c.product_id=p.product_id
where frequency=1;