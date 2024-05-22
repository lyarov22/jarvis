import platform


def print_system_info():
    print(f"Информация об архитектуре: {platform.architecture()}")
    print(f"Тип машины: {platform.machine()}")
    print(f"Сетевое имя компьютера: {platform.node()}")
    print(f"Сведения о базовой платформе: {platform.platform()}")
    print(f"Реальное имя процессора: {platform.processor()}")
    print(f"Номер и дата сборки Python: {platform.python_build()}")
    print(f"Версия компилятора Python: {platform.python_compiler()}")
    print(f"Ветвь SCM реализации Python: {platform.python_branch()}")
    print(f"Реализация Python: {platform.python_implementation()}")
    print(f"Ревизия SCM реализации Python: {platform.python_revision()}")
    print(f"Версия Python как строка: {platform.python_version()}")
    print(f"Версия Python как кортеж: {platform.python_version_tuple()}")
    print(f"Сведения о выпуске системы: {platform.release()}")
    print(f"Имя операционной системы: {platform.system()}")
    print(f"Сведения команды терминала uname: {platform.uname()}")
    print(f"Версия выпуска системы: {platform.version()}")

if __name__ == "__main__":
    print_system_info()
