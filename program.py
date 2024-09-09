import pywhatkit
from scrape import scrape

question = scrape()

pywhatkit.sendwhatmsg_instantly("+919467017811", question, 15)
