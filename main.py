text = []
text2 = []
watched_films_index_list = []
need_to_watch_films_index_list = []
watched_films_index = 0
need_to_watch_films_index = 0

with open('text.txt', 'r', encoding='utf-8') as f: # считываем данные из файла построчно в список
    text = f.readlines()
#print(text)

for i in range(len(text)): # убираем лишние строки
    if (text[i] != '\n') and (('---' in text[i]) != True):
        text2.append(text[i])
#print(text2)

for i in range(len(text2)): # узнаем индекс начала списка фильмов из текстового файла (которые надо посмотреть)
    if '### Фильмы:' in text2[i]:
        need_to_watch_films_index = i
#print(need_to_watch_films_index)

for i in range(len(text2)): # узнаем индекс начала списка фильмов из текстового файла (которые уже просмотрены)
    if '### **Просмотрено:**' in text2[i]:
        watched_films_index = i
#print(watched_films_index)

for i in range(need_to_watch_films_index + 1, watched_films_index): # в этот список всавляем фильмы, которые надо посмотреть
    need_to_watch_films_index_list.append(text2[i])
#print(need_to_watch_films_index_list)

for i in range(watched_films_index + 1, len(text2)): # в этот список всавляем фильмы, которые просмотрены
    watched_films_index_list.append(text2[i])
#print(watched_films_index_list)

for i in range(len(watched_films_index_list)): # добавляем АЙДИШНИК к каждой строке и выделяем фразой строки, где есть *
    if '*' in watched_films_index_list[i]:
        watched_films_index_list[i] = '(СТОИТ ПОСМОТРЕТЬ)' + ' ' + watched_films_index_list[i]
    watched_films_index_list[i] = str(i + 1) + ' ' + watched_films_index_list[i]

for i in range(len(need_to_watch_films_index_list)): # добавляем АЙДИШНИК к каждой строке
    need_to_watch_films_index_list[i] = str(i + 1) + ' ' + need_to_watch_films_index_list[i]

with open('watched_films.txt', 'w', encoding='utf-8') as f2: # в этот файл записываем фильмы, которые уже посмотрели
    for line in watched_films_index_list:
        f2.write(line)

with open('need_to_watch_films.txt', 'w', encoding='utf-8') as f2: # в этот файл записываем фильмы, которые надо посмотреть
    for line in need_to_watch_films_index_list:
        f2.write(line)