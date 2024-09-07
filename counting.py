import  time

time.sleep(0.2)
print("hey type something and this program will count words\n")

time.sleep(1)
User_Words = input("text to count words: ")

def counting(user_text):
    key_list={} #this make word and key (word:key)

    splited_words = user_text.split() #splitet text into words and put in list

    for c_words in splited_words:
        c_words = c_words.lower().strip(('.,!?;"\'()[]{}:')) #make every wor small and remove symbol for star and end

        if c_words in key_list: #if kay lsit contains word form c words add1 else add this word
            key_list[c_words] += 1 #if lsic contains add 1
        else:
            key_list[c_words] = 1 #if not add this owrd to list
    return key_list



counted = counting(User_Words)

print("this is yours counted words")

for word, ammont in counted.items(): # items retur pair (value - key) and u can editi it sperate (word, ammont)
    print(f'{word} : {ammont}') #f'{x} : {x}' remove {} amd put it i refular text


input("press anything to exit")
