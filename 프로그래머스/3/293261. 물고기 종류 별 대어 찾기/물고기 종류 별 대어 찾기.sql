-- 코드를 작성해주세요
select fi.id, fni.fish_name, fi.length
from fish_info fi
join (
    select fish_type, max(length) as max_length
    from fish_info
    group by fish_type
) max_fish on fi.fish_type = max_fish.fish_type and fi.LENGTH = max_fish.MAX_LENGTH
join fish_name_info fni on fi.fish_type = fni.fish_type
order by fi.id;