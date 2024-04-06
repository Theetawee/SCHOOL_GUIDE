from base.settings.base import APP_NAME


def app(request):
    return {"APP_NAME": APP_NAME}
