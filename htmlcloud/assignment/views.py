from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from utils.generate_token import get_words as process_token
from utils.cleanwords import do_clean_text
from utils.generate_frequencies import generate_frequencies
from utils.linkedcloud import find_word


def index(request):
    context = {}
    return render(request, 'home.html', context)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        file = myfile
        try:
            content_type = file.content_type
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
        # Step 1:
        tokens = process_token(filename)
        # Step2: It will clean the words/tokens : all the noise words, removes punctuation,
        # removes words which are just numbers , It will get the all words in lower
        clean_words_list = do_clean_text(tokens)
        # Step 3,4 : It will Cover all cleaned tokens with their frequencies in sorted dict
        # data = get_words(filename)
        data = generate_frequencies(clean_words_list)
        context = {
            'uploaded_file_url': uploaded_file_url,
            'freq_data': data,
            'filename': filename,
            'msg': '',
        }
        return render(request, 'file_upload.html', context)
    context = {}
    return render(request, 'file_upload.html', context)


def show_line(request):
    if request.method == 'GET':
        my_file = request.GET['file']
        word = request.GET['word']
        if my_file and word:
            search_result = find_word(my_file, word)
            word_count_occurance = search_result.get("word_count", 0)
            line_contains_word = search_result.get("line_contains_word", [])
            if word_count_occurance:
                context = {
                    'filename': my_file,
                    'line_list': line_contains_word,
                    'msg': '',
                    'word': word,
                }
            else:
                context = {
                    'msg': 'Unable to Find the %s in File' % word,
                    'word': word,
                }
            return render(request, 'show_text_lines.html', context)
        else:
            context = {
                'msg': 'Please select the word and file from correct url'
            }
            return render(request, 'show_text_lines.html', context)
    context = {
        'msg': 'Unable to Find the word in any line of the file',
    }
    return render(request, 'show_text_lines.html', context)