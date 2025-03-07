from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now
from .models import UserDevice
from django.utils.translation import gettext as _
import requests # pylint: disable=import-error

@receiver(user_logged_in)
def store_user_device(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    device = request.META.get("HTTP_USER_AGENT", _("Unknown"))
    
    location = get_ip_location(ip)

    device_entry = UserDevice.objects.filter(user=user, device=device).first() # pylint: disable=no-member

    if device_entry:
        device_entry.last_login = now()
        device_entry.ip_address = ip
        device_entry.location = location
        device_entry.save()
    else:
        UserDevice.objects.create( # pylint: disable=no-member
            user=user,
            device=device,
            ip_address=ip,
            location=location,
            last_login=now()
        )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_ip_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return f"{data.get('city', '')}, {data.get('region', '')}, {data.get('country', '')}"
    except:
        return _("Unknown")