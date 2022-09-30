from gtts import gTTS
with open('pride.txt', 'r', encoding="utf8") as f:
    t = gTTS(f.read(), lang = 'en')
t.save('pride.mp3')
print('Done')