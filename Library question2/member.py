import mysql.connector

class Member:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="Library"
        )
        self.cursor = self.db_connection.cursor()

    import mysql.connector

class Member:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="Library"
        )
        self.cursor = self.db_connection.cursor()

    def add_member(self, name, address, member_type):
        try:
            sql = "INSERT INTO member (Name, Address, Type) VALUES (%s, %s, %s)"
            member_data = (name, address, member_type)
            self.cursor.execute(sql, member_data)
            self.db_connection.commit()
            print("Member added successfully.")
        except mysql.connector.Error as error:
            print("Error adding member:", error)

    def update_member(self, member_id, name, address, member_type):
        try:
            sql = "UPDATE member SET Name=%s, Address=%s, Type=%s WHERE MemberID=%s"
            member_data = (name, address, member_type, member_id)
            self.cursor.execute(sql, member_data)
            self.db_connection.commit()
            print("Member updated successfully.")
        except mysql.connector.Error as error:
            print("Error updating member:", error)


    def display_members(self):
        try:
            self.cursor.execute("SELECT * FROM member")
            members = self.cursor.fetchall()
            if members:
                print("======= Members =======")
                print("MemberID\tName\tAddress\t\tType")
                for member in members:
                    print(f"{member[0]}\t\t{member[1]}\t{member[2]}\t{member[3]}")
                print("=======================")
            else:
                print("No members available in the library.")
        except mysql.connector.Error as error:
            print("Error displaying members:", error)


    def can_delete_member(self, member_id):
        try:
            # Check if the member has any active book issues
            self.cursor.execute("SELECT COUNT(*) FROM issue WHERE MemberID=%s", (member_id,))
            count = self.cursor.fetchone()[0]
            return count == 0  # If count is 0, member can be deleted
        except mysql.connector.Error as error:
            print("Error checking member's book issues:", error)
            return False

    def delete_member(self, member_id):
        try:
            if self.can_delete_member(member_id):
                # Delete the member if no active book issues
                sql = "DELETE FROM member WHERE MemberID=%s"
                self.cursor.execute(sql, (member_id,))
                self.db_connection.commit()
                print("Member deleted successfully.")
            else:
                print("Cannot delete member as they have active book issues.")
        except mysql.connector.Error as error:
            print("Error deleting member:", error)

    # Other methods remain the same...

if __name__ == "__main__":
    member_manager = Member()
    member_manager.delete_member(1)  # Example: Deleting member with ID 1
