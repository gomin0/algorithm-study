-- 코드를 작성해주세요
select e1.id, e2.size
from ecoli_data e1
join (
    select id,
    case
        when SIZE_OF_COLONY <= 100 then 'LOW'
        when SIZE_OF_COLONY > 1000 then 'HIGH'
        else 'MEDIUM'
    end as size
    from ecoli_data) e2
on e1.id = e2.id
order by e1.id;