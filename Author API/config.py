class Config:
   SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/authors_db" #Default db
    # The connection string is the one in quotes(no spaces included.i.e. DBMS software+driver 
    # database_uri_key = dialect+driver://username:password@host:por/database
    #The default user name is root since no password has been set.
   # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://faithapio:faithapio@100.115.92.198:por/authors_db"