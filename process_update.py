#!/usr/local/bin/python3

import cgi, os
form = cgi.FieldStorage()
pageId = form['pageId'].value
title = form['title'].value
pre_description = form['pre_description'].value # for back-up
description = form['description'].value

# 이전 title, description BackUp
backup_file = open('data/update_backup_data/' + pageId, 'w')
backup_file.write(pre_description)
backup_file.write("\n\n(Update Title: " + title + ")\n")
backup_file.write("(Update Description: " + description + ")\n")
backup_file.close()
# update(new description)
opened_file = open('data/create_data/' + pageId, 'w')
opened_file.write(description)
opened_file.close()
# update(new name)
os.rename('data/create_data/' + pageId, 'data/create_data/' + title)
# Redirection
print("Location: index.py?id="+title)
print()