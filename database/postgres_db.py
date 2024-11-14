from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

from base.base import Base
from models.email import EmailModel

#todo: can be converted to env variable via os.environ.get('DB_URL')
connection_url = 'postgresql://admin:1234@localho:5437/suspicious_messages'
engine = create_engine(connection_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    Base.metadata.create_all(bind=engine)

def process_email_data(email_data):
    email = email_data.get("email")
    sentences = email_data.get("sentences", [])
    for sentence in sentences:
        for keyword, model in EmailModel.items():
            if keyword in sentence.lower():
                suspicious_content = model(email=email, sentence=sentence)
                db_session.add(suspicious_content)

    db_session.commit()