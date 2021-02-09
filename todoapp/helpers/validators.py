
def validate_not_empty_values( field_array, form ):
    """ This function validate if all the fields exists in a posted form to flask.
        
        Parameters
        ----------
        field_array: list
        The list of fields to evaluate exists in a posted form.

        form: dict
        The posted form sent by a client.


        Returns
        -------
        A boolean True if all fields exists in the form. Otherwise returns False.


    """

    for field in field_array:
        if not form[field] :
            return False

    return True



