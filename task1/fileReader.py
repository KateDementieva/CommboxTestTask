
def search_lines(file_name):
    with open(file_name, 'r') as file:
        file_content = file.readlines()

    chunks = []
    for i in range(0, len(file_content), 10):
        chunks.append(file_content[i:i + 10])

    return chunks
