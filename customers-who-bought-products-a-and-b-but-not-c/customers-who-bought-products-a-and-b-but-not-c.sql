# Write your MySQL query statement below


select customer_id , customer_name  from customers where customer_id in(
select customer_id   from Orders where  product_name in('A','B')  and customer_id not in (select customer_id from orders where product_name ='C' )
    group by 1
    having count(distinct product_name  )>=2


 ) 