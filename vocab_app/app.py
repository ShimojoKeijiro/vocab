from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Word
import random
from seeds import seed_default_words

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vocab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key'

db.init_app(app)

with app.app_context():
    db.create_all()
    seed_default_words(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 単語の追加
        jp = request.form['japanese']
        en = request.form['english']
        note = request.form.get('note', '')
        new = Word(japanese=jp, english=en, note=note)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('index'))

    words = Word.query.order_by(Word.id).all()
    return render_template('index.html', words=words)

@app.route('/delete/<int:word_id>', methods=['POST'])
def delete(word_id):
    w = Word.query.get_or_404(word_id)
    db.session.delete(w)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/flashcard')
def flashcard():
    # 単語一覧をセッションに保持（シャッフルしておく）
    if 'order' not in session:
        ids = [w.id for w in Word.query.all()]
        random.shuffle(ids)
        session['order'] = ids
        session['pos'] = 0

    pos = session['pos']
    order = session['order']
    if pos >= len(order):
        # 全問終了
        session.pop('order')
        session.pop('pos')
        return render_template('flashcard.html', finished=True)

    word = Word.query.get(order[pos])
    return render_template('flashcard.html', word=word, show_answer=False)

@app.route('/flashcard/answer')
def show_answer():
    # 回答表示
    pos = session.get('pos', 0)
    order = session.get('order', [])
    if pos >= len(order):
        return redirect(url_for('flashcard'))
    word = Word.query.get(order[pos])
    return render_template('flashcard.html', word=word, show_answer=True)

@app.route('/flashcard/next')
def next_card():
    # 次へ
    session['pos'] = session.get('pos', 0) + 1
    return redirect(url_for('flashcard'))

if __name__ == '__main__':
    app.run(debug=True)
