from django import template

register = template.Library()

@register.filter()
def restrict_text(text):
  """
  Takes string as an argument
  and reurns only 400 first symbols
  """

  if len(text) > 400:

    return text[:400] + ' ...'
  
  return text