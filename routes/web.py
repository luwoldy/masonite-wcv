"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'PageController@home').name('welcome'),
    Get('/ethiopia', 'PageController@eth').name('ethiopia'),
    Get('/team', 'MemberController@show').name('team'),
    Get('/add/team', 'MemberController@add_form').name('member.add_form'),
    Post('/team/add', 'MemberController@add').name('member.add'),
    Get('/volunteer', 'PageController@volunteer').name('volunteer'),
    Post('/volunteer/add', 'PageController@add_volunteer').name('volunteer.add'),
    Get('/donate', 'PageController@donate').name('donate'),
    Get('/ethiopia/training', 'PageController@training').name('eth.training'),
    Get('/contact','PageController@contact').name('contact')

]
