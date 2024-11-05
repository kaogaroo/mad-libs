text = "Today I went to the zoo. I saw a(n) [adjective] [noun] jumping up and down in its tree. He [verb, past tense] [adverb]."

openbracket = False
closedbracket = False

print("Welcome to Mad Libs! Do you want to create a sentence for someone else to add words to, or use the premade sentence? create/premade")
while True:
    answer = input()
    if answer == "create":
        print("Alright, input a sentence or paragraph.")
        print("Make sure to put words that will be replaced in brackets")
        while True:
            text = input("Mad lib:")
            openbracket = "[" in text
            closedbracket = "]" in text
            if openbracket and closedbracket:
                    print("Nice sentence!")
                    break
            else: 
                    print("I didn't find complete brackets. Try again.")
        break
    elif answer == "premade":
        print("Ok!")
        break
    else:
         print("I didn't get that")


libs = []

inbrackets = False
currentLib = ""

for char in text:
    if char == "[":
        currentLib = ""
        inbrackets = True
    elif char == "]":
        libs.append(currentLib)
        inbrackets = False
    elif inbrackets:
        currentLib += char

for i in range(len(libs)):
    text = text.replace(f"[{libs[i]}]", input(f"Tell me a(n) {libs[i]}: "))
    
print(text)