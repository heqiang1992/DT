#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymysql
import uuid

db = pymysql.connect("localhost", "root", "daemon", "keystone")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS token;")
sql = '''create table if not EXISTS token
(
  id varchar(64) NOT NULL,
  expires datetime NULL,
  extra text NULL,
  valid tinyint(1) NOT NULL,
  trust_id varchar(64) NULL,
  user_id varchar(64) NULL,
  PRIMARY KEY (id),
  KEY ix_token_expires (expires),
  KEY ix_token_expires_valid (expires,valid),
  KEY ix_token_user_id (user_id),
  KEY ix_token_trust_id (trust_id)
)'''
cursor.execute(sql)
print("CREATE TABLE OK")
for i in range(1, 10000):
    try:
        sql = '''insert into token(id, expires, extra, valid, trust_id, user_id) values('%s',
        '2019-01-10 03:25:22',
        't',
        1,
        NULL,
        'f3cebf17a6b14c6482ea8b618aed715c')''' % (str(uuid.uuid1()))
        cursor.execute(sql)
    except:
        continue
db.commit()
cursor.close()
db.close()
