
with open(r'E:\PycharmProjects\text_classify\venv\Include\7days.txt','r',encoding='utf-8') as f:
    i = 0
    while True:
        i += 1
        print(1)
        line = f.readline()
        if not line:
            break

str  = "asd|asd"
print(str.split(r'|'))