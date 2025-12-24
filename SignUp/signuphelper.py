
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
    try :
        Phone = str(Phone).strip()
        if len(str(Phone)) != 10:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False
    
