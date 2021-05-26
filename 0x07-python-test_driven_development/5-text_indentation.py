#!/usr/bin/python3
"""a function with split a string dependithe charater
if it has a char like ?, ., and :
it would put two new lines
if the argument pass no it's a string TypeError
"""


def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters: ., ? and :
    args:
        text : (str) = the text to be converted
    if text is not a string raise an TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = 0
    while a < len(text):
        if text[a] == "." or text[a] == "?" or text[a] == ":":
            text = text[:(a + 1)] + "\n\n" + text[(a + 1):]
        a += 1
    new_text = text.splitlines(True)
    # print(new_text)
    for string in new_text:
        print(string.strip(" "), end="")
