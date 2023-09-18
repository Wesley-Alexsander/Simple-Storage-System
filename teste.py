import mysql.connector as odbc
import pandas as pd

con = odbc.connect(
    host='containers-us-west-114.railway.app',
    user='root',
    password='Sq5fg8cBpkMOAgSYChMq',
    port='7626'
    )

query = """insert into S3.Fornecedor  values ('UNIAO EDUCACIONAL, CULTURAL E TECNOLOGICA IMPACTA - UNI.IMPACTA','RUA CUBATAO',	726, null,'VILA MARIANA','SAO PAULO','SP','04.013-002','(11) 3254-2100 / (11) 3825-0510','carlos@3aocubo.com.br')
"""

cursor = con.cursor()

cursor.execute(query)
con.commit()
