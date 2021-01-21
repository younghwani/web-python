#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi, os, view
#import html_sanitizer
#sanitizer = html_sanitizer.Sanitizer()
form = cgi.FieldStorage()
if 'id' in form: #id 있는 경우
    if form['id'].value == 'WEB': #그 id가 WEB인 경우 home 디렉토리
        title = pageId = form['id'].value
        description = open('data/home/WEB', 'r').read()
        update_button = ''
        delete_action = ''
    elif form['id'].value in os.listdir('data/admin'): #관리자 작성 파일은 data 디렉토리
        title = pageId = form["id"].value
        description = open('data/admin/'+pageId, 'r').read()
        update_button = ''
        delete_action = ''
    else:
        title = pageId = form["id"].value #모든 유저가 쓴 파일은 create_data 디렉토리
        description = open('data/create_data/'+pageId, 'r').read()
        description = description.replace('<', '&lt;')
        description = description.replace('>', '&gt;')
        #title = sanitizer.sanitize(title)
        #description = sanitizer.sanitize(description)
        update_button = '<input id="update" type="button" value="Update" onclick="location.href=\'update.py?id={}\';">'.format(pageId)
        delete_action = '''
            <form action="process_delete.py" method="post">
                <input type="hidden" name="pageId" value="{}">
                <input type="hidden" name="description" value="{}">
                <input type="submit" value="Delete">
            </form>
        '''.format(pageId, description)
else:
    title = pageId = 'WEB' #id 없는 경우 기본 홈페이지(default)
    description = open('data/home/WEB', 'r').read()
    update_button = ''
    delete_action = ''

print('''<!DOCTYPE html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="colors.js"></script>
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <input id="night_day" type="button" value="night" onclick="
        nightDayHandler(this);
    ">
    <input id="create" type="button" value="Create" onclick="
        location.href='create.py';">
    {update_button}
    {delete_action}
    <div id="grid">
        <div id="category">
            <h3>By Younghwani</h3>
            <ol>{listStr1}</ol>
            <h3>By All Users</h3>
            <ol>{listStr2}</ol>
        </div>
        <div id="article">
            <h2>{title}</h2>
            <p>{desc}</p>
        </div>
    </div>
</body>
</html>
'''.format(
    title=title, 
    desc=description, 
    listStr1=view.getList('data/admin'),
    listStr2=view.getList('data/create_data'), 
    update_button=update_button, 
    delete_action=delete_action))
#listStr1 : 관리자 작성, listStr2 : 모든 유저 접근