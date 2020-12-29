# — coding: utf-8 —
import os
import sys
import glob
import shlex
import random
import datetime
import platform
import subprocess
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename

# ------------------Данные о системе------------------


def data():
    print("System information: ")
    print('System :', platform.system())  # Отображение названия системы / ОС
    print('Distribution :', platform.platform())  # Показать название ОС, версию и кодовое имя
    print(platform.architecture())  # Показать архитектуру машины
    print('Node :', platform.node())  # Показать имя компьютера в сети
    print('Machine :', platform.machine())  # Показать тип машины
    print('Processor :', platform.processor())  # Показать имя процессора
    print('Version :', platform.version())  # Показать версию системы
    print('Platform :', platform.platform())  # Показать базовую платформу
    print('Release :', platform.release())  # Показать информацию о выпуске системы

# ------------------Установленные пакеты------------------


def installed():
    dpkg_list = shlex.split("dpkg-query -Wf '${Installed-Size}\t${Package}\n'")
    process = subprocess.Popen(dpkg_list, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("List installed application: ")
    print(output.decode('UTF-8'))

 # ------------------Сравнение сканов------------------
    
    
def check():
    check_diff = shlex.split("diff backup_1.txt backup_2.txt")
    process = subprocess.Popen(check_diff, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("List of changes: ")
    print(output.decode('UTF-8'))
    
# ------------------Копирование файла------------------

    
def change(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            out_file.write(line)
        os.remove(input_file)

# ------------------Последний скан----------------  


def last_time():
    if os.path.exists("backup_1.txt"):
        with open('backup_1.txt') as f:
            last_time = f.readline()
    else:
        last_time="Сканирование ни разу не проводилось"
    return last_time

# ------------------Сканирование----------------
def new_scan():
    if os.path.exists("backup_1.txt"): #Если есть предыдущий скан
        sys.stdout = open("backup_2.txt", "w") #Запись в временный файл
        print(datetime.datetime.now().strftime('%Y-%m-%d__%H:%M:%S')) #Первая строчка - время
        data() #Сведения о системе
        installed() #Установленные пакеты
        sys.stdout.close()

        sys.stdout = open("differents.txt", "w")
        check() #Сравнение временного файла и последнего сканирования. Запись различия в файл different.txt
        sys.stdout.close()

        if not os.path.exists("Backups"): #Проверка на существование директории для резервного хранения
            os.mkdir(os.getcwd()+"/Backups/") #Создание директории для резервного хранения
        cwd = os.getcwd()+"/Backups/"
        change("backup_1.txt", cwd + datetime.datetime.now().strftime('%Y-%m-%d__%H:%M:%S')) #Копирование предыдущего скана в резервное хранилище
        change("backup_2.txt", "backup_1.txt") #Копирование временного файла в основной

    else:# Если предыдущего скана нет
        sys.stdout = open("backup_1.txt", "w")
        print(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) #Запись в новый файл
        data()
        installed()
        sys.stdout.close()

        sys.stdout = open("differents.txt", "w")
        print("Не найдено последних проверок")
        sys.stdout.close()
    
    
# ------------------Работа с графическим интерфейсом----------------


# ------------------Открыть скан----------------
def open_scan():
    new_scan() #Сканирование
    filepath = os.getcwd()+"/backup_1.txt" #Адрес файла
    txt_edit.delete("1.0", tk.END) #Очистить поле
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text) #Запись из файла
    window.title(f"MTA Scanner - {filepath}")
    last_scan_2 = tk.Label(fr_buttons, text=last_time())
    last_scan_2.grid(row=7, column=0, sticky="ew", padx=5)
    
# ------------------Открыть различия с предыдущим сканом----------------    
    
def open_diff():
    filepath = os.getcwd()+"/differents.txt" #Адрес файла
    txt_edit.delete("1.0", tk.END) #Очистить поле
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text) #Запись из файла
    window.title(f"MTA Scanner - {filepath}")
    
# ------------------Открыть резервный файл----------------
    
def open_file():
    """Открывает файл для редактирования"""
    os.chdir(os.getcwd()+"/Backups/")
    filepath = askopenfilename(
        filetypes=[("Copy", "*"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"MTA Scanner - {filepath}")
    os.chdir("../")
    
    
window = tk.Tk()
window.title("MTA Scanner") #Создаёт новое окно с заголовком

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1) #Устанавливают конфигурацию строк и столбцов
#Создают виджеты — текстовый бокс, рамку и кнопки.
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Сканировать", command=open_scan)
btn_save = tk.Button(fr_buttons, text="Проверить на наличие изменений", command=open_diff)
btn_open_2 = tk.Button(fr_buttons, text="Резервное хранилище", command=open_file)
last_scan = tk.Label(fr_buttons, text="Последнее сканирование: ")
last_scan_2 = tk.Label(fr_buttons, text=last_time())

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_open_2.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
last_scan.grid(row=6, column=0, padx=5)
last_scan_2.grid(row=7, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
