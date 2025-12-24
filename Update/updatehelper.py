# Validating new full name
def validationForNewFname(newfname, newlname):
    try:
        full_name = f"{newfname} {newlname}".strip()
        if len(full_name) < 3:
            return False
        return full_name
    except Exception:
        return False
