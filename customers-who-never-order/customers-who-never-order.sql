# Write your MySQL query statement below

select name as `Customers` from customers c left join Orders o on
c.id=o.CustomerId
where o.CustomerId is null
-- group by 1