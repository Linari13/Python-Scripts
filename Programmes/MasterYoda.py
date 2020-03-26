def master_yoda(text):
"Given a sentence, return a sentence with the words reversed"
    NewList = text.split(' ')
    NewList.reverse()
    textb = ' '.join(NewList)
    return  textb