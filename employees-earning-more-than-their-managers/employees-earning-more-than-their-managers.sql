# Write your MySQL query statement below


select p.name as Employee from  Employee  p left join employee q
on 
p.managerid=q.id
where
p.salary >q.salary
-- group by 1