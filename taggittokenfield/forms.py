from taggittokenfield.utils import reverse_lazy
from taggit import forms


class TagTokenWidget(forms.TagWidget):
	def __init__(self, attrs=None):
		default_attrs = {'data-token-autocomplete': reverse_lazy('taggittokenfield.views.filter_tags')}

		if attrs:
			default_attrs.update(attrs)

		super(TagTokenWidget, self).__init__(default_attrs)
	
	class Media:
		css = {
			'all': ('taggittokenfield/TagTokenWidget.css',),
		}
		js = ('taggittokenfield/jquery.tokeninput.js', 'taggittokenfield/TagTokenWidget.js',)