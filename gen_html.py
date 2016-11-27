#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os

cwd = os.getcwd()
data_dir = cwd + '\data'
main = open('main_py.html', 'w', encoding='utf-8')
main.write('<!DOCTYPE html>')

def writeProfile(dir_name) :
    main.write('<div class="row profile">')

    # write image
    main.write('<div class="col-xs-4 col-sm-2 col-md-2">')
    main.write('<img src="http://placehold.it/100x100" class="img-fluid" alt="Responsive Image">')
    main.write('</div>') # end of col-sm-2 col-md-2

    # write profile
    main.write('<div class="col-xs-8 col-sm-10 col-md-10 text-left">')
    profile = open(dir_name+'/profile', 'r', encoding='utf-8')
    # youtube link 
	#<a class="fancybox-media" href="http://www.youtube.com/watch?v=2YJ0ekCk5IE">Youtube (iframe)</a>
    for line in profile:
        main.write('<h4>%s</h4>' % line)
    profile.close()
    main.write('</div>') # end of col-sm-10 col-md-2

    main.write('</div>') # end of row profile

def writePost(dir_name) :
    main.write('<div class="row post">')

    # write post
    main.write('<div class="col-sm-12 col-md-12">')
    post = open(dir_name+'/post', 'r', encoding='utf-8')
    main.write('<ul>')
    for line in post:
        main.write('<li><h3>%s</h3></li>' % line)
    post.close()
    main.write('</ul>')
    main.write('</div>') # end of col-sm-12 col-md-12

    # write tag
    #main.write('<div class="col-sm12 col-md-12 tag">')

                #<div class="col-sm12 col-md-12 tag">
                 #   <h4><span>#基督教</span><span>#繼承是家屬還是配偶</span><span>#沈默的聲音</span><span>#家庭的定義</span></h4>
                #</div>
    main.write('</div>') # end of row post

def writePerson(dir_name) :
    main.write('<div class="row oneperson" id="%s">' % dir_name)
    writeProfile(dir_name)
    writePost(dir_name)
    main.write('</div>') # end of row oneperson

main.write('<html lang="zh-TW">')
# write header
main.write('<head>')
main.write('<meta charset="utf-8">')
main.write('<meta name="viewport" content="width=device-width, initial-scale=1">')
main.write('<title>同性婚姻公聽會懶人包</title>')

#<!-- Add jQuery library -->
main.write('<script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>')
#<!-- Add fancyBox -->
main.write('<script type="text/javascript" src="fancybox/source/jquery.fancybox.pack.js?v=2.1.5"></script>')
main.write('<link rel="stylesheet" href="fancybox/source/jquery.fancybox.css?v=2.1.5" type="text/css" media="screen">')
#<!-- Add fancyBox - media helper -->
main.write('<script type="text/javascript" src="fancybox/source/helpers/jquery.fancybox-media.js?v=1.0.6"></script>')
main.write('<script type="text/javascript" src="js/fancybox.js"></script>')
main.write('<link href="css/bootstrap.min.css" rel="stylesheet">')
main.write('<link href="css/main.css" rel="stylesheet">')
main.write('</head>')

# write body
main.write('<body>')
main.write('<div class="container">')

# write title
main.write('<div class="row">')
main.write('<div class="col-md-12 text-right">')
main.write('<h1>同性婚姻公聽會懶人包</h1>')
main.write('<h2>聽聽大家怎麼說</h2>')
main.write('</div>') # end of col-md-12
main.write('</div>') # end of row

# read data and output
for data in os.walk(data_dir):
    # write each person
    if (data[0] != data_dir and data[0] != data_dir +'\.idlerc'):
        writePerson(data[0])

main.write('</div>') # end of container
main.write('</body>') # end of body
main.write('</html>') # end of html
main.close()
