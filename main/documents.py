#documents.py
from django_elasticsearch_dsl import Document
from django_elasticsearc_dsl.registries import registry
#import the class model

@registry.register_document
# after you make models update this file

class QuestionDocument(Document):
    #Name of the Elasticsearch index
    class Index:

        name=''#name of the tables
        settings = {
            'number_of_shards' :1,
            'number_of_replicas':0
            }
    class Django:
        model = # model from models.py
        fields =[] # add the attributes



