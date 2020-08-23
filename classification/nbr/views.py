from django.shortcuts import render
import joblib

#from PIL import Image
import numpy as np
from .models import Hello
from django.core.files.storage import FileSystemStorage
from PIL import Image
import os
from nbr.models import Pest

reload=joblib.load('./models/india.pkl')

def greetings(request):
    return render(request,'nbr/home.html')

def runcode(request):
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    x=os.path.join('./media',filePathName)

    filePathName=fs.url(filePathName)
    #x=os.path.dirname(os.path.dirname(filePathName))
    #x=os.path.join('.',filePathName)
    print(x)
    Im=Image.open(x)
    Im=Im.resize((32,32))
    Im=np.array(Im)

    Im=Im.flatten()
    val=reload.predict([Im])

    x=Pest.objects.get(pk=val[0])


    print(x)







    return render(request,'nbr/home.html',{'p':filePathName,'x':x})
