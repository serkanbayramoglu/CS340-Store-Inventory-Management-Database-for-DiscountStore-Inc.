
-- Prepared by Emma Babcock & Serkan Bayramoglu

-- Your submission should contain ALL the queries required to implement ALL the
-- functionalities listed in the Project Specs.
-- To continue the example from above, if you have 5 tables in your schema, then at a minimum, we expect you to implement 5 SELECTs, 5 INSERTs, 1 UPDATE (M:M), 1 -- DELETE (M:M), 1 NULLable relationship, and 1 Search/Dynamic for a total of 14 functions. 
-- Note: Users are not allowed to manually set foreign keys. They will instead use dropdowns which retrieves entries that exist.

-- Customers

SELECT Customers.customer_id, name, surname, phone_number, signup_date FROM Customers;

SELECT Customers.customer_id, name, surname, phone_number, signup_date FROM Customers WHERE customer_id=%s;

INSERT INTO Customers (name, surname, phone_number, signup_date) VALUES (%s, %s, %s, %s);

DELETE FROM Customers WHERE customer_id = %s;

UPDATE Customers SET name= %s, surname= %s, phone_number= %s, signup_date= %s WHERE customer_id= %s;



-- Sales 

SELECT Sales.sale_id, invoice_number, invoice_date, sales_price_pu, sales_quantity, sales_manager, Items.producer_model_number AS producer_model_number, Customers.customer_id, Customers.name AS customer_name, Customers.surname AS customer_surname FROM Sales LEFT JOIN Customers ON Sales.customer_id = Customers.customer_id LEFT JOIN Items ON Sales.item_id = Items.item_id;

SELECT Sales.sale_id, invoice_number, invoice_date, sales_price_pu, sales_quantity, Customers.name AS customer_name, Items.producer_model_number AS producer_model_number, sales_manager FROM Sales LEFT JOIN Customers ON Sales.customer_id = Customers.customer_id LEFT JOIN Items ON Sales.item_id = Items.item_id WHERE sale_id=%s;

INSERT INTO Sales (invoice_number, invoice_date, sales_price_pu, sales_quantity, customer_id, item_id, sales_manager) VALUES (%s, %s, %s, %s, %s, %s, %s);

DELETE FROM Sales WHERE sale_id = %s;

UPDATE Sales SET invoice_number= %s, invoice_date= %s, sales_price_pu= %s, sales_quantity= %s, customer_id= %s, item_id= %s, sales_manager= %s WHERE sale_id= %s;



-- Orders

SELECT order_invoice_number FROM Orders;

SELECT order_id FROM Orders WHERE order_invoice_number = %s;

SELECT Orders.order_id, order_invoice_number, order_date, expected_arrival_date, arrival_date, total_price, has_arrived, Suppliers.supplier_name AS supplier_id FROM Orders LEFT JOIN Suppliers ON Orders.supplier_id = Suppliers.supplier_id;

SELECT Orders.order_id, order_invoice_number, order_date, expected_arrival_date, arrival_date, total_price, has_arrived, Suppliers.supplier_name AS supplier_id FROM Orders LEFT JOIN Suppliers ON Orders.supplier_id = Suppliers.supplier_id WHERE order_id=%s;

INSERT INTO Orders (order_invoice_number, order_date, expected_arrival_date, arrival_date, total_price, has_arrived, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s);

DELETE FROM Orders WHERE order_id = %s;

UPDATE Orders SET order_invoice_number= %s, order_date= %s, expected_arrival_date= %s, arrival_date= %s, total_price= %s, has_arrived= %s, supplier_id= %s WHERE order_id= %s;


-- Suppliers

SELECT supplier_name FROM Suppliers;

SELECT supplier_id FROM Suppliers WHERE supplier_name = %s;

SELECT Suppliers.supplier_id, supplier_name, contact_details, contact_person, account_manager FROM Suppliers;

SELECT Suppliers.supplier_id, supplier_name, contact_details, contact_person, account_manager FROM Suppliers WHERE supplier_id=%s;

INSERT INTO Suppliers (supplier_name, contact_details, contact_person, account_manager) VALUES (%s, %s, %s, %s)

DELETE FROM Suppliers WHERE supplier_id = %s;

UPDATE Suppliers SET supplier_name= %s, contact_details= %s, contact_person= %s, account_manager= %s WHERE supplier_id= %s;



-- Brands

SELECT brand_name FROM Brands;

SELECT brand_id from Brands WHERE brand_name = %s;

SELECT Brands.brand_id, brand_name, company_name, company_contact_details, service_contact_details, company_website FROM Brands;

SELECT Brands.brand_id, brand_name, company_name, company_contact_details, service_contact_details, company_website FROM Brands WHERE brand_id= %s;

INSERT INTO Brands (brand_name, company_name, company_contact_details, service_contact_details, company_website) VALUES (%s, %s, %s, %s, %s);

DELETE FROM Brands WHERE brand_id = %s;

UPDATE Brands SET brand_name= %s, company_name= %s, company_contact_details= %s, service_contact_details= %s, company_website= %s WHERE brand_id= %s;



-- Items

SELECT producer_model_number FROM Items;

SELECT item_id FROM Items WHERE producer_model_number = %s;

SELECT Items.item_id, product_group, Brands.brand_name AS brand, guarantee_terms, producer_model_number, product_dimensions, package_dimensions, product_description, current_price_pu, available_quantity_warehouse, section_warehouse, available_quantity_store, section_store FROM Items LEFT JOIN Brands ON brand = Brands.brand_id;

SELECT Items.item_id, product_group, Brands.brand_name AS brand, guarantee_terms, producer_model_number, product_dimensions, package_dimensions, product_description, current_price_pu, available_quantity_warehouse, section_warehouse, available_quantity_store, section_store FROM Items LEFT JOIN Brands ON brand = Brands.brand_id WHERE item_id=%s;

INSERT INTO Items (product_group, brand, guarantee_terms, producer_model_number, product_dimensions, package_dimensions, product_description, current_price_pu, available_quantity_warehouse, section_warehouse, available_quantity_store, section_store) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s);

DELETE FROM Items WHERE item_id = %s;

UPDATE Items SET product_group=%s, brand=%s, guarantee_terms=%s, producer_model_number=%s, product_dimensions=%s, package_dimensions=%s, product_description=%s, current_price_pu=%s, available_quantity_warehouse=%s, section_warehouse=%s, available_quantity_store=%s, section_store=%s WHERE item_id=%s;




-- OrderDetails 

SELECT OrderDetails.order_details_id, Orders.order_invoice_number AS order_id, Items.producer_model_number AS producer_model_number, order_quantity, order_price_pu FROM OrderDetails LEFT JOIN Orders ON OrderDetails.order_id = Orders.order_id LEFT JOIN Items ON OrderDetails.item_id = Items.item_id;

SELECT OrderDetails.order_details_id, Orders.order_invoice_number AS order_id, Items.producer_model_number AS producer_model_number, order_quantity, order_price_pu FROM OrderDetails LEFT JOIN Orders ON OrderDetails.order_id = Orders.order_id LEFT JOIN Items ON OrderDetails.item_id = Items.item_id WHERE order_details_id=%s;

INSERT INTO OrderDetails (order_id, item_id, order_quantity, order_price_pu) VALUES (%s, %s, %s, %s);

DELETE FROM OrderDetails WHERE order_details_id = %s;

UPDATE OrderDetails SET order_id= %s, item_id= %s, order_quantity= %s, order_price_pu= %s WHERE order_details_id = %s;




-- SuppliersForItems

SELECT SuppliersForItems.suppliers_for_items_id, Suppliers.supplier_name AS supplier_name, Items.producer_model_number AS producer_model_number FROM SuppliersForItems LEFT JOIN Suppliers ON SuppliersForItems.supplier_id = Suppliers.supplier_id LEFT JOIN Items ON SuppliersForItems.item_id = Items.item_id;

SELECT SuppliersForItems.suppliers_for_items_id, Suppliers.supplier_name AS supplier_id, Items.producer_model_number AS producer_model_number FROM SuppliersForItems LEFT JOIN Suppliers ON SuppliersForItems.supplier_id = Suppliers.supplier_id LEFT JOIN Items ON SuppliersForItems.item_id = Items.item_id WHERE suppliers_for_items_id=%s;

INSERT INTO SuppliersForItems (supplier_id, item_id) VALUES (%s, %s);

DELETE FROM SuppliersForItems WHERE suppliers_for_items_id = %s;

UPDATE SuppliersForItems SET supplier_id= %s, item_id= %s WHERE suppliers_for_items_id= %s;







