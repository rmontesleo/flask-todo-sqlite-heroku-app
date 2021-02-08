
def validate_not_empty_values( field_array, form ):
    for field in field_array:
        if not form[field] :
            return False

    return True



