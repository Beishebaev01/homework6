import re

while True:
    try:
        user = int(input("Выберите действия:\n"
                         "1) Считать имена и фамилии\n"
                         "2) Считать все емайлы\n"
                         "3) Считать названия файлов\n"
                         "4) Считать цвет\n"
                         "5) Выход\n"
                         ">>> "))

        if user == 1:
            with open("MOCK_DATA.txt") as mock:
                data = mock.read()
            names = re.findall(r"[A-Z][a-z]*\s[A-Z][a-z]*[A '-Z']*[a-z]*", data)
            with open("names.txt", "w") as n:
                for name in names:
                    n.write(name + "\n")
            print("Имена и фамилии сохранены в names.txt")

        elif user == 2:
            with open("MOCK_DATA.txt") as mock:
                data = mock.read()
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
            with open("emails.txt", "w") as e:
                for email in emails:
                    e.write(email + "\n")
            print("Почта сохранена в emails.txt")

        elif user == 3:
            with open("MOCK_DATA.txt") as mock:
                data = mock.read()
            file_names = re.findall(r'\b\w+\.\w{2,3}\b', data)
            with open("filenames.txt", "w") as f:
                for filename in file_names:
                    f.write(filename + "\n")
            print("Названия файлов сохранены в filenames.txt")

        elif user == 4:
            with open("MOCK_DATA.txt") as mock:
                data = mock.read()
            colors = re.findall(r'#[0-9A-Fa-f]{6}\b', data)
            with open("colors.txt", "w") as c:
                for color in colors:
                    c.write(color + "\n")
            print("Цвета сохранены в colors.txt")

        elif user == 5:
            break

        else:
            print("Введите одно из действий")
    except:
        print("Введите правильное действие")
