import constant
import os
import shutil

def clean_workdir():
    if os.path.exists(constant.WORKDIR) and os.path.isdir(constant.WORKDIR):
        shutil.rmtree(constant.WORKDIR)

def make_workdir():
    try:
        os.makedirs(constant.WORKDIR)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise 

def multiline_to_words():
    with open('dev/analytics.js', 'r') as file:
        data = file.read().replace('\n','')
    justwords = data.split()
    return justwords
