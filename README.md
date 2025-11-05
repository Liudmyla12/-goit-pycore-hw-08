# 🧠 goit-pycore-hw-08 — Serialization + Assistant Bot

Завдання: зберігати адресну книгу на диск (**pickle**) та відновлювати її при запуску.  
Бот підтримує роботу з контактами, телефонами, днями народження та показує найближчі дні народження на тиждень.

## 📁 Структура проєкту

```text
goit-pycore-hw-08/
├── .gitignore
├── README.md
├── address_book.py      # Field, Name, Phone, Birthday, Record, AddressBook (+get_upcoming_birthdays)
├── bot_commands.py      # add, change, phone, all, add-birthday, show-birthday, birthdays
├── main.py              # CLI-бот + збереження/відновлення через pickle
└── commands.txt         # (опційно) сценарій для автоперевірки

```

> 🗂️ Файл даних `addressbook.pkl` створюється автоматично при виході з програми та **ігнорується Git’ом**.

---

## 🛠️ Вимоги

- Python **3.12** (рекомендовано; перевірено)
- Жодних додаткових пакетів — використовується стандартна бібліотека **pickle**

---

## ▶️ Запуск

### 💻 Windows / PowerShell / VS Code Terminal

```powershell
py main.py
```

### 🐧 macOS / Linux

```bash
python3 main.py
```

Після команди **`exit`** дані збережуться у `addressbook.pkl`.
При наступному запуску вони **автоматично відновляться**.

---

## 📚 Команди бота

| Команда                            | Опис                                    |
| ---------------------------------- | --------------------------------------- |
| `hello`                            | Вітання                                 |
| `add [ім'я] [телефон]`             | Додати контакт або телефон (10 цифр)    |
| `change [ім'я] [старий] [новий]`   | Змінити номер телефону                  |
| `phone [ім'я]`                     | Показати телефони контакту              |
| `all`                              | Показати всі контакти                   |
| `add-birthday [ім'я] [ДД.ММ.РРРР]` | Додати або оновити день народження      |
| `show-birthday [ім'я]`             | Показати дату народження                |
| `birthdays`                        | Показати дні народження протягом 7 днів |
| `exit` / `close`                   | Зберегти та вийти                       |

---

### ✅ Валідація

- **Телефон** — 10 цифр
  ⮕ `Error: Phone must contain exactly 10 digits`
- **Дата народження** — формат `DD.MM.YYYY`
  ⮕ `Error: Invalid date format. Use DD.MM.YYYY`

---

## 🔎 Приклади

### 🟢 1) Живий режим (вручну)

```text
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
```

---

### 🧠 2) Автоматична перевірка через `commands.txt`

📄 **Вміст файлу:**

```text
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
```

⚙️ **Запуск у PowerShell:**

```powershell
Get-Content ".\commands.txt" | py ".\main.py"
```

📋 **Очікуваний результат:**

```text
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
```

---

## 💾 Серіалізація (pickle)

📦 При запуску:

- `main.py` викликає `load_data()` — відновлює адресну книгу з `addressbook.pkl`
- Якщо файлу немає, створюється новий об’єкт `AddressBook`

🧱 При виході:

- Викликається `save_data()` — зберігає всі дані через `pickle.dump()`

Це гарантує, що адресна книга **повністю зберігається між сеансами**.

---

<p align="center">
  <sub>GOIT Python Core — HW-08 · Assistant Bot Project</sub><br>
  <sub>© 2025 All rights reserved</sub>
</p>
