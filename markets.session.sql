-- SELECT Count(DISTINCT product_type_id) from globus;

SELECT product_name, sum(product_amount) from narodnii
where day_to_expire < 2
group by product_name;

-- select sum() from globus
-- Select sum(product_amount)
-- from narodnii
-- where product_name = 'Snikers'
-- UNION
-- Select sum(product_amount)
-- from globus
-- where product_name = 'Snikers';
-- having day_to_expire < 2;
-- having day_to_expire < 1;