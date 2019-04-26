-- 6a. use join to display the first and last names, addresses, of each staff member - use staff and address tables
use sakila;
select staff.first_name, staff.last_name, staff.address_id, address.address_id, address.address, address.address2 
from staff
join address on 
staff.address_id = address.address_id;

-- 6b. use join to display the total amount rung up by each staff member in August 2005, use staff and payment tables
-- total for #1 = 11,853.65 & #2 = 12,218.48
select 	staff.staff_id, staff.first_name, staff.last_name, payment.staff_id, 
			sum(payment.amount) as total_sales
from payment
join staff on
payment.staff_id = staff.staff_id
where 
 	payment.payment_date >=(20050801) 
and
	payment.payment_date <(20050830)
group by staff.staff_id;

--  6c. list each film and number of actors who are listed for that film; use film_actor and film tables (inner join)
select 	film.title,
			count(film_actor.actor_id) as num_actors_in_film
from film
join 	film_actor on
		film.film_id = film_actor.actor_id
group by film.title;

-- 6d. how man copies of the film 'hunchback impossible' exist in the inventory system?
select title, film_id from film
where title = 'hunchback impossible';

select film_id, count(film_id) 
from inventory
where film_id = 439;

-- 6e. use tables payment and customer and the join command to list total paid by each customer. 
-- list customers alphabetically by last name
select 	customer.first_name, customer.last_name, 
			sum(payment.amount) as total_amount_paid
from customer
join payment on
customer.customer_id = payment.customer_id
group by customer.customer_id
order by customer.last_name asc;