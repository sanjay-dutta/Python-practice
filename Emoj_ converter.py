# Emoji converter
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😒"
}
output = ""
word = message.split(' ')
for word in words:
    output += emojis.get(word, word) + " "
print(output)