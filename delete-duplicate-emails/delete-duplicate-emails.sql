# Write your MySQL query statement below

delete from person
where id in (
select id from (
select id, email,row_number() over(partition by email order by id) rn1 from person
)as t
    where t.rn1>1
)