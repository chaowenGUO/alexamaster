with fileinput.FileInput('kernel-metadata.json', inplace=True) as file:
    for line in file:
        print(line.replace('VERSION', 'chat.js'), end='')
