from typing import List
from address_book import AddressBook, Record


# Декоратор обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            # показуємо зміст помилки валідації (телефон/дата)
            return f"Error: {e}"
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    msg = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        msg = "Contact added."
    if phone:
        record.add_phone(phone)
    return msg


@input_error
def change_phone(args: List[str], book: AddressBook) -> str:
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    if record.edit_phone(old_phone, new_phone):
        return "Phone number updated."
    return "Phone not found."


@input_error
def show_phones(args: List[str], book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    phones = ", ".join(p.value for p in record.phones) if record.phones else "—"
    return f"{record.name.value}: {phones}"


@input_error
def show_all(args: List[str], book: AddressBook) -> str:
    if not book.data:
        return "No contacts yet."
    return "\n".join(str(rec) for rec in book.data.values())


@input_error
def add_birthday(args: List[str], book: AddressBook) -> str:
    name, bday_str, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.add_birthday(bday_str)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    if record.birthday:
        return f"{name}'s birthday is {record.birthday.value}"
    return f"{name} has no birthday set."


@input_error
def birthdays(args: List[str], book: AddressBook) -> str:
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays this week."
    return "Upcoming birthdays:\n" + "\n".join(upcoming)
