# seeds.py
from models import db, Word

def seed_default_words(app):
    """アプリ起動時にDBが空なら20語登録するシード処理"""
    with app.app_context():
        if Word.query.count() == 0:
            default_words = [
                {'japanese':'りんご','english':'apple','note':''},
                {'japanese':'バナナ','english':'banana','note':''},
                {'japanese':'みかん','english':'orange','note':''},
                {'japanese':'猫','english':'cat','note':''},
                {'japanese':'犬','english':'dog','note':''},
                {'japanese':'学校','english':'school','note':''},
                {'japanese':'家','english':'house','note':''},
                {'japanese':'本','english':'book','note':''},
                {'japanese':'ペン','english':'pen','note':''},
                {'japanese':'コンピュータ','english':'computer','note':'PCとも'},
                {'japanese':'電話','english':'phone','note':''},
                {'japanese':'水','english':'water','note':''},
                {'japanese':'お茶','english':'tea','note':''},
                {'japanese':'コーヒー','english':'coffee','note':''},
                {'japanese':'車','english':'car','note':''},
                {'japanese':'電車','english':'train','note':''},
                {'japanese':'都市','english':'city','note':''},
                {'japanese':'音楽','english':'music','note':''},
                {'japanese':'映画','english':'movie','note':''},
                {'japanese':'友達','english':'friend','note':''},
            ]
            for w in default_words:
                db.session.add(Word(**w))
            db.session.commit()
