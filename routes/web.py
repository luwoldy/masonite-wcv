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
    Get('/contact', 'PageController@contact').name('contact'),
    Get('/letter', 'PageController@letter').name('letter').middleware('auth'),
    Get('/overview', 'PageController@overview').name('overview').middleware('auth'),
    # Get('/strapi', 'PageController@strapi').name('strapi'),
    Get('/fetal-echocardiography', 'PageController@fe').name('article.fe'),



]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show').name('login'),
    Get().route('/logout', 'LoginController@logout').name('logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show').name('register'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show').name('home'),
    Get().route('/email/verify', 'ConfirmController@verify_show').name('verify'),
    Get().route('/email/verify/send', 'ConfirmController@send_verify_email'),
    Get().route('/email/verify/@id:signed', 'ConfirmController@confirm_email'),
    Get().route('/password', 'PasswordController@forget').name('forgot.password'),
    Post().route('/password', 'PasswordController@send'),
    Get().route('/password/@token/reset',
                'PasswordController@reset').name('password.reset'),
    Post().route('/password/@token/reset', 'PasswordController@update'),
]
