-- 4a. list last names of actors as well as how many actors have that last name
use sakila;
select last_name, count(last_name)
from sakila.actor
group by last_name;

-- 4b. list last names of actors and number of actors who have that last name, but only
-- for names that are shared by at least 2 actors
select last_name, count(last_name) 
from sakila.actor
group by last_name
having count(last_name) >=2;

-- 4c.  the actor 'harpo williams' was accidentally entered in 'actor' as 'groucho williams' - write query to fix
select * from sakila.actor
where first_name= 'groucho'
and 
last_name = 'williams';
-- actor id is 172 fro groucho williams
update actor
set first_name = 'HARPO'
where actor_id = 172;
select * from actor;

-- 4d.  in a single query, if the first name of the actor is 'harpo' change it to 'groucho'
select first_name 
from sakila.actor;
update	actor
set first_name = 'GROUCHO'
where actor_id = 172;
select * from actor
where actor_id = 172;
