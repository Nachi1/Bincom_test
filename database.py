import psycopg2

conn = psycopg2.connect(database="1", user="postgres", password="progres", host="localhost", port="5432")
print('Success')
