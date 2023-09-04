from flask import request, abort
from settings import Settings


class IPAccessChecker:
    allowed_ips = ["127.0.0.1"]  # Список разрешенных IP-адресов

    @staticmethod
    def check_access():
        request_ip = request.headers.get(
            'X-Forwarded-For', request.remote_addr)
        if request_ip == Settings.get_config_param('asterisk_server_ip'):
            return
        else:
            abort(403, "Access denied")
