def uppercase_string(input_string):
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


