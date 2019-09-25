"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'PageController@home').name('welcome'),
    Get('/ethiopia', 'PageController@eth').name('ethiopia'),
    Get('/team', 'MemberController@show').name('team'),

]
