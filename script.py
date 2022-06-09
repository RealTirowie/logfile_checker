# -*- coding: utf8 -*-

import os
from datetime import datetime

def send_mail(errors):
    print("")
    print("Folgende Anträge wurden nicht übernommen: ")
    print("")
    for i in errors:
        print(i)
    print("")
    print("Versuch es nochmal!")
    print("")
    input("Press Enter to close it.")
    print("")


def extract_data_from_file(file):
    with open(file) as f:
        entry_list = [line.rstrip() for line in f]
    return entry_list

def create_error_list(search_words, logfile):
    logfile_errors = []
    # checking if search list element is contained in logfile strings 
    for i in logfile:
        res = [ele for ele in search_words if(ele in i)]
        if res:
            logfile_errors.append(i)
    return logfile_errors


# get list of search words, get list of logfile entries 
try:
    search_words = extract_data_from_file('search_text.txt')
except:
    print("")
    print('kein Suchfile vorhanden: search_text.txt')
    print("")
    input("Press Enter to close it.")
    print("")

try:
    logfile = extract_data_from_file('A2BLog.txt')
except:
    print("")
    print('kein Logfile vorhanden: A2BLog.txt')
    print('Starte zuerst die Antragsübernahme.')
    print("")
    input("Press Enter to close it.")
    print("")

# get logfile entries that match search words
errors = create_error_list(search_words, logfile)

# check for error entries and send mail
if errors != []:
    send_mail(errors)
else:
    print("")  
    print("Alle Anträge wurden übernommen. Gut gemacht! :-)")
    print("")
    input("Press Enter to close it.")
    print("")

# prepare filname
file_name_ex = str(datetime.now())
file_name_ex = file_name_ex.replace(':', '_').replace('.', '_').replace(' ', '_')

os.rename('A2BLog.txt', 'A2BLog'+file_name_ex+'.txt')

try:
    os.rename('A2BLog.txt', 'A2BLog'+str(datetime.now())+'.txt')
except:
    pass

exit()