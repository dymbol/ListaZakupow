#-*- coding: utf-8 -*-
def SearchWriteImage(name, id):
    #Function find image in google by 'name' variable and save image by id variable name plus jpg
    import urllib2
    import urllib
    import BeautifulSoup
    import random
    import os
    import re

    #change id for string (used by file name)
    id = str(id)
    name = name.replace(' ', '+')

    #url link to find image on google
    link = u"http://www.google.pl/search?q=" + name + u"&gbv=1&prmd=ivnse&source=lnms&tbm=isch&sa=X&ei=jN39U4kk453RBc3BgKgO&ved=0CAUQ_AU"

    #opening url
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(link.encode("utf-8"))

    #analyzing tml source by BeutifulSoup
    soup = BeautifulSoup.BeautifulSoup(response.read())
    soup.findAll(itemprop="image")

    #random image from google find page and check if it has http or https link
    imgsrcok = False
    licznik=0
    while imgsrcok is False and licznik < 10:
        imageOBJ= random.choice(soup.findAll('img'))
        if re.match("^(http|https)://*", imageOBJ['src']):
            imgsrcok = True
            #print("imgsrcok is ok")
        else:
            #print("imgsrcok is False")
            licznik = licznik+1



    if licznik < 10:
        sock = urllib.urlopen(imageOBJ['src'])
        imageDATA = sock.read()
        sock.close()
    else:
        sock = urllib.urlopen("http://www.le-math.eu/assets/templates/site/wp/wp2B/15316d025536ca.png")
        imageDATA = sock.read()
        sock.close()


    #Saving image file in static/element_img direcotory of project

    PROJECT_DIR = os.path.dirname(__file__)
    ImageFile = os.path.join(PROJECT_DIR, 'static','element_img',  id + '.jpg')
    try:
        with open(ImageFile, 'w') as f:
            f.write(imageDATA)
    except IOError:
        print("ERROR (function SearchWriteImage) opening file ").format(ImageFile)