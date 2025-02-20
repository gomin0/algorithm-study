-- 코드를 입력하세요
SELECT u.user_id, u.nickname, sum(b.price) as total_sales
from USED_GOODS_USER u
join USED_GOODS_BOARD b on u.user_id = b.writer_id
where b.status = 'DONE'
group by u.user_id
having total_sales >= 700000
order by total_sales