# читаем входные данные из файла
with open("input.txt") as f:
    s = f.readline().strip()

# проходим по строке и восстанавливаем исходную строку
result = ""
i = 0
while i < len(s):
    if s[i].isdigit():
        count = int(s[i])
        i += 1
        while i < len(s) and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1
        result += result[-1] * (count - 1)
    else:
        result += s[i]
    i += 1

# записываем результат в файл
with open("output.txt", "w") as f:
    f.write(result)
