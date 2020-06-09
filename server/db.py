import os
import json

from mysql import connector


dev_path = os.getcwd()

mysql_config = json.loads(open(dev_path+'/mysql_config.json').read())

mysql_config['database'] = 'SG_TMS'

connection = connector.connect(**mysql_config)


class PrimaryKeyAlreadyExistsError(connector.Error):
    '''
    raises when you are trying to insert a tuple whose primary key is already present int the database.
    '''
    pass



def insert(kwargs):
    
    cursor = connection.cursor()
    
    try:
        cursor.execute(f'''
            INSERT INTO cities ({", ".join(list(kwargs.keys()))}) VALUES ({", ".join(list(kwargs.values()))});
        ''')
        connection.commit()
    
    except connector.Error as err:
        if err.errno == 1062:
            raise PrimaryKeyAlreadyExistsError('The `city_id` you are trying to insert is already present in the table.')

    cursor.close()


def show():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cities;")
    result = cursor.fetchall()
    cursor.close()
    return result


__all__ = [insert, connection, dev_path, mysql_config, PrimaryKeyAlreadyExistsError, show]


