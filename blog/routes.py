from flask import render_template, views

from blog import app_ctx


class IndexView(views.View):
    """Список методов, которые может обрабатывать это представление."""
    methods = ['GET', 'POST', ]

    def dispatch_request(self):
        """Подклассы должны переопределить этот метод,
        чтобы реализовать фактический код функции представления.
        Этот метод вызывается со всеми аргументами из правила URL."""
        return render_template('blog/index.html')


app_ctx.add_url_rule('/', view_func=IndexView.as_view('index'))
