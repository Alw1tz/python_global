import re
import psycopg2
import random
import base64
import requests
import json
from xml.etree import ElementTree
from uuid import uuid1
from requests.auth import HTTPBasicAuth
from time import gmtime, strftime
from datetime import datetime
import pandas as pd

import datetime
import time
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from os import system
from rc import pid
from rc import conf

connection = psycopg2.connect(
    user='postgres',
    password='123',
    host='localhost',
    port='5432',
    database='systemrc'
)

# ver si se conectó
print("Se conectó!!!!!!", connection)
connection.autocommit = True
cursor = connection.cursor()
_c = """ 
    select params, job_id from rc.job
    where func_name = 'job_otm_send_shipment_status' 
    and job_status = 'NEW' 
    """
cursor.execute(_c)
_c = cursor.fetchall()
# print(json.dumps(_c[1][0]['url']))
# list_to_dict = dict(_c)
# _params = pd.read_sql_query(sql=_c, con=connection)
# _d = _params.iloc[0]['params']['data']
# url = _params.iloc[1]['params']['url']
# print(type(_c[1][0].get('data')))
# _job_id = _params.iloc[2][1] #lo primero es el elemento y lo segundo es la consulta de job_id (ese no cambia)
# print(url)
# print(len(_c))
# if len(_params) > 0:
#     for d in _params:
#         if d[i] is not None:
#             i += 1
#             # _update_query = "UPDATE rc.job SET job_status = 'FINISHED', finished = now() WHERE job_id = {};".format((d[i][1]))
#             # print("%s" % (d[0].get('url')))
#             print("%s" % (d.iloc[i][0][1]))
# else:
#     print(f'NO DATA FOUND IN QUERY')

# hace el update:
# dx = 62466315
# _act = "UPDATE rc.job SET job_status = 'FINISHED', finished = CLOCK_TIMESTAMP() WHERE job_id = %s;"%(dx)
# cursor.execute(_act)
# connection.commit()
# cursor.close()
iterate = True
seconds_to_wait = 0
error_log_directory = "D:\Logs\Tasks\sp_job_start/"
try:
    if len(_c) > 0:
        i = 0
        for d in _c:
            new_status = 'FINISHED'
            url = _c[i][0]['url']
            _d = _c[i][0]['data']
            job_id = _c[i][1]
            # print(">> Item: %s" % (i)) #control
            # print("url: %s" % url)  # url
            # print("data: %s" % _d)  # data
            # print("job_id %s" % job_id)  # job_id

            # modificar la base de datos
            # _mod_db = ("""
            #     UPDATE rc.job SET job_status = 'FINISHED', finished = CLOCK_TIMESTAMP() WHERE job_id = %s;
            #     """ % (job_id))
            # cursor.execute(_mod_db)
            i += 1
    else:
        print('Sin más registros disponible: OK!')
finally:
    cursor.close()
    connection.close()
# def Main():
#     global connection
#     iterate = True
#     seconds_to_wait = 0
#     error_log_directory = "D:\Logs\Tasks\sp_job_start/"
#
#     try:
#         connection = psycopg2.connect(conf.db.DB_CONNECT_STR_IRON.format("systemrc"))
#         connection.autocommit = True
#         cursor = connection.cursor(cursor_factory=RealDictCursor)
#         i = 0
#
#         # p = pid.Control()
#         # while p.check():
#         while iterate:
#             system("color E")
#             i += 1
#             print(">> Item: %s" % (i))
#             d1 = datetime.datetime.now()
#             cursor.execute("""
#                 UPDATE ONLY rc.sp_job AS j
#                 SET job_status = 'STARTED',
#                     started = CLOCK_TIMESTAMP()
#                 FROM (
#                     SELECT job_id
#                     FROM ONLY rc.sp_job
#                     WHERE job_status = 'NEW'
#                         AND scheduled <= NOW()
#                     ORDER BY created
#                     LIMIT 1
#                     FOR UPDATE
#                     SKIP LOCKED
#                 ) q
#                 WHERE j.job_id = q.job_id
#                 RETURNING j.job_id, j.func_name, j.user_id, j.params::text;
#             """)
#             data = cursor.fetchall()
#
#             if len(data) > 0:
#                 for d in data:
#                     print("  job_id: %s, func_name: %s" % (d["job_id"], d["func_name"]))
#                     result = True
#                     job_status = 'FINISHED'
#                     try:
#                         if "sp_" in d["func_name"]:
#                             cursor.execute("CALL rc.{0}(%s,%s,%s);".format(d["func_name"]),
#                                            (d["job_id"], d["user_id"], d["params"]))
#                         else:
#                             cursor.execute("SELECT rc.{0}(%s,%s,%s);".format(d["func_name"]),
#                                            (d["job_id"], d["user_id"], d["params"]))
#                             data2 = cursor.fetchall()
#                             if len(data2) > 0:
#                                 result = data2[0][d["func_name"]]
#
#                         if result == False:
#                             job_status = 'WARNING'
#                     except psycopg2.DatabaseError as error:
#                         print("    ERROR: %s" % (error.diag.message_primary))
#                         result = False
#                         job_status = 'FAILED'
#                         cursor.execute("SELECT rc.job_log_append(%s,%s,'ERROR',0);",
#                                        (d["job_id"], "MESSAGE: " + str(error.diag.message_primary)))
#
#                     print("    Updating job result: %s" % (job_status))
#                     cursor.execute("""
#                         UPDATE rc.job AS j
#                         SET job_status = '%s',
#                             finished = CLOCK_TIMESTAMP()
#                         WHERE j.job_id = %s;
#                     """ % (job_status, d["job_id"]))
#
#                     print("    Deleting sp_job from stack")
#                     cursor.execute("DELETE FROM ONLY rc.sp_job WHERE job_id = %s;" % (d["job_id"]))
#                     cursor.execute("DELETE FROM ONLY rc.sp_job WHERE job_status IN ('WARNING', 'FINISHED');")
#
#                     dd = datetime.datetime.now() - d1
#                     print("    TotalTime: %s.%s seg" % ((dd.days * 86400) + dd.seconds, dd.microseconds))
#                     # time.sleep(10)
#             else:
#                 i = 0
#                 iterate = False
#                 system("color A")
#                 print("  Status: NO_MORE_JOBS_FOUNDED; Waitting: %s seg" % (seconds_to_wait))
#                 time.sleep(seconds_to_wait)
#     except Exception as error:
#         system("color C")
#         file_name_error = SaveLogFile(error_log_directory, str(error))
#         print("")
#         print("ERROR: %s" % (str(error)))
#         print("Log Saved At %s" % file_name_error)
#     finally:
#         if connection is not None:
#             cursor.close()
#             connection.close()

