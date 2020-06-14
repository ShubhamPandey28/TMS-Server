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


def insert_one(table_data):

    '''
        table_data :    datatype - dict(table_name: string, value: dict)             
    '''

    table_name = table_data['table_name']
    value = table_data['value']

    cursor = connection.cursor()
    
    try:
        cursor.execute(f'''
            INSERT INTO {table_name} ({", ".join(list(value.keys()))}) VALUES ({", ".join(list(value.values()))});
        ''')
        
    except connector.Error as err:
        if err.errno == 1062:
            raise PrimaryKeyAlreadyExistsError('The `city_id` you are trying to insert is already present in the table.')
    
    connection.commit()
    cursor.close()


def insert(table_datas):
    
    '''
        inserts tuple in databases.
        this is separated from insert_one because of future error handling if one table for eg.
        we are able to insert in one table and other table results in insertion error.

        table_datas : list(table_data)
    '''
    
    for table_data in table_datas:
        insert_one(table_data)    


def show(table_name):
    cursor = connection.cursor()
    cursor.execute(f'''
        SELECT * FROM {table_name};
    ''')
    result = cursor.fetchall()
    cursor.close()
    return result


__all__ = [insert, connection, dev_path, mysql_config, PrimaryKeyAlreadyExistsError, show]


