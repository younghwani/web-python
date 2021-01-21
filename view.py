import os
#import html_sanitizer
def getList(path):
    #sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir(path)
    listStr = ''
    for item in files:
        #item = sanitizer.sanitize(item)
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr