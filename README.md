# Store Inventory Management Database – DiscountStore Inc.

A database-driven inventory management web application developed as a course project for **CS 340: Introduction to Databases at Oregon State University**.

The project models the operations of a fictional discount retailer, **DiscountStore Inc.**, including customers, inventory, brands, suppliers, purchases, sales, and supplier-item relationships.

## Technologies

- Python
- Flask
- MySQL / MariaDB
- Jinja2
- HTML / CSS
- SQL

## Features

The application provides a web interface for managing the store's relational database, including:

- View, add, edit, and delete database records
- Manage customers and customer information
- Manage products and inventory
- Maintain brand and supplier information
- Record and manage customer sales
- Manage supplier orders and order details
- Associate suppliers with the products they supply
- Retrieve related records using SQL joins
- Select related entities through dynamically populated fields

## Database Design

The relational database contains the following primary entities:

- **Customers**
- **Items**
- **Brands**
- **Suppliers**
- **Sales**
- **Orders**
- **OrderDetails**
- **SuppliersForItems**

The schema uses primary and foreign keys to model relationships between customers, products, sales, suppliers, and orders.

`SuppliersForItems` implements the many-to-many relationship between suppliers and inventory items.

## Application Architecture

The application uses **Flask** as the Python web framework and **Jinja2** templates to generate the user interface.

Flask routes handle database operations and communicate with a MySQL/MariaDB database. The application supports CRUD operations across the major database entities.

Example architecture:

User Interface (HTML / Jinja2)  
↓  
Flask Application (Python)  
↓  
SQL Queries  
↓  
MySQL / MariaDB Database

## Repository Structure

```text
.
├── Code/
│   ├── app.py
│   ├── templates/
│   └── static/
├── DDL.sql
└── DML.sql

DDL.sql

Contains the database schema, table definitions, relationships, foreign-key constraints, and sample data.

DML.sql

Contains SQL queries supporting application functionality, including:

* SELECT
* INSERT
* UPDATE
* DELETE
* JOIN operations

Code/app.py

Contains the Flask application, routing logic, database interaction, and CRUD functionality.

Code/templates/

Contains the Jinja2 templates used to generate the web interface.

Running the Project

This project was originally developed using Oregon State University’s CS340 database environment.

To run it in another environment, the database connection settings in Code/app.py must be configured for an available MySQL/MariaDB database.

The repository intentionally does not contain the original database credentials.

After configuring the database:

1. Create the database schema using DDL.sql.
2. Configure the database connection in Code/app.py.
3. Install the required Python/Flask/MySQL dependencies.
4. Run the Flask application.

Because this is an archived course project from 2022, dependency versions and configuration may require updating for a current environment.

Academic Context

This project was developed in 2022 as part of Oregon State University’s CS 340 – Introduction to Databases course.

The primary learning objectives included:

* Relational database design
* Entity relationships and foreign keys
* Many-to-many relationships
* SQL queries and joins
* CRUD operations
* Connecting a relational database to a web application
* Building a database-backed interface using Python and Flask

Authors

Serkan Bayramoglu
Emma Babcock

Oregon State University
CS 340 – Introduction to Databases

Note

This repository is preserved as an academic project demonstrating database design, SQL, Python/Flask development, and integration of a relational database with a web application.
