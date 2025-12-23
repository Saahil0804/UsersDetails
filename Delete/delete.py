from Delete.deletehelper import dbConnection

# Function to allow user to soft delete or hard delete their account
def deleteUserAccount(email_id, delete_choice):
    try:
        connection = dbConnection()
        if connection is None:
            return "Failed to connect to the database."
        cursor = connection.cursor()
        auth_query = "SELECT * FROM UserDetails WHERE email_id = %s"    
        cursor.execute(auth_query, (email_id,))
        user = cursor.fetchone()
        if not user:
            return "Authentication failed. Please check your email and try again."   
        else:
            print("Authentication successful. You can now delete your account.")
            if delete_choice == 1:
                soft_delete_query = "UPDATE UserDetails SET is_active = false WHERE email_id = %s"
                cursor.execute(soft_delete_query, (email_id,))
                connection.commit()
                print("Your account has been soft deleted.")
            elif delete_choice == 2:
                hard_delete_query = "DELETE FROM UserDetails WHERE email_id = %s"
                cursor.execute(hard_delete_query, (email_id,))
                connection.commit()
                print("Your account has been hard deleted.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
            return True
    except Exception as e:
        print(f"An error occurred during account deletion: {e}")
        raise str(e)