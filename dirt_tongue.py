import re


standart_dirt = [1093, 1091, 1081, 124, 1073, 1083, 1103, 124, 1077, 1073, 124, 
                 1087, 1080, 1079, 1076, 124, 1105, 1073] # censored

standart_dirt = ''.join(chr(n) for n in standart_dirt)


def _get_search(pattern: str):
    """
    return function to search words with the pattern
    """
    @lru_cache()
    def hide_search(word: str) -> bool:
        return bool(re.search(pattern, word))

    return hide_search


def is_dirt(pattern: str=standart_dirt):
    """
    return function to search pattern in text
    """
    funk = _get_search(pattern)

    def hide_search(text: str) -> bool:
        for word in re.findall(r'\w+', text):
            if funk(word.lower()):
                return True
        
        return False

    return hide_search

