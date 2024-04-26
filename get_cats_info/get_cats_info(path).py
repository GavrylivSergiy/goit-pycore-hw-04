
def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats_info

cats_info = get_cats_info(r"C:\Users\Acer\Documents\My_repo\goit-pycore-hw-04\get_cats_info\cats_file.txt")
print(cats_info)