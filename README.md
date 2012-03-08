Django Taggit Token Field
=========================

**Django Taggit Token Field** provides a simple to use `TagTokenWidget`, which autocompletes and tokenizes tag entry.

Installation
------------

1. Install `taggittokenfield` somewhere on your Python Path. The easiest way to do this may be `pip install git+https://github.com/oberlin/django-taggit-tokenfield#egg=taggittokenfield`.
2. Add `'taggittokenfield'` to `INSTALLED_APPS` in `settings.py`.
3. Add `url(r'^tags/', include('taggittokenfield.urls'))` or similar to your `urlpatterns` in `urls.py`.

Usage
-----

The easiest way to use the token field in the Django admin is to override the form widget for `TaggableManagers` on your `ModelAdmin`s using the `formfield_overrides` attribute. E.g.,

    from django.contrib import admin
    from taggit.managers import TaggableManager
    from taggittokenfield.forms import TagTokenWidget
    
    class BlogAdmin(admin.ModelAdmin):
        formfield_overrides = {
            TaggableManager: {'widget': TagTokenWidget}
        }