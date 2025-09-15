# Write your MySQL query statement below
# ROW_NUMBER() OVER (PARTITION BY product_category ORDER BY revenue DESC) AS rank
# dense_rank() OVER (PARTITION BY product_category ORDER BY revenue DESC) AS rank
with base as (
    select b.name as Department, a.name as Employee, dense_rank() over (partition by b.name order by a.salary desc) as salary_rank, a.salary as Salary
    from Employee a
    left join Department b
    on a.departmentId = b.id
    )
select Department, Employee, Salary 
from base 
where salary_rank < 4