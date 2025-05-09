import sqlite3 

connection = sqlite3.connect("student.db")

cursor = connection.cursor() 

# Create the table
create_table_query="""
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME    VARCHAR(25),
    COURSE   VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS   INT
);
"""

