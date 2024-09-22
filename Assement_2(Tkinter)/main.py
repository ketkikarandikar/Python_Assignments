import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from db_connection import connect_db

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management Application")
        self.current_user = None
        self.setup_login_screen()

    def setup_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)
        
        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.entry_password = tk.Entry(self.login_frame, show='*')
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.login_frame, text="Register", command=self.setup_registration_screen).grid(row=3, column=0, columnspan=2, pady=10)

    def setup_registration_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack(pady=20)

        tk.Label(self.register_frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
        self.entry_reg_username = tk.Entry(self.register_frame)
        self.entry_reg_username.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.register_frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.entry_reg_password = tk.Entry(self.register_frame, show='*')
        self.entry_reg_password.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.register_frame, text="User Type").grid(row=2, column=0, padx=10, pady=10)
        self.user_type = tk.StringVar()
        self.user_type.set("customer")
        tk.Radiobutton(self.register_frame, text="Manager", variable=self.user_type, value="manager").grid(row=2, column=1, padx=10, pady=10)
        tk.Radiobutton(self.register_frame, text="Customer", variable=self.user_type, value="customer").grid(row=2, column=2, padx=10, pady=10)

        tk.Button(self.register_frame, text="Register", command=self.register).grid(row=3, column=0, columnspan=3, pady=10)
        tk.Button(self.register_frame, text="Back to Login", command=self.setup_login_screen).grid(row=4, column=0, columnspan=3, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if not username or not password:
            messagebox.showerror("Input Error", "Please enter both username and password")
            return
        
        connection = None
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()
            if user:
                self.current_user = user
                if user[3] == 'manager':
                    self.setup_manager_screen()
                else:
                    self.setup_customer_screen()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if connection:
                connection.close()

    def register(self):
        username = self.entry_reg_username.get()
        password = self.entry_reg_password.get()
        user_type = self.user_type.get()
        if not username or not password:
            messagebox.showerror("Input Error", "Please fill all fields")
            return

        connection = None
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (username, password, user_type) VALUES (%s, %s, %s)",
                           (username, password, user_type))
            connection.commit()
            messagebox.showinfo("Success", "Registration successful")
            self.setup_login_screen()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if connection:
                connection.close()

    def setup_manager_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.manager_frame = tk.Frame(self.root)
        self.manager_frame.pack(pady=20)

        tk.Label(self.manager_frame, text="Product Name").grid(row=0, column=0, padx=10, pady=10)
        self.entry_prod_name = tk.Entry(self.manager_frame)
        self.entry_prod_name.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.manager_frame, text="Price").grid(row=1, column=0, padx=10, pady=10)
        self.entry_prod_price = tk.Entry(self.manager_frame)
        self.entry_prod_price.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.manager_frame, text="Stock").grid(row=2, column=0, padx=10, pady=10)
        self.entry_prod_stock = tk.Entry(self.manager_frame)
        self.entry_prod_stock.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(self.manager_frame, text="Add Product", command=self.add_product).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.manager_frame, text="View Products", command=self.view_products).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.manager_frame, text="Logout", command=self.setup_login_screen).grid(row=5, column=0, columnspan=2, pady=10)

        self.listbox_products = tk.Listbox(self.manager_frame, width=50, height=10)
        self.listbox_products.grid(row=6, column=0, columnspan=2, pady=10)

    def add_product(self):
        name = self.entry_prod_name.get()
        price = self.entry_prod_price.get()
        stock = self.entry_prod_stock.get()
        if not name or not price or not stock:
            messagebox.showerror("Input Error", "Please fill all fields")
            return

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid price or stock")
            return

        connection = None
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
            connection.commit()
            messagebox.showinfo("Success", "Product added successfully")
            self.entry_prod_name.delete(0, tk.END)
            self.entry_prod_price.delete(0, tk.END)
            self.entry_prod_stock.delete(0, tk.END)
            self.view_products()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if connection:
                connection.close()

    def view_products(self):
        connection = None
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            self.listbox_products.delete(0, tk.END)
            for product in products:
                self.listbox_products.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}")
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if connection:
                connection.close()

    def setup_customer_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.customer_frame = tk.Frame(self.root)
        self.customer_frame.pack(pady=20)

        tk.Button(self.customer_frame, text="View Products", command=self.view_products).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Button(self.customer_frame, text="View Orders", command=self.view_orders).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Button(self.customer_frame, text="Logout", command=self.setup_login_screen).grid(row=2, column=0, columnspan=2, pady=10)

        self.listbox_products = tk.Listbox(self.customer_frame, width=50, height=10)
        self.listbox_products.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(self.customer_frame, text="Product ID").grid(row=4, column=0, padx=10, pady=10)
        self.entry_order_prod_id = tk.Entry(self.customer_frame)
        self.entry_order_prod_id.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.customer_frame, text="Quantity").grid(row=5, column=0, padx=10, pady=10)
        self.entry_order_quantity = tk.Entry(self.customer_frame)
        self.entry_order_quantity.grid(row=5, column=1, padx=10, pady=10)

        tk.Button(self.customer_frame, text="Purchase", command=self.purchase_product).grid(row=6, column=0, columnspan=2, pady=10)

    def purchase_product(self):
        product_id = self.entry_order_prod_id.get()
        quantity = self.entry_order_quantity.get()
        if not product_id or not quantity:
            messagebox.showerror("Input Error", "Please fill all fields")
            return

        try:
            product_id = int(product_id)
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid product ID or quantity")
            return

        connection = None
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT stock FROM products WHERE id=%s", (product_id,))
            product = cursor.fetchone()
            if not product:
                messagebox.showerror("Error", "Product not found")
                return
            if product[0] < quantity:
                messagebox.showerror("Error", "Insufficient stock")
                return
            cursor.execute("UPDATE products SET stock=stock-%s WHERE id=%s", (quantity, product_id))
            cursor.execute("INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)",
                           (self.current_user[0], product_id, quantity))
            connection.commit()
            messagebox.showinfo("Success", "Purchase successful")
            self.entry_order_prod_id.delete(0, tk.END)
            self.entry_order_quantity.delete(0, tk.END)
            self.view_products()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if connection:
                connection.close()

    def view_orders(self):
        connection = None
        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT orders.id, products.name, orders.quantity FROM orders JOIN products ON orders.product_id = products.id WHERE orders.customer_id=%s", (self.current_user[0],))
            orders = cursor.fetchall()
            self.listbox_products.delete(0, tk.END)
            for order in orders:
                self.listbox_products.insert(tk.END, f"Order ID: {order[0]}, Product: {order[1]}, Quantity: {order[2]}")
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if connection:
                connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()