import sqlite3
import pandas as pd

square= lambda n : n*n



with sqlite3.connect("Northwind.db") as conn: 
    conn.create_function("square", 1 ,square)
    cursor= conn.cursor()
    query= "SELECT *, square(Price) FROM products"
    cursor.execute(query)
    results= cursor.fetchall()
    results_df= pd.DataFrame(results)

print(results_df)


# conn= sqlite3.connect("Northwind.db")
# conn.create_function("square", 1, square)

# cursor= conn.cursor()

# cursor.execute(
#     '''
#     SELECT * FROM Products
    
#     '''
# )

# results= cursor.fetchall()
# results_df= pd.DataFrame(results)

# conn.commit()
# cursor.close()
# conn.close()    
# print(results_df)