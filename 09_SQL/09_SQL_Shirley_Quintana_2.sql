-- 2a. find the ID #, first, last name of an actor you know only by the first name, "Joe".
-- what query would you run to find this actor? (results=1 row)
use sakila;
select * from sakila.actor
where first_name like '%Joe%';

-- 2b. find all actors whose last name contains the letters 'gen' (results=4 rows)
select * from sakila.actor
where last_name like '%gen%';

-- 2c. find all actors whose last names contain the letters 'LI', this time order the rows by last name / first name
-- results returned 10 rows 
select * from sakila.actor
where last_name like '%li%' 
order by last_name, first_name;

-- 2d. using 'IN', display the country id and country columns of the following countries:
-- afghanistan, bangladesh, and china
select country_id, country from sakila.country
where country in ('Afghanistan', 'Bangladesh', 'China');