import csv
import re


with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)

new_contacts_list = []

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub = r'+7(\2)-\3-\4-\5 \6\7'

for i in contacts_list[1:]:
    data = ' '.join(i[:3]).split()
    i[0] = data[0]
    i[1] = data[1]
    if len(data) > 2:
        i[2] = data[2]
    i[5] = re.sub(pattern, sub, i[5])

for i in contacts_list:
    for j in contacts_list:
        if i[0] == j[0] and i[1] == j[1]:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]

for i in contacts_list:
    if len(i) > 7:
        i.reverse()
        i.remove('')
        i.reverse()

for i in contacts_list:
    if i not in new_contacts_list:
        new_contacts_list.append(i)

with open('phonebook.csv', 'w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
