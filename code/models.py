from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Malware(Base):

    __tablename__ = "malware"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    sha256_hash = Column(String)
    sha1_hash = Column(String)
    md5_hash = Column(String)
    first_seen = Column(String)
    tags = Column(String)
    signature = Column(String)



