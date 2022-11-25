from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from rsakeys.src.main import get_publicKeyInfo, get_privateKeyInfo, is_valid_file

list_campos = [
    'Modulus',
    'Public exponent',
    'Private exponent',
    'First prime',
    'Second prime',
    'Exponent 1',
    'Exponent 2',
    'Coefficient'
]

def index(request):
    keytype = None
    context = {}
    if request.method == 'POST' and request.FILES['file']:
        upload = request.FILES['file']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        pem = open('C:/Users/oscar.pf.h/Documents/Seguridad/rsa_keys/rsakeys' + file_url, 'r').read()
        
        is_valid, keytype = is_valid_file(pem)
        if is_valid == True:
            print(pem)
            if keytype == 'public':
                pubKeyInfo = get_publicKeyInfo(pem)
                context = {
                    'key': pubKeyInfo,
                    'keytype': keytype
                }
            elif keytype == 'private':
                privKeyInfo = get_privateKeyInfo(pem)
                info_list = zip(list_campos, privKeyInfo.values())
                context = {
                    'info_list': info_list,
                    'keytype': keytype
                }
            else :
                print('key not defined')
            return render(request, 'form.html', context)
        else :
            print('file not valid')

    return render(request, 'form.html')