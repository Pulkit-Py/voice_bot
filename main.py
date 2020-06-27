from speech import take
from wish import wishme
from speek import sp
from chatbot import chatty
import  wikipedia
import webbrowser
import os
import random
import datetime
def main():
    wishme()
    while(True):
        query = take().lower()
        if "None" not in query:
            value = chatty(query)
            if value is not None:
                print("jarvis : "+ value)
                sp(value)
            else:
                if "search" in query:
                    try:
                        sp("searching....")
                        result = wikipedia.summary(query,sentences=1)
                        print("Jarvis: "+result)
                        sp(result)
                    except Exception as e:
                        sp("soory i didn't find anything try agin")
                elif "open" in query:
                    chrome_path =" C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                    query = query.replace("open","")
                    res = query.split()
                    for i in res:
                        if ".com" in i:
                            sp("sure sir")
                            webbrowser.get(chrome_path).open(i)
                elif "calculate" in query:
                    query = query.replace("into","*")
                    query = query.replace("multiply","*")
                    query = query.replace("divide","/")
                    query = query.replace("by","/")
                    res = query.split()
                    temp = []
                    for i in res:
                        if i.isdigit() or '+'in i or "*" in i or '-' in i or '/' in i:
                            temp.append(i)
                    answer = ''.join(temp) 
                    ans = eval(answer)
                    print("jarvis: the answer is "+ str(ans))
                    sp("the answe is "+ str(ans))
                elif 'play music' in query:
                    music_dir = "F:\\Playlist"
                    songs = os.listdir(music_dir)
                    song = random.choice(songs)
                    os.startfile(os.path.join(music_dir,song))
                elif "the time" in query:
                    time = datetime.datetime.now().strftime("%H:%m:%S")
                    print("jarvis: the time is "+ str(time))
                    sp("sir the time is "+ str(time))
                elif "stop" in query:
                    sp("bye bye sir")
                    break
        else:
            sp("can you speek again ")
main()

        