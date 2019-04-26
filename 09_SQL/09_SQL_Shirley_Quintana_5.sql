-- 5a.  you cannot locate the schema of the 'address' table - write a query to re-create it
use sakila;
create table address3 (
	address_id int auto_increment not null,
    address varchar(100),
    address2 varchar(100),
    district varchar(75),
    city_id int,
    postal_code int, 
    phone int,
    location blob,
    last_update datetime,
    primary key (address_id)
);
