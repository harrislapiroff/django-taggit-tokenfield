import json
from django.http import HttpResponse
from taggit.models import Tag

def filter_tags(request):
	"Returns a JSON formatted list of tags starting with the value of GET variable 'q'."
	limiter = request.GET['q']
	results = Tag.objects.filter(name__istartswith=limiter).values_list('name', flat=True)
	data = []
	for tag_name in results:
		data.append({'id': '"%s"' % tag_name, 'name': tag_name})
	return HttpResponse(json.dumps(data), mimetype="application/json")