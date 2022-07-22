# import mysql.connector
# from database import
#
# try:
#     with connect(
#         host="localhost",
#         user=input("Enter username: "),
#         password=getpass("Enter password: "),
#     ) as connection:
#         create_db_query = "CREATE DATABASE Wallet_database"
#         with connection.cursor() as cursor:
#             cursor.execute(create_db_query)
#
#
#     mySql_Create_Table_wallet = """CREATE TABLE Wallet (
#                              Id int(11) NOT NULL,
#                              Name varchar(250) NOT NULL,
#                              Price float NOT NULL,
#                              Purchase_date Date NOT NULL,
#                              PRIMARY KEY (Id)) """
#
#     cursor = connection.cursor()
#     result = cursor.execute(mySql_Create_Table_Query)
#     print("Laptop Table created successfully ")
#
#
# with connection.cursor() as cursor:
#     cursor.execute(create_reviewers_table_query)
#     connection.commit()
#
# show_db_query = "SHOW DATABASES"
# >>> with connection.cursor() as cursor:
# ...     cursor.execute(show_db_query)
# ...     for db in cursor:
# ...         print(db)
