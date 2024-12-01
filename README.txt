
У РЕЗУЛЬТАТ.pdf - скріни результатів або на гугл диск посилання з цима результами:
https://docs.google.com/document/d/1Dj2X6cg5v0CshCmmJVyVtCLKUW1PTS8X/edit?usp=sharing&ouid=108293263267985466466&rtpof=true&sd=true

Тут(рідмі) опис структури та функціоналу


src

 main.py

fastapi dev main.py  - запуск

StaticFiles - дозволяє обробляти статичні файли (для зображення)
Jinja2Templates - забезпечує рендеринг HTML-шаблонів

from api import info, get_all, get_new, get_known, search - ендпоінти у папці api

Шаблон розташований в папці templates, яка знаходиться на одному рівні з файлом main.py

Статичні файли розташовані в папці static. Вони доступні за URL /static (зображення)



 api
  info.py

секція "General Info"

@router.get('/info') - декоратор реєструє маршрут для обробки GET-запитів за шляхом /info

def info() - ця функція повертає дані у форматі JSON (інформацію про автора і додаток)



  get_all.py

datetime та timedelta - працюють з датами, щоб визначити діапазон дат

секція "Last N Days CVEs" 

 data
Вказую шлях до JSON-файлу (data), який містить дані про вразливості

@router.get("/get/all") - декоратор реєструє ммаршрут /get/all

timespan - gараметр запиту (Query), який визначає кількість днів для аналізу (за замовчуванням взяла 10 днів, бо 5 вже не актуально)

відкриваю JSON-файл та отримую data.get("vulnerabilities", [])

розраховується дата початку (start_date), від якої потрібно шукати дані та фільтруються дані, залишаючи тільки ті, де дата додавання яких (dateAdded) знаходиться у вказаному діапазоні

Повертаю максимум 40 перших вразливостей, знайдених у діапазоні за умовою



  get_new.py

секція "10 Latest CVEs"

@router.get("/get/new") - шлях /get/new

тут просто API повертає 10 останніх записів CVE з JSON-файлу, відсортованих за датою додавання (dateAdded)

sorted() - cортує список вразливостей
key=lambda x: x.get("dateAdded", "") - dикористовує поле dateAdded як критерій сортування
reverse=True - cортує у зворотному порядку, щоб найновіші записи йшли першими

Повертаю перші 10 записів із відсортованого списку

  get_known.py

секція "Known Ransomware СVEs"

шукаю вразливості поле knownRansomwareCampaignUse має значення "Known"

створюю список known_cve, що містить лише ті записи, у яких поле knownRansomwareCampaignUse має значення "Known"

Використовую генератор списків (list comprehension) для фільтрації

обмеження результатів до максимум 10 записів

  search.py

секція "Search CVEs"

URL /search

query - параметр запиту, обов'язковий, описується як "Keyword to search for". Наприклад: /search?query=unknown

cтворюю список filtered_cve із записів, які відповідають умові:
json.dumps(cve) - запис перетворюєм у стрінгу  для пошуку ключового слова в усіх полях
re.search():
rf'\b{re.escape(query)}\b' - рв для пошуку слова query як ОКРЕМОГО терміна
\b - для межі слова 
re.escape(query) - екранізує спеціальні символи у query, якщо вони є
re.IGNORECASE - ігнору регістрів під час пошуку


 templates
  index.html - для розмітки

uvicorn main:app --reload - запуск




