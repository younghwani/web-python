#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi, os, view
form = cgi.FieldStorage()

if 'id' in form: #id 있는 경우
    if form['id'].value == 'WEB': #그 id가 WEB인 경우 home 디렉토리
        pageId = form['id'].value
        description = open('data/home/WEB', 'r').read()
    elif form['id'].value in os.listdir('data/admin'): #관리자 작성 파일은 data 디렉토리
        pageId = form["id"].value
        description = open('data/admin/'+pageId, 'r').read()
    else:
        pageId = form["id"].value #모든 유저가 쓴 파일은 create_data 디렉토리
        description = open('data/create_data/'+pageId, 'r').read()
else:
    pageId = 'WEB' #id 없는 경우 기본 홈페이지(default)
    description = open('data/home/WEB', 'r').read()


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
    <div id="grid">
        <div id="category">
            <h3>By Younghwani</h3>
            <ol>{listStr1}</ol>
            <h3>By All Users</h3>
            <ol>{listStr2}</ol>
        </div>
        <div id="article">
            <form action="process_update.py" method='post'>
                <input type='hidden' name='pageId' value='{form_default_title}'>
                <p><input type='text' name='title' placeholder='title' value='{form_default_title}'></p>
                <p><input type='hidden' name='pre_description' value='{form_default_description}'>
                <p><textarea rows='4' name='description' placeholder='description'>{form_default_description}</textarea></p>
                <p><input type='submit'></p>
            </form>
        </div>
    </div>
</body>
</html>
'''.format(
    title=pageId, 
    description=description, 
    listStr1=view.getList('data/admin'), 
    listStr2=view.getList('data/create_data'), 
    form_default_title=pageId, 
    form_default_description=description))