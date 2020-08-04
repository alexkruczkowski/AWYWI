import re
import pandas as pd

def FilePrep():
    my_file = open("AWYWI.txt", "r")
    content = my_file.read()
    replace_n = content.replace("\n"," ")
    clean1 = re.sub('[^A-Za-z0-9 ]+', '', replace_n)
    cleaned = clean1.lower()
    return(cleaned)

def Convert():
    song = FilePrep()
    song_li = list(song.split(" "))
    return(song_li)

def UniqueCount():
    song_li = Convert()
    di = dict()
    for w in song_li:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
    return(di)

def Export():
    final = UniqueCount()
    df = pd.DataFrame(final.items(),columns = ['Word', 'Frequency'])
    df.to_csv(r'AWYWI.csv')
    print(df)

Export()
