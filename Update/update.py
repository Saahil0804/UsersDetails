from Update.updatehelper import *
from datetime import datetime


def updateUserDetails(email_id):
    try:
        connection = dbConnection()
        if connection is None:
             raise "Error in database connection"
        cursor = connection.cursor()
        auth_query = "SELECT * FROM UserDetails WHERE email_id = %s AND is_active = true"    
        cursor.execute(auth_query, (email_id,))
        user = cursor.fetchone()
        if not user:
            return False 
        else:
            return True
    except Exception as e:
        print(f"An error occurred during user authentication: {e}")
        return False        


# Function to update user data into the database
def update_user_data(email_id,fname,lname,phone_update,choice):
    try:
        checkuserExist= updateUserDetails(email_id)
        if checkuserExist == False:
            return "User is not Exist"  
        name_update = validationForNewFname (fname, lname)
        connection = dbConnection()
        if connection is None:
            return "Failed to connect to the database."
        cursor = connection.cursor()
        if choice == 1:
            update_query = """
                UPDATE UserDetails
                SET FullName = %s, updated_at = CURRENT_TIMESTAMP, updated_by = FullName
                WHERE email_id = %s
            """
            cursor.execute(update_query, (name_update, email_id))
        if choice == 2:
            update_query = """
                UPDATE UserDetails
                SET phone_no = %s, updated_at = CURRENT_TIMESTAMP, updated_by = FullName
                WHERE email_id = %s
            """
            cursor.execute(update_query, (phone_update, email_id))
        if choice == 3:
            update_query = """
                    UPDATE UserDetails
                    SET FullName = %s, phone_no = %s, updated_at = CURRENT_TIMESTAMP, updated_by = FullName
                    WHERE email_id = %s
            """
            cursor.execute(update_query, (name_update, phone_update, email_id))
        connection.commit()
        cursor.close()
        connection.close()
        return "User details updated successfully."
    except Exception as e:
        print(f"An error occurred while updating user data: {e}")
        raise "Failed to update user details."