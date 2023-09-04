# lamda and + operation

log = list(map(str, input().split(',')))
print(log)

def sortLogFile(logs : list[str])->list[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))

    return letters + digits

print(sortLogFile(log))

