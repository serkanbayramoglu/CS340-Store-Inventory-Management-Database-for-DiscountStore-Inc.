from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import sys

# Configuration
app = Flask(__name__)

# database connection info
# - PLEASE NOTE THAT WE REMOVED OUR CREDENTIALS ON PURPOSE
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_XXXX"
app.config["MYSQL_PASSWORD"] = "XXXX"
app.config["MYSQL_DB"] = "cs340_XXXX"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Route to Homepage
@app.route("/")
def home():
    return render_template("index.j2")

@app.route("/index.html")
def home2():
    return redirect("/")

# Route to Main Pages for Tables
@app.route("/<table_name>")
def show_tablepage(table_name):
    return render_template("tablesentry.j2", table_name=table_name)

# Insert Data
@app.route("/<table_name>/insert", methods=["POST"])
def insert_data(table_name):
    # required fields ahould also contain non space characters
    all_forms = dict()
    for key in request.form.keys():
        if request.form[key].strip() == "":
            all_forms[key] = None
        else:
            all_forms[key] = request.form[key]
    error_message = ""
    exception_occured = False
    if table_name == "Brands":
        query1 = "INSERT INTO Brands (brand_name, company_name, company_contact_details, service_contact_details, company_website) VALUES (%s, %s, %s, %s, %s)"
        cur = mysql.connection.cursor()
        try:
            cur.execute(query1, (all_forms['brand_name'], all_forms['company_name'], all_forms['company_contact_details'], all_forms['service_contact_details'], all_forms['company_website']))
        except:
            error_m = str(sys.exc_info()[1])
            exception_occured = True
    elif table_name == "Customers":
        surname = all_forms['surname'] if all_forms['surname'] != "" else None
        query1 = "INSERT INTO Customers (name, surname, phone_number, signup_date) VALUES (%s, %s, %s, %s)"
        cur = mysql.connection.cursor()
        try:
            cur.execute(query1, (all_forms['name'], surname, all_forms['phone_number'], all_forms['signup_date']))
        except:
            error_m = str(sys.exc_info()[1])
            exception_occured = True
    elif table_name == "Suppliers":
        query1 = "INSERT INTO Suppliers (supplier_name, contact_details, contact_person, account_manager) VALUES (%s, %s, %s, %s)"
        cur = mysql.connection.cursor()
        try:
            cur.execute(query1, (all_forms['supplier_name'],all_forms['contact_details'],all_forms['contact_person'],all_forms['account_manager']))
        except:
            error_m = str(sys.exc_info()[1])
            exception_occured = True
    elif table_name == "Items":
        query0 = "SELECT brand_id from Brands WHERE brand_name = %s;"
        cur = mysql.connection.cursor()
        cur.execute(query0, (all_forms['brand_name'],))
        data0 = cur.fetchall()
        product_dimensions = all_forms['product_dimensions'] if all_forms['product_dimensions'] != "" else None
        package_dimensions = all_forms['package_dimensions'] if all_forms['package_dimensions'] != "" else None
        product_description = all_forms['product_description'] if all_forms['product_description'] != "" else None
        section_warehouse = all_forms['section_warehouse'] if all_forms['section_warehouse'] != "" else None
        section_store = all_forms['section_store'] if all_forms['section_store'] != "" else None
        query1 = "INSERT INTO Items (product_group, brand, guarantee_terms, producer_model_number, product_dimensions, package_dimensions, product_description, current_price_pu, available_quantity_warehouse, section_warehouse, available_quantity_store, section_store) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"
        cur = mysql.connection.cursor()
        try:
            cur.execute(query1, (all_forms['product_group'],data0[0]['brand_id'],all_forms['guarantee_terms'],all_forms['producer_model_number'], product_dimensions, package_dimensions, product_description, all_forms['current_price_pu'],all_forms['available_quantity_warehouse'],section_warehouse, all_forms['available_quantity_store'], section_store))
        except:
            error_m = str(sys.exc_info()[1])
            exception_occured = True
    elif table_name == "SuppliersForItems":
        query0 = "SELECT supplier_id FROM Suppliers WHERE supplier_name = %s;"
        cur = mysql.connection.cursor()
        cur.execute(query0, (all_forms['supplier_name'],))
        data01 = cur.fetchall()
        query0 = "SELECT item_id FROM Items WHERE producer_model_number = %s;"
        cur = mysql.connection.cursor()
        cur.execute(query0, (all_forms['producer_model_number'],))
        data02 = cur.fetchall()
        query1 = "INSERT INTO SuppliersForItems (supplier_id, item_id) VALUES (%s, %s)"
        cur = mysql.connection.cursor()
        try:
            cur.execute(query1, (data01[0]['supplier_id'], data02[0]['item_id']))
        except:
            error_m = str(sys.exc_info()[1])
            exception_occured = True
    elif table_name == "Sales":
        if all_forms['producer_model_number'] == "":
            item_id = None
        else:
            query0 = "SELECT item_id FROM Items WHERE producer_model_number = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query0, (all_forms['producer_model_number'],))
            data01 = cur.fetchall()
            item_id = data01[0]['item_id']
        query1 = "INSERT INTO Sales (invoice_number, invoice_date, sales_price_pu, sales_quantity, customer_id, item_id, sales_manager) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur = mysql.connection.cursor()
        try:
            cur.execute(query1, (all_forms['invoice_number'], all_forms['invoice_date'], all_forms['sales_price_pu'], all_forms['sales_quantity'], all_forms['customer_id'], item_id, all_forms['sales_manager']))
        except:
            error_m = str(sys.exc_info()[1])
            exception_occured = True
    elif table_name == "Orders":
        if all_forms['supplier_name'] == "":
            supplier_id = None
        else:
            query0 = "SELECT supplier_id FROM Suppliers WHERE supplier_name = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query0, (all_forms['supplier_name'],))
            data0 = cur.fetchall()
            supplier_id = data0[0]['supplier_id']
        expected_arrival_date = all_forms['expected_arrival_date'] if all_forms['expected_arrival_date'] != "" else None
        arrival_date = all_forms['arrival_date'] if all_forms['arrival_date'] != "" else None
        query1 = "INSERT INTO Orders (order_invoice_number, order_date, expected_arrival_date, arrival_date, total_price, has_arrived, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur = mysql.connection.cursor()
        try:
            cur.execute(query1, (all_forms['order_invoice_number'], all_forms['order_date'], expected_arrival_date, arrival_date, all_forms['total_price'], all_forms['has_arrived'], supplier_id))
        except:
            error_m = str(sys.exc_info()[1])
            exception_occured = True
    elif table_name == "OrderDetails":
        if all_forms['producer_model_number'] == "":
            item_id = None
        else:
            query0 = "SELECT item_id FROM Items WHERE producer_model_number = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query0, (all_forms['producer_model_number'],))
            data01 = cur.fetchall()
            item_id = data01[0]['item_id']
        if all_forms['order_invoice_number'] == "":
            order_id = None
        else:
            query0 = "SELECT order_id FROM Orders WHERE order_invoice_number = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query0, (all_forms['order_invoice_number'],))
            data02 = cur.fetchall()
            order_id = data02[0]['order_id']
        query1 = "INSERT INTO OrderDetails (order_id, item_id, order_quantity, order_price_pu) VALUES (%s, %s, %s, %s)"
        cur = mysql.connection.cursor()
        try:
            cur.execute(query1, (order_id, item_id, all_forms['order_quantity'], all_forms['order_price_pu']))
        except:
            error_m = str(sys.exc_info()[1])
            exception_occured = True

    mysql.connection.commit()

    if exception_occured:
        error_message = "Unknown exception occured. Please try again"
        if error_m[1:5] == "1062":
            error_message = "A record with the same unique attribute already exists, dublicate entries on unique attributes are not allowed"
        elif error_m[1:5] == "1048":
            error_message = "Please include non-space character(s) to the required attributes"
        return render_template("tablesentry.j2", table_name=table_name, error_message=error_message)
    else:
        return render_template("tablesentry.j2", table_name=table_name, result_message="Record added successfully!")

# Retriece All or Queried Data
@app.route("/<table_name>/action/", methods=["GET"])
def retrieve_data(table_name):
    all_args = request.args
    retrieve_query = False
    if "select_option" in all_args:
        if all_args["select_option"] == "new_entry":
            data_brands, data_suppliers, data_producer_model_numbers, data_order_invoice_numbers = retrieve_required_lists(table_name)
            return render_template("tablesentry.j2", action_name="enter_new", data_1="", table_name=table_name, data_brands=data_brands, data_suppliers=data_suppliers, data_producer_model_numbers=data_producer_model_numbers, data_order_invoice_numbers=data_order_invoice_numbers)
        elif all_args["select_option"] == "retrieve_query":
            data_brands, data_suppliers, data_producer_model_numbers, data_order_invoice_numbers = retrieve_required_lists(table_name)
            return render_template("tablesentry.j2", action_name="retrieve_query", data_1="", table_name=table_name, data_brands=data_brands, data_suppliers=data_suppliers, data_producer_model_numbers=data_producer_model_numbers, data_order_invoice_numbers=data_order_invoice_numbers)
    if "select_option" not in all_args:
        retrieve_query = True
    exception_occured, key_id, data = retrieve_data_helper("main", table_name, retrieve_query, all_args)
    if exception_occured:
        error_message = "Unknown exception occured. Please try again"
        return render_template("tablesentry.j2", table_name=table_name, data="", key_id=key_id, action_name="retrieve_data", error_message=error_message)
    elif len(data) > 0:
        return render_template("tablesentry.j2", table_name=table_name, data=data, key_id=key_id, action_name="retrieve_data")
    else:
        if retrieve_query:
            result_message="No data available under this search criteria!"
        else:
            result_message="The " + table_name + " table has no records!"
        return render_template("tablesentry.j2", table_name=table_name, data=data, key_id=key_id, action_name="retrieve_data", result_message=result_message)

# Retrieve Supporting Data
@app.route("/<table_name>/supportingaction", methods=["GET"])
def retrieve_data_2(table_name):
    all_args = request.args
    data_brands, data_suppliers, data_producer_model_numbers, data_order_invoice_numbers = retrieve_required_lists(table_name)
    if 'items_id' in all_args:
        items_id = all_args['items_id']
    else:
        items_id = ""
    table_name_2 = all_args['supporting_table']
    retrieve_query = True
    exception_occured, key_id_2, data_2 = retrieve_data_helper("supporting", table_name_2, retrieve_query, all_args)
    if exception_occured:
        error_message = "Unknown exception occured. Please try again"
        return render_template("tablesentry.j2", table_name=table_name, data_2="", key_id_2=key_id_2, action_name=all_args['action_name'], error_message=error_message)
    elif len(data_2) > 0:
        return render_template("tablesentry.j2", table_name=table_name, data_1=all_args, data_2=data_2, key_id_2=key_id_2, items_id=items_id, data_brands=data_brands, action_name=all_args['action_name'])
    else:
        if retrieve_query:
            result_message="No data available under this search criteria!"
        else:
            result_message="The " + table_name + " table has no records!"
        return render_template("tablesentry.j2", table_name=table_name, data_1=all_args, data_2=data_2, key_id_2=key_id_2, items_id=items_id, data_brands=data_brands, action_name=all_args['action_name'], result_message=result_message)


def retrieve_data_helper(table_type, table_name, retrieve_query, all_args):
    data = ""
    w_sec = ""
    key_id = ""
    query_list = []
    if table_name == "Brands":
        query = "SELECT Brands.brand_id, brand_name, company_name, company_contact_details, service_contact_details, company_website FROM Brands"
        if retrieve_query:
            args_list = ["brand_id", "brand_name"]
            args_list_like = ["company_name", "company_contact_details", "service_contact_details", "company_website"]
            for argument in args_list:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + "=%s"
                    query_list.append(all_args[argument])
            for argument in args_list_like:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + " LIKE %s"
                    query_list.append("%" + all_args[argument] + "%")
        key_id = "brand_id"
    elif table_name == "Customers":
        query = "SELECT Customers.customer_id, name, surname, phone_number, signup_date FROM Customers"
        if retrieve_query:
            args_list = ["customer_id", "signup_date"]
            args_list_like = ["name", "surname", "phone_number"]
            for argument in args_list:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + "=%s"
                    query_list.append(all_args[argument])
            for argument in args_list_like:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + " LIKE %s"
                    query_list.append("%" + all_args[argument] + "%")
        key_id = "customer_id"
    elif table_name == "Suppliers":
        query = "SELECT Suppliers.supplier_id, supplier_name, contact_details, contact_person, account_manager FROM Suppliers"
        if retrieve_query:
            args_list = ["supplier_id", "account_manager"]
            args_list_like = ["supplier_name", "contact_details", "contact_person"]
            for argument in args_list:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + "=%s"
                    query_list.append(all_args[argument])
            for argument in args_list_like:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + " LIKE %s"
                    query_list.append("%" + all_args[argument] + "%")
        key_id = "supplier_id"
    elif table_name == "Items":
        query = "SELECT Items.item_id, product_group, Brands.brand_name AS brand, guarantee_terms, producer_model_number, product_dimensions, package_dimensions, product_description, current_price_pu, available_quantity_warehouse, section_warehouse, available_quantity_store, section_store FROM Items LEFT JOIN Brands ON brand = Brands.brand_id"
        if retrieve_query:
            args_list = ["item_id", "producer_model_number", "product_dimensions", "package_dimensions", "current_price_pu", "available_quantity_warehouse", "available_quantity_store"]
            args_list_like = ["product_group", "guarantee_terms", "product_description", "section_warehouse", "section_store"]
            for argument in args_list:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + "=%s"
                    query_list.append(all_args[argument])
            for argument in args_list_like:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + " LIKE %s"
                    query_list.append("%" + all_args[argument] + "%")
            if all_args["brand_name"] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + "Brands.brand_name" + "=%s"
                    query_list.append(all_args['brand_name'])
        key_id =  "item_id"
        if table_type == "supporting":
            key_id = "producer_model_number"
    elif table_name == "SuppliersForItems":
        query = "SELECT SuppliersForItems.suppliers_for_items_id, Suppliers.supplier_name AS supplier_name, Items.producer_model_number AS producer_model_number FROM SuppliersForItems LEFT JOIN Suppliers ON SuppliersForItems.supplier_id = Suppliers.supplier_id LEFT JOIN Items ON SuppliersForItems.item_id = Items.item_id"
        if retrieve_query:
            if all_args["suppliers_for_items_id"] != "":
                w_sec = w_sec + " AND " if w_sec != "" else ""
                w_sec = w_sec + "suppliers_for_items_id" + "=%s"
                query_list.append(all_args['suppliers_for_items_id'])
            if all_args["supplier_name"] != "":
                w_sec = w_sec + " AND " if w_sec != "" else ""
                w_sec = w_sec + "Suppliers.supplier_name" + "=%s"
                query_list.append(all_args['supplier_name'])
            if all_args["producer_model_number"] != "":
                w_sec = w_sec + " AND " if w_sec != "" else ""
                w_sec = w_sec + "Items.producer_model_number" + "=%s"
                query_list.append(all_args['producer_model_number'])
        key_id = "suppliers_for_items_id"
    elif table_name == "Sales":
        query = "SELECT Sales.sale_id, invoice_number, invoice_date, sales_price_pu, sales_quantity, sales_manager, Items.producer_model_number AS producer_model_number, Customers.customer_id, Customers.name AS customer_name, Customers.surname AS customer_surname FROM Sales LEFT JOIN Customers ON Sales.customer_id = Customers.customer_id LEFT JOIN Items ON Sales.item_id = Items.item_id"
        if retrieve_query:
            args_list = ["sale_id", "invoice_number", "invoice_date", "sales_price_pu", "sales_quantity"]
            for argument in args_list:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + "=%s"
                    query_list.append(all_args[argument])
            if all_args["producer_model_number"] != "":
                w_sec = w_sec + " AND " if w_sec != "" else ""
                w_sec = w_sec + "Items.producer_model_number" + "=%s"
                query_list.append(all_args['producer_model_number'])
            if all_args["customer_id"] != "":
                w_sec = w_sec + " AND " if w_sec != "" else ""
                w_sec = w_sec + "Customers.customer_id" + "=%s"
                query_list.append(all_args['customer_id'])
        key_id = "sale_id"
    elif table_name == "Orders":
        query = "SELECT Orders.order_id, order_invoice_number, order_date, expected_arrival_date, arrival_date, total_price, has_arrived, Suppliers.supplier_name AS supplier_id FROM Orders LEFT JOIN Suppliers ON Orders.supplier_id = Suppliers.supplier_id"
        if retrieve_query:
            args_list = ["order_id", "order_invoice_number", "order_date", "expected_arrival_date", "arrival_date", "total_price", "has_arrived"]
            for argument in args_list:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + "=%s"
                    query_list.append(all_args[argument])
            if all_args["supplier_name"] != "":
                w_sec = w_sec + " AND " if w_sec != "" else ""
                w_sec = w_sec + "Suppliers.supplier_name" + "=%s"
                query_list.append(all_args['supplier_name'])
        key_id = "order_id"
    elif table_name == "OrderDetails":
        query = "SELECT OrderDetails.order_details_id, Orders.order_invoice_number AS order_id, Items.producer_model_number AS producer_model_number, order_quantity, order_price_pu FROM OrderDetails LEFT JOIN Orders ON OrderDetails.order_id = Orders.order_id LEFT JOIN Items ON OrderDetails.item_id = Items.item_id"
        if retrieve_query:
            args_list = ["order_details_id", "order_quantity", "order_price_pu"]
            for argument in args_list:
                if all_args[argument] != "":
                    w_sec = w_sec + " AND " if w_sec != "" else ""
                    w_sec = w_sec + argument + "=%s"
                    query_list.append(all_args[argument])
            if all_args["producer_model_number"] != "":
                w_sec = w_sec + " AND " if w_sec != "" else ""
                w_sec = w_sec + "Items.producer_model_number" + "=%s"
                query_list.append(all_args['producer_model_number'])
            if all_args["order_invoice_number"] != "":
                w_sec = w_sec + " AND " if w_sec != "" else ""
                w_sec = w_sec + "Orders.order_invoice_number" + "=%s"
                query_list.append(all_args['order_invoice_number'])
        key_id = "order_details_id"
    else:
        redirect("/")

    exception_occured = False

    try:
        cur = mysql.connection.cursor()
        if w_sec != "":
            query = query + " WHERE " + w_sec + ";"
            cur.execute(query, tuple(query_list))
        else:
            query = query + ";"
            cur.execute(query)

        data = cur.fetchall()
    except:
        exception_occured = True

    return (exception_occured, key_id, data)


# Comfirm Delete Request Before Deleting Data From Tables
@app.route("/delete/<table_name>/<items_id>", methods=["GET", "POST"])
def delete_confirm_execute(table_name, items_id):
    if request.method == "GET":
        if table_name == "Brands":
            query = "SELECT Brands.brand_id, brand_name, company_name, company_contact_details, service_contact_details, company_website FROM Brands WHERE brand_id=" + items_id
        elif table_name == "Customers":
            query = "SELECT Customers.customer_id, name, surname, phone_number, signup_date FROM Customers WHERE customer_id=" + items_id
        elif table_name == "Suppliers":
            query = "SELECT Suppliers.supplier_id, supplier_name, contact_details, contact_person, account_manager FROM Suppliers WHERE supplier_id=" + items_id
        elif table_name == "Items":
            query = "SELECT Items.item_id, product_group, Brands.brand_name AS brand, guarantee_terms, producer_model_number, product_dimensions, package_dimensions, product_description, current_price_pu, available_quantity_warehouse, section_warehouse, available_quantity_store, section_store FROM Items LEFT JOIN Brands ON brand = Brands.brand_id WHERE item_id=" + items_id
        elif table_name == "SuppliersForItems":
            query = "SELECT SuppliersForItems.suppliers_for_items_id, Suppliers.supplier_name AS supplier_id, Items.producer_model_number AS producer_model_number FROM SuppliersForItems LEFT JOIN Suppliers ON SuppliersForItems.supplier_id = Suppliers.supplier_id LEFT JOIN Items ON SuppliersForItems.item_id = Items.item_id WHERE suppliers_for_items_id=" + items_id
        elif table_name == "Sales":
            query = "SELECT Sales.sale_id, invoice_number, invoice_date, sales_price_pu, sales_quantity, Customers.name AS customer_name, Items.producer_model_number AS producer_model_number, sales_manager FROM Sales LEFT JOIN Customers ON Sales.customer_id = Customers.customer_id LEFT JOIN Items ON Sales.item_id = Items.item_id WHERE sale_id=" + items_id
        elif table_name == "Orders":
            query = "SELECT Orders.order_id, order_invoice_number, order_date, expected_arrival_date, arrival_date, total_price, has_arrived, Suppliers.supplier_name AS supplier_id FROM Orders LEFT JOIN Suppliers ON Orders.supplier_id = Suppliers.supplier_id WHERE order_id=" + items_id
        elif table_name == "OrderDetails":
            query = "SELECT OrderDetails.order_details_id, Orders.order_invoice_number AS order_id, Items.producer_model_number AS producer_model_number, order_quantity, order_price_pu FROM OrderDetails LEFT JOIN Orders ON OrderDetails.order_id = Orders.order_id LEFT JOIN Items ON OrderDetails.item_id = Items.item_id WHERE order_details_id=" + items_id
        else:
            redirect("/")

        exception_occured = False
        try:
            cur = mysql.connection.cursor()
            cur.execute(query)
            data = cur.fetchall()
        except:
            exception_occured = True

        if exception_occured:
            error_message = "Unknown exception occured. Please try again"
            return render_template("tablesentry.j2", table_name=table_name, data="", items_id=items_id, action_name="delete_confirm", error_message=error_message)
        elif len(data) > 0:
            return render_template("tablesentry.j2", table_name=table_name, data=data, items_id=items_id, action_name="delete_confirm")
        else:
            result_message="Looks like the record is no more available. Please check if the record still exists"
            return render_template("tablesentry.j2", table_name=table_name, data=data, items_id=items_id,  action_name="delete_confirm", result_message=result_message)


    if request.method == "POST":
        if table_name == "Brands":
            key_id = "brand_id"
        elif table_name == "Customers":
            key_id = "customer_id"
        elif table_name == "Suppliers":
            key_id = "supplier_id"
        elif table_name == "Items":
            key_id = "item_id"
        elif table_name == "SuppliersForItems":
            key_id = "suppliers_for_items_id"
        elif table_name == "Sales":
            key_id = "sale_id"
        elif table_name == "Orders":
            key_id = "order_id"
        elif table_name == "OrderDetails":
            key_id = "order_details_id"
        else:
            redirect("/")
        query = "DELETE FROM " + table_name + " WHERE " + key_id + " = %s"

        exception_occured = False
        try:
            cur = mysql.connection.cursor()
            cur.execute(query, (items_id,))
            mysql.connection.commit()
        except:
            exception_occured = True

        if exception_occured:
            error_message = "Unknown exception occured. Please try again"
            return render_template("tablesentry.j2", table_name=table_name, error_message=error_message)
        else:
            result_message="Record deleted successfully"
            return render_template("tablesentry.j2", table_name=table_name, result_message=result_message)

# Edit Data From Table and Execute
@app.route("/edit/<table_name>/<items_id>", methods=["GET", "POST"])
def edit_execute(table_name, items_id):
    if request.method == "GET":
        data_brands, data_suppliers, data_producer_model_numbers, data_order_invoice_numbers = retrieve_required_lists(table_name)
        if table_name == "Brands":
            query = "SELECT Brands.brand_id, brand_name, company_name, company_contact_details, service_contact_details, company_website FROM Brands WHERE brand_id=" + items_id
        elif table_name == "Customers":
            query = "SELECT Customers.customer_id, name, surname, phone_number, signup_date FROM Customers WHERE customer_id=" + items_id
        elif table_name == "Suppliers":
            query = "SELECT Suppliers.supplier_id, supplier_name, contact_details, contact_person, account_manager FROM Suppliers WHERE supplier_id=" + items_id
        elif table_name == "Items":
            query = "SELECT Items.item_id, product_group, Brands.brand_name AS brand, guarantee_terms, producer_model_number, product_dimensions, package_dimensions, product_description, current_price_pu, available_quantity_warehouse, section_warehouse, available_quantity_store, section_store FROM Items LEFT JOIN Brands ON brand = Brands.brand_id WHERE item_id=" + items_id
        elif table_name == "SuppliersForItems":
            query = "SELECT SuppliersForItems.suppliers_for_items_id, Suppliers.supplier_name AS supplier_id, Items.producer_model_number AS producer_model_number FROM SuppliersForItems LEFT JOIN Suppliers ON SuppliersForItems.supplier_id = Suppliers.supplier_id LEFT JOIN Items ON SuppliersForItems.item_id = Items.item_id WHERE suppliers_for_items_id=" + items_id
        elif table_name == "Sales":
            query = "SELECT Sales.sale_id, invoice_number, invoice_date, sales_price_pu, sales_quantity, sales_manager, Items.producer_model_number AS producer_model_number, Customers.customer_id AS customer_id, Customers.name AS customer_name, Customers.surname AS customer_surname FROM Sales LEFT JOIN Customers ON Sales.customer_id = Customers.customer_id LEFT JOIN Items ON Sales.item_id = Items.item_id WHERE sale_id=" + items_id
        elif table_name == "Orders":
            query = "SELECT Orders.order_id, order_invoice_number, order_date, expected_arrival_date, arrival_date, total_price, has_arrived, Suppliers.supplier_name AS supplier_id FROM Orders LEFT JOIN Suppliers ON Orders.supplier_id = Suppliers.supplier_id WHERE order_id=" + items_id
        elif table_name == "OrderDetails":
            query = "SELECT OrderDetails.order_details_id, Orders.order_invoice_number AS order_id, Items.producer_model_number AS producer_model_number, order_quantity, order_price_pu FROM OrderDetails LEFT JOIN Orders ON OrderDetails.order_id = Orders.order_id LEFT JOIN Items ON OrderDetails.item_id = Items.item_id WHERE order_details_id=" + items_id
        else:
            redirect("/")

        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        data_1 = data[0]

        if table_name == "Sales":
            data_1['s_producer_model_number'] = data_1['producer_model_number']
            data_1['s_customer_id'] = data_1['customer_id']

        return render_template("tablesentry.j2", table_name=table_name, data_1=data_1, data=data, items_id=items_id, action_name="edit_entry", data_brands=data_brands, data_suppliers=data_suppliers, data_producer_model_numbers=data_producer_model_numbers, data_order_invoice_numbers=data_order_invoice_numbers)

    if request.method == "POST":
        # required fields ahould also contain non space characters
        all_args = dict()
        for key in request.form.keys():
            if request.form[key].strip() == "":
                all_args[key] = None
            else:
                all_args[key] = request.form[key]
        exception_occured = False
        if table_name == "Brands":
            required_attributes = ['brand_name', 'company_name', 'company_contact_details', 'service_contact_details', 'company_website']
            for attribute in required_attributes:
                if all_args[attribute] is None:
                    error_m = '01048'
                    exception_occured = True
            if exception_occured == False:
                query = "UPDATE Brands SET brand_name= %s, company_name= %s, company_contact_details= %s, service_contact_details= %s, company_website= %s WHERE brand_id= %s"
                try:
                    cur = mysql.connection.cursor()
                    cur.execute(query, (all_args["brand_name"], all_args["company_name"], all_args["company_contact_details"], all_args["service_contact_details"], all_args["company_website"], items_id))
                except:
                    error_m = str(sys.exc_info()[1])
                    exception_occured = True
        elif table_name == "Customers":
            required_attributes = ['name', 'phone_number', 'signup_date']
            for attribute in required_attributes:
                if all_args[attribute] is None:
                    error_m = '01048'
                    exception_occured = True
            if exception_occured == False:
                query = "UPDATE Customers SET name= %s, surname= %s, phone_number= %s, signup_date= %s WHERE customer_id= %s"
                try:
                    cur = mysql.connection.cursor()
                    cur.execute(query, (all_args["name"], all_args["surname"], all_args["phone_number"], all_args["signup_date"], items_id))
                except:
                    error_m = str(sys.exc_info()[1])
                    exception_occured = True
        elif table_name == "Suppliers":
            required_attributes = ['supplier_name', 'contact_details', 'contact_person', 'account_manager']
            for attribute in required_attributes:
                if all_args[attribute] is None:
                    error_m = '01048'
                    exception_occured = True
            if exception_occured == False:
                query = "UPDATE Suppliers SET supplier_name= %s, contact_details= %s, contact_person= %s, account_manager= %s WHERE supplier_id= %s"
                try:
                    cur = mysql.connection.cursor()
                    cur.execute(query, (all_args["supplier_name"], all_args["contact_details"], all_args["contact_person"], all_args["account_manager"], items_id))
                except:
                    error_m = str(sys.exc_info()[1])
                    exception_occured = True
        elif table_name == "Items":
            required_attributes = ['product_group', 'guarantee_terms', 'producer_model_number', 'current_price_pu', 'available_quantity_warehouse', 'available_quantity_store']
            for attribute in required_attributes:
                if all_args[attribute] is None:
                    error_m = '01048'
                    exception_occured = True
            if exception_occured == False:
                query = "SELECT brand_id FROM Brands WHERE brand_name= %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (all_args["brand_name"],))
                data = cur.fetchall()
                brand_id = data[0]["brand_id"]
                query = "UPDATE Items SET product_group=%s, brand=%s, guarantee_terms=%s, producer_model_number=%s, product_dimensions=%s, package_dimensions=%s, product_description=%s, current_price_pu=%s, available_quantity_warehouse=%s, section_warehouse=%s, available_quantity_store=%s, section_store=%s WHERE item_id=%s"
                try:
                    cur = mysql.connection.cursor()
                    cur.execute(query, (all_args['product_group'],brand_id,all_args['guarantee_terms'],all_args['producer_model_number'], all_args['product_dimensions'], all_args['package_dimensions'], all_args['product_description'], all_args['current_price_pu'],all_args['available_quantity_warehouse'], all_args['section_warehouse'], all_args['available_quantity_store'], all_args['section_store'], items_id))
                except:
                    error_m = str(sys.exc_info()[1])
                    exception_occured = True
        elif table_name == "SuppliersForItems":
            query = "SELECT supplier_id FROM Suppliers WHERE supplier_name= %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (all_args["supplier_name"],))
            data = cur.fetchall()
            supplier_id = data[0]["supplier_id"]
            query = "SELECT item_id FROM Items WHERE producer_model_number= %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (all_args["producer_model_number"],))
            data = cur.fetchall()
            item_id_items = data[0]["item_id"]
            query = "UPDATE SuppliersForItems SET supplier_id= %s, item_id= %s WHERE suppliers_for_items_id= %s"
            try:
                cur = mysql.connection.cursor()
                cur.execute(query, (str(supplier_id), str(item_id_items), items_id))
            except:
                error_m = str(sys.exc_info()[1])
                exception_occured = True
        elif table_name == "Sales":
            required_attributes = ['invoice_number', 'invoice_date', 'sales_price_pu', 'sales_quantity', 'sales_manager']
            for attribute in required_attributes:
                if all_args[attribute] is None:
                    error_m = '01048'
                    exception_occured = True
            if exception_occured == False:
                if all_args['producer_model_number'] == "":
                    item_id_items = None
                else:
                    query0 = "SELECT item_id FROM Items WHERE producer_model_number = %s;"
                    cur = mysql.connection.cursor()
                    cur.execute(query0, (all_args['producer_model_number'],))
                    data01 = cur.fetchall()
                    item_id_items = data01[0]['item_id']
                query1 = "UPDATE Sales SET invoice_number= %s, invoice_date= %s, sales_price_pu= %s, sales_quantity= %s, customer_id= %s, item_id= %s, sales_manager= %s WHERE sale_id= %s"
                try:
                    cur = mysql.connection.cursor()
                    cur.execute(query1, (all_args['invoice_number'], all_args['invoice_date'], all_args['sales_price_pu'], all_args['sales_quantity'], all_args['customer_id'], item_id_items, all_args['sales_manager'], items_id))
                except:
                    error_m = str(sys.exc_info()[1])
                    exception_occured = True
        elif table_name == "Orders":
            required_attributes = ['order_invoice_number', 'order_date', 'total_price']
            for attribute in required_attributes:
                if all_args[attribute] is None:
                    error_m = '01048'
                    exception_occured = True
            if exception_occured == False:
                if all_args['supplier_name'] == "":
                    supplier_id = None
                else:
                    query0 = "SELECT supplier_id FROM Suppliers WHERE supplier_name = %s;"
                    cur = mysql.connection.cursor()
                    cur.execute(query0, (all_args['supplier_name'],))
                    data0 = cur.fetchall()
                    supplier_id = data0[0]['supplier_id']
                expected_arrival_date = all_args['expected_arrival_date'] if all_args['expected_arrival_date'] != "" else None
                arrival_date = all_args['arrival_date'] if all_args['arrival_date'] != "" else None
                query1 = "UPDATE Orders SET order_invoice_number= %s, order_date= %s, expected_arrival_date= %s, arrival_date= %s, total_price= %s, has_arrived= %s, supplier_id= %s WHERE order_id= %s"
                try:
                    cur = mysql.connection.cursor()
                    cur.execute(query1, (all_args['order_invoice_number'], all_args['order_date'], expected_arrival_date, arrival_date, all_args['total_price'], all_args['has_arrived'], supplier_id, items_id))
                except:
                    error_m = str(sys.exc_info()[1])
                    exception_occured = True
        elif table_name == "OrderDetails":
            required_attributes = ['order_quantity', 'order_price_pu']
            for attribute in required_attributes:
                if all_args[attribute] is None:
                    error_m = '01048'
                    exception_occured = True
            if exception_occured == False:
                if all_args['producer_model_number'] == "":
                    item_id_items = None
                else:
                    query0 = "SELECT item_id FROM Items WHERE producer_model_number = %s;"
                    cur = mysql.connection.cursor()
                    cur.execute(query0, (all_args['producer_model_number'],))
                    data01 = cur.fetchall()
                    item_id_items = data01[0]['item_id']
                if all_args['order_invoice_number'] == "":
                    order_id = None
                else:
                    query0 = "SELECT order_id FROM Orders WHERE order_invoice_number = %s;"
                    cur = mysql.connection.cursor()
                    cur.execute(query0, (all_args['order_invoice_number'],))
                    data02 = cur.fetchall()
                    order_id = data02[0]['order_id']
                query1 = "UPDATE OrderDetails SET order_id= %s, item_id= %s, order_quantity= %s, order_price_pu= %s WHERE order_details_id = %s"
                try:
                    cur = mysql.connection.cursor()
                    cur.execute(query1, (order_id, item_id_items, all_args['order_quantity'], all_args['order_price_pu'], items_id))
                except:
                    error_m = str(sys.exc_info()[1])
                    exception_occured = True
        else:
            redirect("/")

        mysql.connection.commit()

        if exception_occured:
            error_message = "Unknown exception occured. Please try again"
            if error_m[1:5] == "1062":
                error_message = "A record with the same unique attribute already exists, dublicate entries on unique attributes are not allowed"
            elif error_m[1:5] == "1048":
                error_message = "Please include non-space character(s) to the required attributes"
            return render_template("tablesentry.j2", table_name=table_name, error_message=error_message)
        else:
            return render_template("tablesentry.j2", table_name=table_name, result_message="Record updated successfully!")

def retrieve_required_lists(table_name):
    data_brands = ""
    data_suppliers = ""
    data_producer_model_numbers = ""
    data_order_invoice_numbers = ""
    if table_name == "Items":
        data_brands = retrieve_brand_names()
    elif table_name == "SuppliersForItems":
        data_suppliers = retrieve_supplier_names()
        data_producer_model_numbers = retrieve_producer_model_numbers()
    elif table_name == "Sales":
        data_producer_model_numbers = retrieve_producer_model_numbers()
        data_brands = retrieve_brand_names()
    elif table_name == "Orders":
        data_suppliers = retrieve_supplier_names()
    elif table_name == "OrderDetails":
        data_producer_model_numbers = retrieve_producer_model_numbers()
        data_order_invoice_numbers = retrieve_order_invoice_numbers()
    return (data_brands, data_suppliers, data_producer_model_numbers, data_order_invoice_numbers)

def retrieve_brand_names():
    query = "SELECT brand_name FROM Brands"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data

def retrieve_supplier_names():
    query = "SELECT supplier_name FROM Suppliers"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data

def retrieve_producer_model_numbers():
    query = "SELECT producer_model_number FROM Items"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data

def retrieve_order_invoice_numbers():
    query = "SELECT order_invoice_number FROM Orders"
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data

# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=6128, debug=True)
