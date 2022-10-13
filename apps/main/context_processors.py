from apps.main.models import GlobalSetting


def global_data(request):
    settings = GlobalSetting.objects.get(id=1)
    return {
        'SETTINGS': settings
    }

