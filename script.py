with open('readme.md', 'r') as file:
    content = file.read()


content = content.replace('Dynamic Programming', '###REPLACE###').replace('Docker', 'Dynamic Programming').replace('###REPLACE###', 'Docker', 1)


with open('README.md', 'w') as file:
    file.write(content)
