🧠 goit-pycore-hw-08 — Serialization + Assistant Bot

Завдання:
Зберігати адресну книгу на диск (pickle) та відновлювати її при запуску.
Бот підтримує роботу з контактами, телефонами, днями народження
та показує найближчі дні народження.

📁 Структура проєкту

goit-pycore-hw-08/
├── .gitignore # кеші, venv, IDE-файли, addressbook.pkl
├── README.md # цей файл
├── address_book.py # Field, Name, Phone, Birthday, Record, AddressBook (+ get_upcoming_birthdays)
├── bot_commands.py # add, change, phone, all, add-birthday, show-birthday, birthdays
├── main.py # CLI-бот + збереження/відновлення з addressbook.pkl
└── commands.txt # (опційно) сценарій для автоперевірки
⚙️ Файл даних addressbook.pkl створюється автоматично та ігнорується Git’ом.

🛠️ Вимоги

Python 3.12 (рекомендовано, перевірено)

Додаткові пакети не потрібні — використовується стандартна бібліотека pickle

▶️ Запуск
Windows / PowerShell / VS Code Terminal
py main.py

macOS / Linux
python3 main.py

Після завершення командою exit дані збережуться у addressbook.pkl.
При наступному запуску — автоматично відновляться.

📚 Команди бота
| Команда | Опис |
| ---------------------------------- | ------------------------------------------------------- |
| `hello` | Вітання |
| `add [ім'я] [телефон]` | Додати новий контакт або телефон до існуючого (10 цифр) |
| `change [ім'я] [старий] [новий]` | Змінити номер телефону |
| `phone [ім'я]` | Показати телефони контакту |
| `all` | Показати всі контакти |
| `add-birthday [ім'я] [ДД.ММ.РРРР]` | Додати або оновити дату народження |
| `show-birthday [ім'я]` | Показати дату народження |
| `birthdays` | Показати дні народження протягом наступних 7 днів |
| `exit` або `close` | Зберегти та вийти |

🧾 Валідація

Телефон — рівно 10 цифр
→ Error: Phone must contain exactly 10 digits

День народження — формат DD.MM.YYYY
→ Error: Invalid date format. Use DD.MM.YYYY

🔎 Приклади
🟢 Живий режим (вручну)
Welcome to the assistant bot!
Enter a command: add Mila 1234567890
Contact added.
Enter a command: add-birthday Mila 10.04.1995
Birthday added for Mila.
Enter a command: phone Mila
Mila: 1234567890
Enter a command: all
Contact name: Mila, phones: 1234567890, birthday: 10.04.1995
Enter a command: exit
Good bye!

🧠 Автоматична перевірка зі скрипту (commands.txt)

Файл commands.txt:
hello
add Anna 5551112223
add-birthday Anna 06.11.1990
add Max 5551112224
add-birthday Max 08.11.1988
add Leo 5551112225
add-birthday Leo 12.11.1992
phone Anna
show-birthday Max
birthdays
all
exit

Запуск:
Get-Content ".\commands.txt" | py ".\main.py"

✅ Результат перевірки

Тестування виконано як у живому режимі, так і через файл commands.txt.
Усі команди працюють стабільно, включно з серіалізацією через pickle.
Після перезапуску програми адресна книга повністю відновлюється,
а метод get_upcoming_birthdays() правильно показує дні народження на наступному тижні.

Приклад виводу (автоматичний режим):
Welcome to the assistant bot!
Enter a command: How can I help you?
Enter a command: Contact added.
Enter a command: Birthday added for Anna.
Enter a command: Contact added.
Enter a command: Birthday added for Max.
Enter a command: Contact added.
Enter a command: Birthday added for Leo.
Enter a command: Anna: 5551112223
Enter a command: Max's birthday is 08.11.1988
Enter a command: Upcoming birthdays:
Anna — 06.11.1990
Max — 08.11.1988
Leo — 12.11.1992
Enter a command: Contact name: Mila, phones: 1234567890, birthday: 10.04.1995
Contact name: John, phones: 1234567890, birthday: 15.06.1990
Contact name: Anna, phones: 5551112223, birthday: 06.11.1990
Contact name: Max, phones: 5551112224, birthday: 08.11.1988
Contact name: Leo, phones: 5551112225, birthday: 12.11.1992
Enter a command: Good bye!

<p align="center"> <sub>GOIT Python Core — HW-08 · Assistant Bot Project</sub><br> <sub>© 2025 All rights reserved</sub> </p>
