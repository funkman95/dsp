import advanced_python_regex as regex

faculty_dict = {}
for i, n in enumerate(regex.last_name):
    creds = [regex.degree[i], regex.tls[i], regex.email[i]]
    counter = regex.last_name.count(n)
    if i == 0:
        c = 0
        faculty_dict[n] = creds
    elif counter > 1:
        if c == 0:
            faculty_dict[n] = []
            faculty_dict[n].append(creds)
            c += 1
        else:
            faculty_dict[n].append(creds)
            c += 1
    else:
        faculty_dict[n] = creds
        c = 0

professor_dict = {}
for i, n in enumerate(regex.last_name):
    professor_dict.update({(regex.first_name[i], regex.last_name[i]): [regex.degree[i], regex.tls[i], regex.email[i]]})

s = sorted(professor_dict.items(), key=lambda item: item[0][1])
