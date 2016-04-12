path = raw_input('Please Enter a file path: ')

f = open(path, 'r+')
text = f.read()

def replace_text():
    new_text = text.replace('Hello World', "O'Doyle Rules!")
    f.seek(0)
    f.write(new_text)
    f.truncate()
    f.close()

replace_text()
