# Write your MySQL query statement below

select  product_id, year first_year , quantity , price from ( 
select product_id, year, quantity , price, rank() over(partition by product_id order by year) rn1 from sales 
    ) as t
    where t.rn1=1