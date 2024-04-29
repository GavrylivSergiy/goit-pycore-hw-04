import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для підтримки кольорів у консолі
init()

def visualize_directory_structure(directory_path, indent=0):
    """
    Функція для візуалізації структури директорії з використанням рекурсії.

    :param directory_path: Шлях до директорії
    :param indent: Відступ для візуального відображення рівня вкладеності
    """
    directory = Path(directory_path)
    
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + "Помилка: Зазначений шлях не існує або не є директорією." + Style.RESET_ALL)
        return
    
    # Виводимо ім'я поточної директорії
    print(Fore.BLUE + '  ' * indent + '+ ' + directory.name + Style.RESET_ALL)
    
    # Виводимо файли поточної директорії
    for file in directory.iterdir():
        if file.is_file():
            print(Fore.GREEN + '  ' * (indent + 1) + '- ' + file.name + Style.RESET_ALL)
    
    # Рекурсивно викликаємо функцію для піддиректорій
    for sub_dir in directory.iterdir():
        if sub_dir.is_dir():
            visualize_directory_structure(sub_dir, indent + 1)

# Отримуємо шлях до директорії з аргументів командного рядка
if len(sys.argv) != 2:
    print(Fore.RED + "Помилка: Будь ласка, вкажіть шлях до директорії як аргумент командного рядка." + Style.RESET_ALL)
else:
    directory_path = sys.argv[1]
    visualize_directory_structure(directory_path)