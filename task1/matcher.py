import re

from aggregator import add_result


def find_matches(chunks, words):
    for chunk_number, chunk in enumerate(chunks):
        for word in words:
            found_occurrence = find_all_words(word, chunk)
            if len(found_occurrence) > 0:
                add_result(word, chunk_number, found_occurrence)


def find_all_words(sub, strings):
    occurrence = []
    for string_number, string in enumerate(strings):
        if sub in string:
            occurrence.append({
                "line": string_number,
                "chars_offset": [m.start() for m in re.finditer(sub, string)]})
    return occurrence
