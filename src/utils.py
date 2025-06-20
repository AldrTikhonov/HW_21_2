import os.path

CYRRENT_DIR = os.path.dirname(__file__)


def open_html(file):

    file_dir = os.path.join(CYRRENT_DIR, '..', file)

    with open(file_dir, 'r+') as f:
        data = f.read()

    if data:
        return data
    return 'Файл не найден'
