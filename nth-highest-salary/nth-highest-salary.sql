CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      
      select salary from (
      select salary , dense_rank() over( order by salary desc) rn1 from employee
      ) as t where t.rn1=n
      group by 1
      
  );
END