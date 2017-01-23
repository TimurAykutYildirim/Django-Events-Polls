from tastypie.resources import ModelResource
from tastypie import fields
from polls.models import Question, Choice
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'

class ChoiceResource(ModelResource):
    question = fields.ForeignKey(QuestionResource, 'question')
    #question = fields.ForeignKey(QuestionResource, Question.objects.get(id=2))
    class Meta:
        filtering = {
            'question': ALL_WITH_RELATIONS,
        }
        queryset = Choice.objects.all()
        resource_name = 'choice'

