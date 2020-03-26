def paper_doll(text):
"Given a string, return a string where for every character in the original there are three characters"
    NewText=''
    for lettre in text:
        NewText = NewText + lettre*3
    return NewText