"""
Exercise 1: Tab completion warm-up

None of the functions below do anything yet. Each one has a comment
describing what it should do and a `pass` placeholder instead of real
code.

For each function: delete the `pass` line, put your cursor there, and
start typing. Once GitHub Copilot is enabled, it will offer a suggestion as gray "ghost
text." Press Tab to accept it, Esc to dismiss it, or keep typing your
own version.
"""


def square(n):
    # Return the square of n.
    return n * n


def is_prime(n):
    # Return True if n is prime, False otherwise.
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def filter_by_length(strings, min_length):
    # Return only the strings from `strings` that are at least
    # `min_length` characters long.
    return [s for s in strings if len(s) >= min_length]


def reverse_sentence(sentence):
    # Reverse the word order of `sentence`.
    # "hello world" becomes "world hello".
    return " ".join(sentence.split()[::-1])
