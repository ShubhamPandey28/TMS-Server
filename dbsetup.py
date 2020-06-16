"""
This is mysql development env setup file.
Just run it once.
"""

import os
import getpass
import json

from mysql import connector


mysql_config = dict()

dbname = "SG_TMS"

dev_path = os.getcwd()

try:

    mysql_config = json.loads(open(dev_path + "/mysql_config.json").read())


except FileNotFoundError:

    print(
        "`mysql_config.json` is not present in your development env.\nSo we have to get your mysql authentication first"
    )

    mysql_config["user"] = input("Enter your mysql Username (root): ")

    if mysql_config["user"].lower() in ["y", "\n", ""]:
        mysql_config["user"] = "root"

    mysql_config["password"] = getpass.getpass(
        prompt=f"Enter your mysql password for {mysql_config['user']} :"
    )

    mysql_config["host"] = input("Enter your mysql hostname (localhost): ")

    if mysql_config["host"].lower() in ["y", "\n", ""]:
        mysql_config["host"] = "localhost"

mysql_connection = connector.connect(**mysql_config)

mycursor = mysql_connection.cursor()

with open(os.getcwd() + "/schema.sql") as f:
    mycursor.execute(f.read(), multi=True)

json.dump(mysql_config, open(dev_path + "/mysql_config.json", "w"), indent=4)

__all__ = []
