import os
import re

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def get_environs_vars(variable_name, /):
    try:
        file_ = get_env_file()
        for line in file_.readlines():
            regex = re.compile(r'^{}='.format(variable_name))
            if result := regex.match(line):
                result = line.replace(result.group(), '')
                file_.close()
                return result
    except Exception as e:
        raise e


def get_env_file():
    file_ = open(BASE_DIR / '.env', 'r')
    return file_