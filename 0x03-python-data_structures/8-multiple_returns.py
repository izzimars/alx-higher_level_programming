#!bin/bash/python3
def multiple_returns(sentence):
    """A function that tries the multiple return power of a tuple.

    Args:
        sentence: string

    Return: tuple
    """
    lent = len(sentence)
    if lent == 0:
        return (lent, None)
    return(lent, sentence[0])
