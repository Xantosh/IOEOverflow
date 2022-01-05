from django.shortcuts import render
from elasticsearch import Elasticsearch

# Create your views here.
def index(request):
    return render(request, "main/index.html")


def forum(request):
    return render(request,"main/forum.html")

# Posting question view 
def questionPost(request):
    # First, count the total number of documents in the index in the elastic search
    # Second, update the models use the id from the total number of contents +1 
    # Third, update the data in the elastic server database
    pass

def update_els_server(id,text,image):
    es = Elasticsearch()
    doc ={
            'text':text,
            'image':image
            } 
    es.create(index='question',id=id,body=doc)





