
from decouple import config

def contact_email(request):
    return {'contact_email': config('CONTACT_EMAIL', default='example@example.com') }