select f.flavor
from first_half as f
join (
    select flavor, sum(total_order) as july_total_order
    from july as j
    group by flavor
) as j
on f.flavor = j.flavor
order by (f.total_order + j.july_total_order) desc
limit 3;