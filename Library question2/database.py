import mysql.connector

# Connect to MySQL server
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="ombati",
    password="your_password"
)

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

try:
    # Create the Library database
    cursor.execute("CREATE DATABASE IF NOT EXISTS Library")

    # Select the Library database
    cursor.execute("USE Library")

    # Create the bookRecord table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookRecord (
            Bno INT AUTO_INCREMENT PRIMARY KEY,
            Title VARCHAR(255) NOT NULL,
            Author VARCHAR(255) NOT NULL,
            Quantity INT NOT NULL,
            Available INT NOT NULL
        )
    """)

    # Create the issue table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issue (
            IssueID INT AUTO_INCREMENT PRIMARY KEY,
            Bno INT,
            MemberID INT,
            IssueDate DATE,
            DueDate DATE,
            FOREIGN KEY (Bno) REFERENCES bookRecord(Bno),
            FOREIGN KEY (MemberID) REFERENCES member(MemberID)
        )
    """)

    # Create the member table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS member (
            MemberID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Address VARCHAR(255) NOT NULL,
            Type VARCHAR(10) NOT NULL
        )
    """)

    print("Database and tables created successfully.")

except mysql.connector.Error as error:
    print("Error while creating database and tables:", error)

finally:
    # Close cursor and database connection
    if cursor:
        cursor.close()
    if db_connection:
        db_connection.close()
