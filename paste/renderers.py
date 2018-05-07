from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from paste.tools import cache_exists, cache_fetch, cache_store


def render_pygments(request, paste, data):
    """Renders Pygments template."""
    key = paste.slug+'_pygments.cache'
    if cache_exists(key):
        highlighted_content = cache_fetch(key)
    else:
        lexer = get_lexer_by_name(paste.language.slug)
        formatter = get_formatter_by_name('html')
        highlighted_content = highlight(paste.content, lexer, formatter)
        cache_store(key, highlighted_content)
    data['paste'] = paste
    data['highlighted'] = highlighted_content
    rendered = loader.render_to_string('paste/show-pygments.html', data, request)
    return HttpResponse(rendered)


def render_form(request, paste, data):
    """Renders Form template."""
    data['paste'] = paste
    rendered = loader.render_to_string('paste/show-form.html', data, request)
    return HttpResponse(rendered)


def render_raw(request, paste, data):
    """Renders RAW content."""
    return HttpResponse(paste.content, content_type='text/plain')
