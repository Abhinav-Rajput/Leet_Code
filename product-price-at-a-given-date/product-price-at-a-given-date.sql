# Write your MySQL query statement below





# select p.product_id, ifnull(new_price, 10) price from products p left join

# (select product_id , max(change_date) c_date from products where change_date<='2019-08-16'  group by 1) as b
# on p.product_id =b.product_id;


select product_id , 10 as price from products where (product_id)  in 
(select product_id from products group by 1 
 having min(change_date)>'2019-08-16'
)
union 
select product_id , new_price  as price from products where (product_id)  in 
(select product_id from products group by 1 
 having min(change_date)<='2019-08-16'
)
and change_date<='2019-08-16'
and (product_id, change_date) in 
(select product_id , max(change_date) c_date from products where change_date<='2019-08-16'  group by 1)
group by 1,2
 order by 1
