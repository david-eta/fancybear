"""
Functionality:
- 'search_form': This function generates a context dictionary containing a 'search_form' instance of the 'SearchForm' class, which is used to render a search form in templates.

Note:
- Assumes the existence of a 'SearchForm' class defined in the forms.py file within the same directory as this module.
- This function is typically used as a context processor to make the search form available in multiple templates across the application.
"""

from .forms import SearchForm

def search_form(request):
    return {'search_form': SearchForm()}