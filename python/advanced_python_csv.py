import advanced_python_regex as regex

with open('/Users/samfunk/ds/metis/metisgh/prework/dsp/python/emails.csv', 'w') as f:
    for e in regex.email:
        f.write(e + '\n')
