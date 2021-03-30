from pprint import pprint

filenames = ['1.txt', '2.txt', '3.txt']


def read_files_to_dict(file_list):
    # Функция читает содержимое файлов в словарь, где ключом является имя файла, а значением массив строк.
    # Читать сразу все в память может быть не оптимально, если мы знаем, что файлы могут быть большого объема или их очень много.
    # Но в условиях задачи ничего подобного не было.

    files_content = dict()
    files_lines_count = dict()

    for filename in file_list:
        with open(filename, encoding="utf-8") as f:
            file_lines = [line.strip() for line in f]
            files_content.update({filename: file_lines})
            files_lines_count.update({filename: len(file_lines)})
    # pprint(files_lines_count)
    return files_content


def write_file_sorted(files_content):
    files_content_sorted = sorted(files_content.values(), key=len)

    # Такой способ сортировки будет работать в версиях Python до 3.7, так как в них не запоминалось последовательность добавления ключей в словари.
    # В новых версиях можно использовать такую конструкцию:
    # files_content_sorted = dict(sorted(file_content.items(), key=lambda x: len(x[1])))
    # на выходе получим отсортированный словарь
    with open("output.txt", "w") as f:
        for content_lines_sorted in files_content_sorted:
            for filename, content_lines in files_content.items():
                if content_lines == content_lines_sorted:
                    f.write(filename + '\n')
                    f.write(str(len(content_lines_sorted)) + '\n')
                    f.write('\n'.join(content_lines_sorted) + '\n')
                    break
    return 1


files_content_dict = read_files_to_dict(filenames)
write_file_sorted(files_content_dict)

