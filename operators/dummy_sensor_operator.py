__author__ = 'astronomerio'

from airflow.operators.sensors import BaseSensorOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults


class DummySensorOperator(BaseSensorOperator):
    """
    This dummy does whatever you want it to.

    Useful for testing

    Returns True or False
    """
    ui_color = '#7c7287'

    @apply_defaults
    def __init__(self, flag, *args, **kwargs):
        super(DummySensorOperator, self).__init__(*args, **kwargs)
        self.flag = flag

    def poke(self, context):
        return True if self.flag in [1, True, 'true', 'True'] else False


class DummySensorPlugin(AirflowPlugin):
    name = "DummySensorPlugin"
    hooks = []
    operators = [DummySensorOperator]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
