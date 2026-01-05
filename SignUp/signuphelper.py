
# Validating full name
def validationForFName (fname, lname):
    try :
        FullName = fname + " " + lname   
        FullName = str(FullName).strip()
        if len(FullName) < 3:
            return False
        else:
            return FullName
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False
    
# Validating phone number
def validationForPhone(Phone):
    try:
        Phone = str(Phone).strip()

        if not Phone.isdigit():
            return False

        if len(Phone) != 10:
            return False

        return True

    except Exception as e:
        print(f"Error during phone validation: {e}")
        return False
