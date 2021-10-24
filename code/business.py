from flask import Flask,request
import models
import urlParser
from models import Malware
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from datetime import datetime


session = Session(engine)
models.Base.metadata.create_all(bind=engine)

def scan():
    checkLink = urlParser.checkLink()
    rows = session.query(Malware).count()
    if checkLink[0] > rows:
        for i in checkLink[1]:
            is_true = session.query(Malware.md5_hash).filter_by(md5_hash=i).first() is not None
            if is_true != True :
                hashDetail = urlParser.checkAllMalware(i)
                departure_date = datetime(2012, 3, 3, 10, 10, 10)
                data = Malware(sha256_hash="{}".format(hashDetail[0]['sha256_hash']), sha1_hash="{}".format(hashDetail[0]['sha1_hash']),
                               md5_hash="{}".format(hashDetail[0]['md5_hash']), first_seen="{}".format(hashDetail[0]['first_seen']),
                               tags="{}".format(hashDetail[0]['tags']), signature="{}".format(hashDetail[0]['signature']))
                session.add(data)
                session.commit()

def count():
    count = session.query(Malware).count()
    return count


def deleteMalware(id):
    session.query(Malware).filter_by(id=id).delete()


def malwareDetail(id):
    s = session.query(Malware).get(id)
    data = {'id' : s.id, 'sha256_hash' : s.sha256_hash, 'sha1_hash' : s.sha1_hash, 'md5_hash' : s.md5_hash,
            'first_seen' : s.first_seen, 'tags' : s.tags, 'signature' : s.signature}
    return data


def listAllMalware():
    malwares = session.query(Malware).all()
    arr = []
    for i in malwares:
        a = [i.id,i.sha256_hash,i.sha1_hash,i.md5_hash,i.first_seen,i.tags,i.signature]
        arr.append(a)
    dict = {'data' : arr}
    return dict
