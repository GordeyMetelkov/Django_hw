from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)


def custom_log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Была вызвана функция {func.__name__}')
        return result
    return wrapper

@custom_log
def index(request):
    return render(request, 'index.html', {'tittle': 'Главная'})

@custom_log
def about(request):
    return render(request, 'about.html', {'tittle': 'Обо мне'})