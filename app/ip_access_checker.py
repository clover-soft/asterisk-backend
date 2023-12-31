from flask import request, abort
from settings import Settings


class IPAccessChecker:
    allowed_ips = ["127.0.0.1"]  # Список разрешенных IP-адресов

    @staticmethod
    def check_access():
        request_ip = request.headers.get(
            'X-Forwarded-For', request.remote_addr)
        if request_ip in Settings.get_config_param('client_ip_list'):
            return
        else:
            abort(403, "Access denied")
