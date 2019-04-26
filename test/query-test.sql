-- Created data in mysql to confirm the results
-- SQL my yield different results in different type of database e.g. sqlite


-- 1. List the stores allowed to sell alcohol
select name from interview.stores where allowed_alcohol = 1;

-- 2. Give the product name of the 2 most expensive items based on their price at store id 1
select prd.name from interview.store_prices sp, interview.products prd
    where sp.store_id = 1 and sp.product_id = prd.id
    group by sp.price order by sp.price desc limit 2;

-- 3. List the products that are not sold in the store id 2
select name from interview.products where id not in (select product_id from interview.order_lines where store_id = 2);

-- 4. What is the most popular item sold?
select name from interview.products p, (select product_id, count(*) qty from interview.order_lines group by product_id order by qty desc limit 1) temp
    where p.id = temp.product_id ;

with temp as (
    select product_id, count(*) qty
        from interview.order_lines
        group by product_id
        order by qty desc limit 1
        )
    select p.name from temp, interview.products p where temp.product_id = p.id;

-- 5. Write a SQL statement to update the line_total field
update interview.order_lines set line_total = 44.54;