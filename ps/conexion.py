import pyodbc
import mysql.connector


###SERVIDOR EMPRESA ZETONE
zt_server = '---'
zt_user = '---'
zt_psw = '----'

###SERVIDOR PRONEUTRONXS
ps_server = '----'
#ps_user = '----'
#ps_psw = '----'
ps_user = '----'
ps_psw = '----'
ps_port = '----'



###CONEXIONES SERVIDOR EMPRESA ZETONE

#VARIABLE DATABASE
db_SQLRondin = 'MyZetto'

def SQLRondin():
    try:
        Rondin = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + zt_server +'; DATABASE=' + db_SQLRondin + '; UID=' + zt_user + '; PWD=' + zt_psw)
        return Rondin
    except Exception as e: 
        print(e)
        print("EXCEPT - CONEXIÓN.PY") 

db_SQLRoca5_Zetoneapp = 'Zetoneapp'

def SQLRoca5():
    try:
        Roca5 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + zt_server +'; DATABASE=' + db_SQLRoca5_Zetoneapp + '; UID=' + zt_user + '; PWD=' + zt_psw)
        return Roca5
    except Exception as e: 
        print(e)
        print("EXCEPT - CONEXIÓN.PY")



###CONEXIONES SERVIDOR PRONEUTRONXS

#VARIABLE DATABASE
ps_db_Rondin = 'Rondin'

def ps_Rondin():
    try:
        ps_Rondin = mysql.connector.connect(host = ps_server, port = ps_port, user = ps_user, password = ps_psw, db = ps_db_Rondin)
        return ps_Rondin
    except Exception as e:
        
        print(e)
        print("EXCEPT - CONEXIÓN.PY") 
        return e

ps_db_permisos = 'Permisos'

def ps_Permisos():
    try:
        ps_permisos = mysql.connector.connect(host = ps_server, port = ps_port, user = ps_user, password = ps_psw, db = ps_db_permisos)
        return ps_permisos
    except Exception as e:
        print(e)
        print("EXCEPT - CONEXIÓN.PY")


