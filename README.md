# Laba1_Nginx


Лабораторная работа 1: Настройка Nginx
Описание работы

В рамках данной лабораторной работы было создано простое Flask-приложение, настроен веб-сервер Nginx, а также сгенерированы и настроены SSL-сертификаты для доменов project1.com и project2.com. Целью работы было освоение базовой конфигурации Nginx как обратного прокси-сервера для Flask-приложения с поддержкой HTTPS.

Цель работы:
    Настроить Nginx для обслуживания приложения.
    Создать самоподписанные SSL-сертификаты для доменов project1.com и project2.com.
    Настроить Nginx для поддержки HTTPS и корректной маршрутизации запросов к Flask-приложению.


Настройка Nginx

    Установлен веб-сервер Nginx.
    Настроен конфигурационный файл Nginx для маршрутизации запросов к Flask-приложению.
    Реализована поддержка двух доменов: project1.com и project2.com.

Запуск

    Nginx перезапущен для применения конфигурации: sudo systemctl restart nginx.
    Проверена доступность приложения через HTTPS по адресам https://project1.com и https://project2.com.


Итоги

    Успешно настроен Nginx как обратный прокси-сервер для Flask-приложения.
    Реализована поддержка HTTPS для двух доменов с использованием самоподписанных сертификатов.