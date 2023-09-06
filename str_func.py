def uppercase_string(input_string):
    """
    Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами.

    :param input_string: Входная строка
    :return: Строка с заглавными буквами
    """
    return input_string.upper()
def capitalize_first_letters(input_string):
    """
    Функция, которая делает заглавными первые буквы каждого слова в строке.

    :param input_string: Входная строка
    :return: Строка с первыми буквами каждого слова в верхнем регистре
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    capitalized_string = ' '.join(capitalized_words)
    return capitalized_string
