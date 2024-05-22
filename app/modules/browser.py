import webbrowser


# Открывает пустую вкладку браузера
def openBrowser():
    url = "https://"
    webbrowser.open(url)

    print('Browser has open')


# Открывает страницу по url
def openPage(url):
    webbrowser.get('windows-default').open("http://"+url)