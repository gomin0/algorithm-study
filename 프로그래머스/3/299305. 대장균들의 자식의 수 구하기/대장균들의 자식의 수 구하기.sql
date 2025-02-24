-- 코드를 작성해주세요
select e.ID, COALESCE(child_counts.CHILD_COUNT, 0) as CHILD_COUNT
from ecoli_data e
left join(
    select parent_id, count(*) as child_count
    from ecoli_data
    where parent_id is not null
    group by parent_id) child_counts
on e.id = child_counts.parent_id
order by e.id;