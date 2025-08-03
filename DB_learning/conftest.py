import mysql.connector
import pytest
import pandas as pd
# establishing the connection
import pytest
import _mysql_connector


@pytest.fixture

mydb = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        passwd="Garvsql1@",
        database="gauravdb"

    )



