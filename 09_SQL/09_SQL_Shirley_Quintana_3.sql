-- 3a.  create a column in the table actor called 'description'; use data type 'blob'
use sakila;
select * from sakila.actor;
alter table actor
add column description blob;

-- 3b. delete the description column
select * from sakila.actor;
alter table actor
drop column description;