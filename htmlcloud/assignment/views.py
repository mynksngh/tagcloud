from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from tokenize import *


def index(request):
    context = {}
    return render(request, 'home.html', context)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        file = myfile
        try:
            content_type = file.content_type
            print content_type
            if not content_type in ['text/plain']:
                context = {
                    'msg': 'Invalid File Type, Please Upload a Text File Only'
                }
                return render(request, 'file_upload.html', context)
        except AttributeError:
            pass
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = get_words(filename)
        link_data = list_dictionary(filename)
        context = {
            'uploaded_file_url': uploaded_file_url,
            'freq_data': data,
            'link_data': link_data,
            'filename': filename,
            'msg': '',
        }
        return render(request, 'file_upload.html', context)
    context = {}
    return render(request, 'file_upload.html', context)

def show_line(request):
    if request.method == 'GET':
        myfile = request.GET['file']
        word = request.GET['word']
        word = word.upper()
        # link_data = list_dictionary(myfile)
        line_list = []
        word_count = 0
        with open('media/'+myfile) as db_file:
            for line_no, line in enumerate(db_file):
                line = line.lower()
                word = word.lower()
                r = re.compile(r'\b%s\b' % word, flags=re.I | re.X)
                if r.findall(line):
                    line_list.append(line)
                    word_count += 1
                else:
                    pass
        if word_count:
            context = {
                'filename': myfile,
                'line_list': line_list,
                'msg': '',
                'word': word,
            }
        else:
            context = {
                'msg': 'Unable to Find the %s in File' % word,
                'word': word,
            }
        return render(request, 'show_text_lines.html', context)
    context = {
        'msg': 'Unable to Find the word in any line of the file',
    }
    return render(request, 'show_text_lines.html', context)