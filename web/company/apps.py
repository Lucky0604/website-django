from django.apps import AppConfig


class CompanyConfig(AppConfig):
    name = 'company'
    # 修改admin页面中app的别名
    verbose_name = '公司动态'
