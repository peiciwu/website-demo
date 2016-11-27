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
    main.write('<div class="col-sm-2 col-md-2">')
    main.write('<img src="http://placehold.it/100x100">')
    main.write('</div>') # end of col-sm-2 col-md-2

    # write profile
    main.write('<div class="col-sm-10 col-md-10 text-left">')
    profile = open(dir_name+'/profile', 'r', encoding='utf-8')
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
main.write('<title>同性婚姻公聽會懶人包</title>')
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
