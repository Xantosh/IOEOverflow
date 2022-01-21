from django.shortcuts import render
from elasticsearch import Elasticsearch
from .models import *
from .forms import * 


#models used 
# Question -> id, text, image, upvote, downvote

# Create your views here.
def index(request):
    return render(request, "main/index.html")

#Create the forms


# Posting question view 
def forum(request):
    text='' 
    imageocr =''
    image=''
    
    if request.method == 'POST':
        # get the data
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            print("form valid")
            text=form.cleaned_data["text"]
            image = form.cleaned_data["image"]

        

            
    # First, count the total number of documents in the index in the elastic search
        es = Elasticsearch()
        number_of_items = es.count(index='question')['count'] # current total number of docs in the index
                                                              # count function returns a dictionary so take the count key item 

    # Second, update the models use the id from the total number of contents +1 
        number_of_items += 1
        #update the sql server
        # right now id =2 but after connecting elastic server you need to id= number_of_items
        obj = Question.objects.create(id=number_of_items,text=text,image=image)
        obj.save()
    # Third, update the data in the elastic server database
    # call the ocr function and get the string search data to be able to search 
        imageocr= ocrcompdummy() 
        update_els_server(number_of_items,text,imageocr)
        

    form= QuestionForm()
    context={
            'form':form
            }

    return render(request,"main/forum.html",context)




def questionPost(request):
    questions = Question.objects.all().order_by('id')[:10].values() # Getting the required data from the models
    print(questions)
    return render(request,'main/posts.html',{
        'questions':questions
        }) #returning the template with the context
    
    
def search(request):
        form= SearchForm()
        text=''
        search_ids=[]
        question=[]

        if request.method =='POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['text']
        # elastic search using the given query
        #call a function
            search_ids = getID_ElasticSearch(text)
            for i in search_ids :
                data= Question.objects.filter(id=i).values()
                question.append(data)

            print(question)
        context={
                "search":form,
                "questions": question

                }
        




        return render(request,'main/search.html',context)


# function for ocr computation 
def ocrcomp():
import cv2
import numpy as np
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def ocr_core(img):            # function to convert iamge to text
    text = tess.image_to_string(img)
    return text


img = cv2.imread('lol.png')  # get image from location


def get_grayscale(image):          # preprocess to convert to grayscale
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 5)


def threshholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


img = get_grayscale(img)
img = threshholding(img)
img = remove_noise(img)

print(ocr_core(img))



# dummy testing function for ocrcomp
def ocrcompdummy():
    return "this is a dummy string"

def update_els_server(id,text,image):
    es = Elasticsearch()
    doc ={
            'text':text,
            'image':image
            } 
    es.create(index='question',id=id,body=doc)

def getID_ElasticSearch(text):
    es = Elasticsearch()
    indices=[]
    doc = {
    "query":{
        "match":{
            "text":{
                    "query":text,
                            "fuzziness": "AUTO"
                                  
            }

        }

    }

    }
    data=es.search(index='question',body=doc)
    print(data)
    a= len(data['hits']['hits'])
    data=data['hits']['hits']
    for i in range(0,a):

        indices.append(data[i]['_id'])


    print(indices)
    return indices
    


def getID_ElasticSearch_Dummy(text):

    return [1,2]

