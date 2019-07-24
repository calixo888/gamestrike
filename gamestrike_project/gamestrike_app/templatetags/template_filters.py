from django import template

register = template.Library()

def url_valid(url):
    import requests
    try:
        conn = requests.get(url)
        return True
    except Exception as e:
        print(e)
        return False

register.filter('url_valid', url_valid)
