def check_vowel_consonants(alphabhet):
    alphabhet=alphabhet.lower()

    if len(alphabhet)==1 and alphabhet.isalpha():
        if alphabhet in 'aeiou':
            print("it is a vowel")
        else:
            print("it is a consonants")
    else:
        print("enter a single aplhabet")


alphabhet=input("enter a alphabet:")

check_vowel_consonants(alphabhet)