import django.dispatch
from django.utils.functional import LazyObject

__version__ = '1.2.1'

default_app_config = 'constance.apps.ConstanceConfig'


class LazyConfig(LazyObject):
    def _setup(self):
        from .base import Config
        self._wrapped = Config()


config = LazyConfig()

updated_signal = django.dispatch.Signal(providing_args=['key', 'value'])
