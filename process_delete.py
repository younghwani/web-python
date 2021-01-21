#!/usr/local/bin/python3

import cgi, os, datetime
form = cgi.FieldStorage()
pageId = form['pageId'].value
description = form['description'].value
# 휴지통 기능(삭제 시간 저장)
now = datetime.datetime.now()
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
delete_file = open('data/deleted_data/' + pageId, 'w')
delete_file.write(description)
delete_file.write("\n\n(Delete Time: " + nowDateTime + ")")
delete_file.close()
# remove
os.remove('data/create_data/' + pageId)
# Redirection
print("Location: index.py")
print()