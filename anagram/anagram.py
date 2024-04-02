def reverse_words(text: str) -> str:
    """
      Function that reverses all the words of input text and all non-letter symbols stay on the same places
    """
    reversed_words = []
    for word in text.split():
        stack = [el for el in word if el.isalpha()]
        reversed_word = ''.join(stack.pop() if el.isalpha() else el for el in word)
        reversed_words.append(reversed_word)
    return " ".join(reversed_words)


if __name__ == '__main__':
    cases = (
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", "")
    )

    for test, result in cases:
        assert reverse_words(test) == result
