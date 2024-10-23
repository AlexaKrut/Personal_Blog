from flask import Flask, render_template, request, redirect, url_for, session
from article_manager import ArticleManager
from auth import check_authentication

app = Flask(__name__)
app.secret_key = '0000'  # Замените на свой секретный ключ
article_manager = ArticleManager()

@app.route('/')
def index():
    articles = article_manager.get_all_articles()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = article_manager.get_article(article_id)
    return render_template('article.html', article=article)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_authentication(username, password):
            session['logged_in'] = True
            return redirect(url_for('admin_panel'))
    return render_template('admin.html')

@app.route('/admin/panel')
def admin_panel():
    if not session.get('logged_in'):
        return redirect(url_for('admin'))
    articles = article_manager.get_all_articles()
    return render_template('admin_panel.html', articles=articles)

@app.route('/admin/add', methods=['GET', 'POST'])
def add_article():
    if not session.get('logged_in'):
        return redirect(url_for('admin'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        article_manager.add_article(title, content)
        return redirect(url_for('admin_panel'))
    return render_template('add_article.html')

@app.route('/admin/edit/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin'))
    article = article_manager.get_article(article_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        article_manager.edit_article(article_id, title, content)
        return redirect(url_for('admin_panel'))
    return render_template('edit_article.html', article=article)

@app.route('/admin/delete/<int:article_id>')
def delete_article(article_id):
    if not session.get('logged_in'):
        return redirect(url_for('admin'))
    article_manager.delete_article(article_id)
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    app.run(debug=True)