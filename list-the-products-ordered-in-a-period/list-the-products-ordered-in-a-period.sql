# Write your MySQL query statement below



select  product_name,  unit from products p
 join
(select product_id, sum(unit) unit from orders  where left(order_Date,7)='2020-02' group by 1
having  sum(unit) >=100) as b
on p.product_id=b.product_id
group by 1,2