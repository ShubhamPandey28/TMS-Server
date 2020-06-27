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


def insert_one(table_name, row):

    cursor = connection.cursor()

    try:
        cursor.execute(
            f"""
            INSERT INTO {table_name} ({", ".join(map(str, row.keys()))}) VALUES ({", ".join(map(str, row.values()))});
        """
        )

    except connector.Error as err:
        if err.errno == 1062:
            raise PrimaryKeyAlreadyExistsError(
                "The `ID` you are trying to insert is already present in the table."
            )

    finally:
        connection.commit()
        cursor.close()


def insert(table_name, rows):

    for row_data in rows:
        insert_one(table_name, row_data)


def return_table(table_name):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT * FROM {table_name};
    """
    )
    result = cursor.fetchall()
    cursor.close()
    return result


def get_client_consignments(client_name):
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT t1.Consignment_ID FROM Consignment as t1 INNER JOIN Consignor_Consignee as t2 ON t1.Consignor_ID = t2.ID OR t1.Consignee_ID = t2.ID WHERE t2.name = '{client_name}'; 
    """
    )
    result = list(set(cursor.fetchall()))
    cursor.close()
    return result


__all__ = [
    insert,
    connection,
    dev_path,
    mysql_config,
    PrimaryKeyAlreadyExistsError,
    return_table,
    get_client_consignments,
]
