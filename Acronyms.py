

def Acronyms():
    """An acronym is a short form of a word created by long words or phrases 
    such as NLP for natural language processing."""
    
    user_input = str(input("Enter a Phrase: "))
    splitted_phrase = user_input.split()
    acronyms = ''

    for word in splitted_phrase:
        acronyms = acronyms + word[0].upper()

    return acronyms






