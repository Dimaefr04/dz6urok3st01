from fastapi import FastAPI

app = FastAPI()
books_db = [
    {
        "title": "Дюна",
        "author": "Фрэнк Герберт",
        "genre": "Научная фантастика"
    },
    {
        "title": "Марсианин",
        "author": "Энди Вейер",
        "genre": "Научная фантастика"
    },
    {
        "title": "451 по Фаренгейту",
        "author": "Рэй Брэдбери",
        "genre": "Антиутопия"
    },
    {
        "title": "Гарри Поттер и философский камень",
        "author": "Дж. К. Роулинг",
        "genre": "Фэнтези"
    }
]

@app.get("/")
def read_root():
    return {
        "Название API": "API библиотеки",
        "Путь к книгам": "/books"
    }

@app.get("/books")
def get_books():
    return books_db