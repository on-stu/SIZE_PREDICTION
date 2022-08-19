def search_by_col(data:list, col_name: str, expectation, opposite:bool):
    return_value = 0
    for datum in data:
        if(not opposite and datum[col_name] == expectation):
            return_value += 1
        elif(opposite and datum[col_name] != expectation):
            return_value += 1
    return return_value

def search_with_ages(data:list, col_name: str, expectation, opposite:bool, ages):
    return_value = 0
    for datum in data:
        if(not opposite and datum[col_name] == expectation and datum['나이대'] == ages):
            return_value += 1
        elif(opposite and datum[col_name] != expectation and datum['나이대'] == ages):
            return_value += 1
    return return_value

def get_value_by_col(data:list, col_name: str, expectation, opposite:bool):
    return_list = []
    for datum in data:
        if(not opposite and datum[col_name] == expectation):
            return_list.append(datum)
        elif(opposite and datum[col_name] != expectation):
            return_list.append(datum)
    return return_list

def get_col(data:list, col_name:str):
    return_list = []
    for datum in data:
        return_list.append(datum[col_name])
    return return_list