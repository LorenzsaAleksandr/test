def main(input: str) -> str:
    """
    Выполняет арифметическую операцию над двумя числами.

    Args:
        input: Строка с арифметическим выражением (например, "1 + 2").

    Returns:
        Строка с результатом выполнения операции.

    Raises:
        ValueError: Если ввод некорректен (неверный формат, числа вне диапазона).
    """
    try:
        # Разделяем строку на операнды и оператор
        a, operator, b = input.split()

        # Проверяем, что числа в диапазоне от 1 до 10
        if not (1 <= int(a) <= 10 and 1 <= int(b) <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10.")

        # Выполняем операцию
        a = int(a)
        b = int(b)
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a // b  # Деление с отбрасыванием остатка
        else:
            raise ValueError("Неверная операция.")

        return str(result)

    except ValueError as e:
        raise ValueError(f"Ошибка: {e}")


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите математическую операцию (например, 1 + 2): ")
            result = main(user_input)
            print(result)
        except ValueError as e:
            print(f"Ошибка: {e}")
            break

