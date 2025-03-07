-- 코드를 입력하세요
SELECT p.product_code, sum(p.price * o.sales_amount) as sales
from PRODUCT p
join OFFLINE_SALE o on p.product_id = o.product_id
group by p.product_code
order by sales desc, p.product_code;