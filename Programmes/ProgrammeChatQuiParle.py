def ChatQuiParle (dialogue):
    #Dessine un chat disant quelquechose
    traits = '-' * (len(dialogue) +1)
    print ('{0:>11}{1}'.format('-', traits))
    print ('{0:>11}{1}{2}'.format('< ', dialogue, ' >'))
    print ('{0:>11}{1}'.format('-', traits))
    print ('{0:>10}'.format('/'))
    print (' /\_/\  /')
    print ('( o.o )')
    print (' > ^ <')

def main ():
    dialogue = input('Que dit le chat ? ')
    ChatQuiParle(dialogue)

if __name__ == '__main__':
    main()
