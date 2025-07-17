# 正しくは apps.py 内でこう使う
from django.apps import AppConfig

class MealsConfig(AppConfig):
    name = 'meals'

    def ready(self):
        from django.apps import apps
        Meal = apps.get_model('meals', 'Meal')
        # ここで信号(signal)接続などを行う

