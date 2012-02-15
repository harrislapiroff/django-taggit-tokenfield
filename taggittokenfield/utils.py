"As of the time of this writing, reverse_lazy is in Django's development version, but until that is released, we'll import it from here."
from django.utils.functional import lazy
from django.core.urlresolvers import reverse

reverse_lazy = lazy(reverse, str)