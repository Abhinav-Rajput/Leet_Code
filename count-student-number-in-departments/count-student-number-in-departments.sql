# Write your MySQL query statement below

select dept_name , count(student_id ) student_number   from department  d left join
student s on
s.dept_id =d.dept_id 
group by 1 order by 2 desc, 1