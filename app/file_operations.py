import mysql.connector
from settings import Settings
from flask import request,make_response, abort, send_file, Response
import os

class file:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Settings.get_config_param('db_host'),
            user=Settings.get_config_param('db_user'),
            password=Settings.get_config_param('db_password'),
            database=Settings.get_config_param('db_name')
        )
    def download(self):
        linkedid = request.args.get('linkedid')
        cursor = self.conn.cursor()
        cursor.execute(f'''SELECT 1''')
        result = cursor.fetchone()
        self.conn.close()
        # Проверяем, существует ли файл
        if not result:
            abort(404)

        file_path = result[0]

        # Проверяем, существует ли файл на диске
        if not os.path.isfile(file_path):
            abort(404)

        # Возвращаем файл клиенту
        try:
            response = make_response(send_file(file_path, as_attachment=True))
            response.headers['Content-Disposition'] = f'attachment; filename={linkedid}.mp3'
            response.headers['Content-Type'] = 'audio/mpeg'
            return response
        except Exception as e:
            return Response(str(e), status=400)
