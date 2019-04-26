-- 7a. use subqueries to display titles of movies starting with k and q whose language is english
use sakila;
select title from film
where language_id in
(
	select language_id
    from language
    where name = 'english'
    )
    and title like 'k%' 
    or title like 'q%';


-- 7b. use subqueries to display all actors who appear in the film 'alone trip'
select first_name, last_name
from actor
where actor_id in
(
	select actor_id
	from film_actor
	where film_id in
(
	select film_id
    from film
    where title = 'alone trip'
   )
   );


-- 7c. use joins to retrieve canadian customers names and email addresses
SELECT cus.first_name, cus.last_name, cus.email, ctr.country
FROM customer cus
INNER JOIN address a
ON (cus.address_id = a.address_id)
INNER JOIN city cit
ON (a.city_id = cit.city_id)
INNER JOIN country ctr
ON (cit.country_id = ctr.country_id)
WHERE ctr.country = 'canada';


-- 7d. identify all movies categorized as family films
select title
from film
where film_id in
(
select fc.film_id
from film_category fc, category cat
    where cat.name = 'family'
    and fc.category_id = cat.category_id
    );


-- 7e. display the most frequently rented movies in descending order
SELECT inv.film_id, film.title, count(*) as num_rentals
from rental r,
		inventory inv,
        film
where 
			r.inventory_id = inv.inventory_id
and
			inv.film_id = film.film_id
group by inv.film_id, film.title
order by num_rentals desc;


-- 7f. write a query to display how much business, in dollars, each store brought in
select cust.store_id, sum(pmt.amount) as store_sales 
from customer cust,
		 payment pmt
where cust.customer_id = pmt.customer_id
group by cust.store_id;


-- 7g. write a query to display for each store its store ID, city, and country
select cust.store_id, city.city, country.country
from customer cust
join address a
on cust.address_id = a.address_id
join city
on a.city_id = city.city_id
join country 
on city.country_id = country.country_id;

-- 7h. list the top 5 genres in gross revenue in descending order (use category, film_category, inventory, payment, rental tables)
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














