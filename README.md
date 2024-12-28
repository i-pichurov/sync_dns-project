Скрипт делает запросы нужной DNS-записи ко всем NS-серверам указанного домена и принтит результат в командную строку.

# Required
Права Администратора к устройству  
Python 3.9 или новее  
Homebrew 4.4.10 или новее  
Poetry: 1.8.3 или новее  
    
# Installing

Скачиваем и распаковываем архив с главной страницы репозитория через кнопку "Code" -> "Download ZIP"

Далее установка и взаимодействие со скриптом происходит путем ввода команд в строку Терминала.

Проверяем, установлен ли на устройстве Python3, командой:
    
    python3 --version
Если нет - ставим через приложение Self Service.

Ставим Homebrew (это менеджер пакетов для macOS, который упрощает установку многих программ), с помощью команды:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Проверяем наличие и версию командой:
    
    brew --version

Ставим Poetry (это инструемент для управления зависимосятми, публикации и установки пакетов Python) с помощью команды:

    brew install poetry
Проверяем наличие и версию командой:

    poetry --version

Открываем директорию проекта:
    
    cd sync_dns-project-main

Устанавливаем зависимости проекта с помощью poetry:
    
    poetry install

# Работа со скриптом

Открываем директорию проекта, если мы еще не в ней (проверить, где мы сейчас в терминале, можно командой 'pwd'):
    
    cd sync_dns-project
    
Запускаем настроенное виртуальное окружение:
    
    poetry shell

Окружение готово для использования в нем нашего скрипта. Для получения справки об использовании скрипта используем команду:
    
    check_dns -h

Пример применения скрипта и его результат:

    check_dns mail.ru TXT mail.ru
    #Result:
    ns1.mail.ru. mail.ru TXT _globalsign-domain-verification=n57ZlrTnnCnyCw1NMLRcU6gFwa3ykYc-KMqjCOSAOP
    ns1.mail.ru. mail.ru TXT v=spf1 redirect=_spf.mail.ru
    
    ns2.mail.ru. mail.ru TXT v=spf1 redirect=_spf.mail.ru
    ns2.mail.ru. mail.ru TXT _globalsign-domain-verification=n57ZlrTnnCnyCw1NMLRcU6gFwa3ykYc-KMqjCOSAOP

Для выхода из вирутального окружения используем команду:
    
    exit

Почему нельзя просто установить скрипт в общую среду Python на устройстве? - Гипотетически можно, НО:  
Виртуальное окружение в Python создаёт изолированную среду для проекта, что помогает избежать конфликтов между зависимостями и облегчает управление ими.
