# Write your MySQL query statement below

select Name from Employee where id in
(
select ManagerId from Employee 
where ManagerId is not null  group by 1
having   count(id) >=5)