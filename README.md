# back_front
back_front endpoints:

Получения списка новостей по методу GET --> https://sultan11.pythonanywhere.com
Получения деталей новости (detail) по методу GET --> https://sultan11.pythonanywhere.com/detail/2 #id новости
Создание новости (create) по методу POST --> https://sultan11.pythonanywhere.com/create/
Обновление новости (update) по методу POST --> https://sultan11.pythonanywhere.com/update/2 #id новости
Удаление новости (delete) по методу POST --> https://sultan11.pythonanywhere.com/delete/2 #id новости
Пример json строки для создания задания
    {
        "id": 1,
        "title": "1",
        "description": "1",
        "date": "2022-10-14T12:59:09.186457Z",
        "published": false
    }
И так далее по всем вашим endpoints
