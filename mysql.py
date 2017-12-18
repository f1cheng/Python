# !/usr/bin/env python
# coding:utf-8

import MySQLdb, sys

try:
    db = MySQLdb.connect(host='localhost',
                         user='test',
                         passwd='test',
                         db='testdb')
# with db:---affect in python3?
# root/charging

    cur = db.cursor()
    create_tbl = "drop table if exists Orders;\
                  CREATE TABLE Orders(Id INT(9) primary key auto_increment, \
                                      Name VARCHAR(50), \
                                      Unit int, \
                                      Price double)"
    cur.execute(create_tbl)
    insert_rec1 = "insert into Orders(Name, Unit, Price) values('F1cheng', 1, 100)"
    cur.execute(insert_rec1)

    insert_rec = "insert into Orders(Name, Unit, Price) values(%s, %s, %s)"
    name = 'f2'
    unit = 2
    price = 2
    args = (name, unit, price)
    cur.execute(insert_rec, args)
    db.commit()

    cur.execute('select * from Orders')
    line = '*'*30
    print line
    for row in cur.fetchall():
        print (row)
    print line

except MySQLdb.Error, e:
    print "Error %d:%s" %(e.args[0], e.args[1])

finally:
    if db:
        db.close()

if __name__ == '__main__':
    print ('MySQLdb\nFinished')
