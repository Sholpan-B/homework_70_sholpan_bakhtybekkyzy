Получение информации о конкретной задаче

Для получения информации о конкретной задаче, выполните GET-запрос к /api/tasks/{id}/, где {id} - это идентификатор задачи.
Например: http://127.0.0.1:8000/api/tasks/5/


Обновление информации о задаче

Для обновления информации о задаче, отправьте PUT-запрос на /api/tasks/{id}/ с JSON-телом, содержащим обновленные параметры задачи в следующем формате:
{
    "summary": "Новое краткое описание задачи",
    "description": "Новое подробное описание задачи",
    "project": 2,
    "status": 2,
    "type": 2
}


Удаление задачи

Для удаления задачи, выполните DELETE-запрос к /api/tasks/{id}/, где {id} - это идентификатор задачи.



Получение информации о конкретном проекте

Для получения информации о конкретном проекте, выполните GET-запрос к /api/projects/{id}/, где {id} - это идентификатор проекта.
Например: http://127.0.0.1:8000/api/projects/22/

Обновление информации о проекте

Для обновления информации о проекте, отправьте PUT-запрос на тот же URL, что и для получения информации о проекте (/api/projects/{id}/), указав в теле запроса новые данные проекта в формате JSON.

Удаление проекта

Для удаления проекта, выполните DELETE-запрос к /api/projects/{id}/, где {id} - это идентификатор проекта.



Superuser

login: sholpan;
password: sholpan



Project Manager: Bob, password: bob Team Leader: Kira, password: Kira Developer: Sara, password: sara
