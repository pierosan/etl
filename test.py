sql = open("sql/tablas.sql", "r")
texto_sql = sql.read()
sentencias_sql = texto_sql.split(";")
print(sentencias_sql)