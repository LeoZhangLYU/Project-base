with open("./demo1.txt", "r", encoding="utf-8") as f1:
    file_data_1 = f1.read()

with open("./demo2.txt", "r", encoding="utf-8") as f2:
    file_data_2 = f2.read()

with open("./demo3.txt", "w", encoding="utf-8") as f3:
    f3.write(file_data_1)
    f3.write(file_data_2)
