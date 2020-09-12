import avo

while True:
    text = input('avo >> ')
    if(text=="exit"):
        exit()
    result, error = avo.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
