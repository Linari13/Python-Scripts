def animal_crackers(text):
	"takes a two-word string and returns True if both words begin with same letter"
    ind = text.index(' ')
    return text[0] == text[ind+1]