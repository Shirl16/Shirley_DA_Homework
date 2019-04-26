-- 1a. display first and last names of all actors from actor table
-- 1b. display the names of each actor in a single column called 'Actor Name'
-- all in upper case
use sakila;
select * from sakila.actor;
select first_name, last_name from actor;

alter table actor
add column ActorName varchar(100);

select concat(upper(first_name), " ", (last_name)) as ActorName
from sakila.actor;