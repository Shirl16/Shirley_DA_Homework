use sakila;

-- 8a. create a view for step 7h (or substitute another query to create a view)
create view Sales_by_Genre as
select c.name as Genre, sum(p.amount) as Gross_Revenue
from 	category c
join		film_category f
on c.category_id = f.category_id
join		inventory i
on f.film_id = i.film_id
join 		rental r
on i.inventory_id = r.inventory_id
join 		payment p
on r.rental_id = p.rental_id
group by c.name
order by Gross_Revenue desc limit 5;

-- 8b. how would you display the view in 8a?
show create view sakila.Sales_by_Genre;
select * from Sales_by_Genre;

-- 8c. write a query to delete the top_five_genres
drop view Sales_by_Genre;



