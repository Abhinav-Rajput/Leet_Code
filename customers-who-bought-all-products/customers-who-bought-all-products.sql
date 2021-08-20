# Write your MySQL query statement below

with t1 as(
select count(product_key) as total_products from product
)

select customer_id from customer
group by 1
having count(distinct product_key)>=(select total_products from t1)