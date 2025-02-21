-- 코드를 입력하세요
SELECT car_id, if(sum(case when START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16' then 1 else 0 end) > 0, '대여중', '대여 가능') as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc;