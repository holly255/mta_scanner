# — coding: utf-8 —
import platform
import os


def data():
    print("System information: ")
    print('System :', platform.system())  # Отображение названия системы / ОС
    print('Distribution :', platform.platform())  # Показать название ОС, версию и кодовое имя
    print(platform.architecture())  # Показать архитектуру машины
    print('Node :', platform.node())  # Показать имя компьютера в сети
    print('Machine :', platform.machine())  # Показать тип машины
    print('Processor :', platform.processor())  # Показать имя процессора
