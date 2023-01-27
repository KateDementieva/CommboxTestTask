from collections import defaultdict

results_dict = defaultdict(list)


def add_result(word, chunk_number, positions):
    for place in positions:
        for offset in place["chars_offset"]:
            results_dict[word].append([chunk_number * 10 + place["line"], offset])


def print_all_results():
    for key, values in results_dict.items():
        print(key + "--->")
        for value in values:
            print("lineOffset = " + str(value[0]), "charOffset = " + str(value[1]))
