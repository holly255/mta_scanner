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
<<<<<<< HEAD


def installed():
    dpkg_list = shlex.split("dpkg-query -Wf '${Installed-Size}\t${Package}\n'")
    process = subprocess.Popen(dpkg_list, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("List installed application: ")
    print(output.decode('UTF-8'))
=======
    print('Version :', platform.version())  # Показать версию системы
    print('Platform :', platform.platform())  # Показать базовую платформу
    print('Release :', platform.release())  # Показать инфор
>>>>>>> f16042c88591ac5f928c2820c3d122bfba3648ba
