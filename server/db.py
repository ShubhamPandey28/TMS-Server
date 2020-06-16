import os
import json

from mysql import connector


dev_path = os.getcwd()

mysql_config = json.loads(open(dev_path + "/mysql_config.json").read())

mysql_config["database"] = "SG_TMS"

connection = connector.connect(**mysql_config)


class PrimaryKeyAlreadyExistsError(connector.Error):
    """
    raises when you are trying to insert a tuple whose primary key is already present int the database.
    """

    pass


def insert_one(table_name, table_data):

    value = table_data

    cursor = connection.cursor()

    try:
        cursor.execute(
            f"""
            INSERT INTO {table_name} ({", ".join(list(value.keys()))}) VALUES ({", ".join(list(value.values()))});
        """
        )

    except connector.Error as err:
        print(err)

    finally:
        connection.commit()
        cursor.close()


def insert(table_name, table_datas):

    for table_data in table_datas:
        insert_one(table_name, table_data)


def show(table_name, to_disp=None):
    cursor = connection.cursor()

    columns = []
    for key in to_disp.keys():
        if to_disp[key] == True:
            columns.append(key)

    if columns == []:
        cursor.execute(
            f"""
            SELECT * FROM {table_name};
        """
        )
    else:
        cursor.execute(
            f"""
            SELECT {", ".join(columns)} FROM {table_name};
        """
        )

    result = cursor.fetchall()
    cursor.close()

    return result


__all__ = [
    insert,
    connection,
    dev_path,
    mysql_config,
    PrimaryKeyAlreadyExistsError,
    show,
]
