import os
from requests import get
from json import loads


# Перезагрузить компьютер

def rebootPC():
    os.system("shutdown /r /t 1")


# Выйти из системы
def logoutPC():

    os.system("shutdown /l")


# Внешний IP

def get_ip():
    ip = get("https://api64.ipify.org?format=json").text
    ip = loads(ip)["ip"]
    if ip == None or '':
        print("ERORR getting IP.")
    else:
        return ip

# Список пользователей
def get_users():
    os.system("net user")


# Диспетчер задач
def task_manager():
    os.system("tasklist")


# 
def arp():
    os.system("arp -a")


# Активные соединения
def get_active_connections():
    os.system("netstat")


#
def get_mac_adress():
    os.system("getmac")


#
def get_wifi_connections():
    os.system("netsh wlan show profiles")


#
def get_wifi_pass(wifi_name):
    try:
        os.system(f"netsh wlan show profile {wifi_name} key=clear")
    except:
        print("Please provide a wifi name as an argument.")


# Полная информация о системе
def systeminfo():
    os.system("systeminfo")

# Имя ПК
def get_hostname():
    os.system("hostname")
