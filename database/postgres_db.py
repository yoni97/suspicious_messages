from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker


#todo: can be converted to env variable via os.environ.get('DB_URL')
connection_url = 'postgresql://admin:1234@localho:5437/suspicious_messages'
engine = create_engine(connection_url, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))