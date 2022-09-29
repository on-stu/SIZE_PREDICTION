import pyperclip

def find_column_by_name(to_search):
    import csv

    csv_file = open("data_extracted.csv", "r", newline="" )

    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    header = next(f)
    for i, col in enumerate(header):
        if(to_search in col):
            return i
    

def text_to_function(text : str):
    new_text = text.replace("/", " ")
    new_text = new_text.replace("-", " ")
    new_text = new_text.replace("(", " ")
    new_text = new_text.replace(")", " ")

    attributes = new_text.split(" ")

    while True:
        if('' in attributes):
            attributes.remove('')
        else:
            break

    values = {}
    for attribute in attributes:
        values[attribute] = find_column_by_name(attribute)

    result_text = text
    for key, value in values.items():
        result_text = result_text.replace(key, "float(row[{}])".format(str(value)))
    
    print("return ", result_text)
    pyperclip.copy("return " + result_text)

while True:
    text = input("input the text : ")
    if(text == 'quit'):
        break
    text_to_function(text)

    