# Write your MySQL query statement below



select seller_id from (
select seller_id , rank () over(  order by sum(price) desc) rn1 from sales group by 1
) as t where t.rn1=1