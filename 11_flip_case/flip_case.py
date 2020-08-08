def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    for to_swap in phrase:
        if to_swap == to_swap.lower():
            to_swap = to_swap.upper();
        if to_swap == to_swap.upper():
            to_swap = to_swap.lower();
        return phrase