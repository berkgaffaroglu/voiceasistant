import speech_recognition as sr
import os,time
from selenium import webdriver
import pyttsx3

class AsistantBot:
    def __init__(self, name, gender, rate):
        self.name = name
        self.gender = gender
        self.rate = rate
        self.standby = True

    def getInformation(self,text):
        if 'what is your name' in text:
            self.response(f'My name is {self.name}')
        elif 'how old are you' in text:
            self.response(f"I don't want to tell you my age.")
        elif "who are you" in text:
            self.response(f'I am an asistant to help you in order to improve your life quality.')
        elif "hi" in text:
            self.response('Hi!')
        else:
            return False


    def response(self,text):
        print(text)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        #0 man 1 woman
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()


    def get_text(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                text = ''
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio, language=('en-US'))
                    print(text)
                    return text
                except sr.UnknownValueError:
                    if self.standby == False:
                        self.response("I couldn't understand what you mean.")
                    return -1

                except sr.RequestError:
                    if self.standby == False:
                        self.response('There is something wrong with my services.')
                    return -1


    def action(self,text):
        text = text.strip().lower()
        if 'youtube' in text:
            self.response('What do you want to search in Youtube?')
            searchKeyword = self.get_text() # Asking for the keywords that user want to search for.
            if searchKeyword != -1:
                searchKeyword = f'{searchKeyword}'
                BASE_URL = "https://www.youtube.com/results?search_query={}"
                url = self.queryFriendly(searchKeyword, BASE_URL)
                self.searchInWeb(url)


    def queryFriendly(self, keywords, BASE_URL):
        self.response(f'Here is what I have found about {keywords}')
        keywords = keywords.replace(' ','+')
        url = (BASE_URL.format(keywords)) # Creating the url with keywords
        return url

    def searchInWeb(self,url):
        #Open browser
        browser = webdriver.Chrome() 
        #Search for the URL
        browser.get(url)

    def run(self):
        self.standby = False 
        # Wait for the order.
        request = self.get_text() 
        # Checking if call is valid
        if request != -1: 
            notRequireAction = self.getInformation(request) # Is it a simple question or does it require action
            if not notRequireAction: # If it does require action 
                self.action(request) # Then action.
                        



if __name__ == "__main__":
    bot = AsistantBot('jack',0,125)
    while True:
        running = bot.run()
            
            


    
    


                
            

