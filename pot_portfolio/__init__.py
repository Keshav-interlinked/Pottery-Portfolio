import pymysql

pymysql.version_info = (2, 2, 1, 'final', 0)   #this fooking important for mysql connection to work
                                                # Fake a high enough mysqlclient version so Django's check passes
                                                #This tricks Django into thinking you're using a new enough         mysqlclient.
#Without faking the version, Django sees PyMySQL's real version_info (often something like 0.x or 1.0.x) and raises the "mysqlclient 2.2.1 or newer required; you have X.Y.Z" error.
pymysql.install_as_MySQLdb()