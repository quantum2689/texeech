from gtts import gTTS

lang = "en"
text = "Hello world"

speech = gTTS(text=text,lang=lang,slow=False,tld="com.au")
speech.save("text.mp3")