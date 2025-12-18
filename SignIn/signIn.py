from SignIn.signInHelper import dbConnection

# Function to sign in an existing user
def signInUser(email_id, Pword):
    try:
        connection = dbConnection()
        if connection is None:
            raise "Error in database connection"
        cursor = connection.cursor()
        select_query = """
                SELECT * FROM UserDetails WHERE email_id = %s AND Pword = %s AND is_active = TRUE
            """
        cursor.execute(select_query, (email_id, Pword))
        user = cursor.fetchone()
        if user:
            return {
                 "user_id":user[0],
                 "username":user[1],
                 "password":user[2],
                 "fname":user[3],
                 "mail":user[4],
                 "phone":user[5],
            }
        else:
            return "Invalid email or password."
    except Exception as e:
            print("Error in the signInUser:SignIn.signIn",str(e))
            raise e
    finally:
            cursor.close()
            connection.close()