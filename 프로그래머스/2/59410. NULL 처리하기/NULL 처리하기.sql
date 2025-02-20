-- 코드를 입력하세요
SELECT animal_type, if(name is null, 'No name', name), sex_upon_intake
from ANIMAL_INS
order by animal_id;