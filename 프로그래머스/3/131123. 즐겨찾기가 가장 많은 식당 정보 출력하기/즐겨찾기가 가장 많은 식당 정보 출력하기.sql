-- 코드를 입력하세요
SELECT ri.food_type, ri.rest_id, ri.rest_name, ri.favorites
from rest_info ri
join(
    select food_type, max(favorites) as max_favorites
    from rest_info
    group by food_type
) max_rest on max_rest.food_type = ri.food_type and ri.favorites = max_rest.max_favorites
order by food_type desc