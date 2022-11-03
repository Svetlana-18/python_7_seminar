def creat_csv():
    FILE_NAME = "data_base.csv"
    with open(FILE_NAME, "w", encoding='UTF-8') as f:
        f.write("Фамилия, Имя, Отчество, номер телефона, примечание \n")

def creat_txt():
    FILE_NAME1 = "data_base.txt"
    with open(FILE_NAME1, "w", encoding='UTF-8') as f1:
        f1.write("Фамилия, Имя, Отчество, номер телефона, примечание \n")