from . import main



@main.route('/')
def index():
    return '<h1> the post</h1>'