
# Import the required module for text   
# to speech conversion 
import pyttsx3 
  
# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)
engine.setProperty('rate',120)
text = "I don't want it to go really slow just slow enough to be easy for a non native speaker to understand the words in the words list. Also if it is impossible to do it using the pyttsx module can you suggest a module that can do that?"
# say method on the engine that passing input text to be spoken 
engine.say(text) 
  
# run and wait method, it processes the voice commands.  
engine.runAndWait() 