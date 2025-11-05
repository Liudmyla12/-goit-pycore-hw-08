from __future__ import annotations

from collections import UserDict
from datetime import datetime, date
from typing import Optional


class Field:
    """Базове поле запису (має значення та текстове представлення)."""

    def __init__(self, value: str):
        self._value: Optional[str] = None
        self.value = value  # пройти через сеттер

    @property
    def value(self) -> str:
        return self._value  # type: ignore[return-value]

    @value.setter
    def value(self, v: str) -> None:
        self._value = v

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value!r})"


class Name(Field):
    """Ім'я контакту (обов'язкове поле)."""

    def __init__(self, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Phone(Field):
    """Телефон з валідацією рівно на 10 цифр."""

    @staticmethod
    def _normalize(s: str) -> str:
        return "".join(ch for ch in s if ch.isdigit())

    @Field.value.setter  # перевизначений сеттер з валідацією
    def value(self, v: str) -> None:
        digits = self._normalize(v)
        if len(digits) != 10:
            raise ValueError("Phone must contain exactly 10 digits")
        self._value = digits

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Phone):
            return self.value == other.value
        if isinstance(other, str):
            try:
                return self.value == Phone(other).value
            except ValueError:
                return False
        return False


class Birthday(Field):
    """Дата народження у форматі DD.MM.YYYY з валідацією."""

    @staticmethod
    def _parse(v: str) -> date:
        try:
            return datetime.strptime(v, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    @Field.value.setter
    def value(self, v: str) -> None:
        # перевірка формату; зберігаємо як оригінальний рядок
        _ = self._parse(v)
        self._value = v


class Record:
    """Запис контакту: ім'я + список телефонів + (опційно) день народження."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Optional[Birthday] = None

    # телефони
    def add_phone(self, phone: str) -> Phone:
        p = Phone(phone)
        self.phones.append(p)
        return p

    def find_phone(self, phone: str) -> Optional[Phone]:
        try:
            probe = Phone(phone)
        except ValueError:
            return None
        for p in self.phones:
            if p == probe:
                return p
        return None

    def remove_phone(self, phone: str) -> bool:
        target = self.find_phone(phone)
        if target:
            self.phones.remove(target)
            return True
        return False

    def edit_phone(self, old: str, new: str) -> bool:
        target = self.find_phone(old)
        if not target:
            return False
        target.value = Phone(new).value  # валідація у Phone
        return True

    # день народження
    def add_birthday(self, birthday_str: str) -> Birthday:
        b = Birthday(birthday_str)
        self.birthday = b
        return b

    def __str__(self) -> str:
        phones_part = ", ".join(p.value for p in self.phones) if self.phones else "—"
        bday_part = self.birthday.value if self.birthday else "—"
        return f"Contact name: {self.name.value}, phones: {phones_part}, birthday: {bday_part}"


class AddressBook(UserDict):
    """Колекція записів (name -> Record)."""

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False

    # --- ДОДАНО для HW-08: найближчі дні народження ---
    def get_upcoming_birthdays(self) -> list[str]:
        """
        Повертає список рядків "Name — DD.MM.YYYY" для контактів,
        у яких день народження протягом наступних 7 днів (включно).
        """
        today = datetime.today().date()
        upcoming: list[str] = []

        for record in self.data.values():
            if not record.birthday:
                continue
            try:
                bday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
            except ValueError:
                # пропускаємо некоректні значення, якщо хтось зіпсував файл вручну
                continue

            this_year = bday_date.replace(year=today.year)
            # якщо в цьому році вже минув — дивимось наступний рік
            if this_year < today:
                this_year = this_year.replace(year=today.year + 1)

            delta = (this_year - today).days
            if 0 <= delta <= 7:
                upcoming.append(f"{record.name.value} — {record.birthday.value}")

        return upcoming


