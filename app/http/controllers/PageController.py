"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller
from app.notifications.VolunteerNotification import VolunteerNotification
from notifications import Notify
from masonite.helpers import compact


class PageController(Controller):
    """Controller For Welcoming The User."""

    def home(self, view: View, request: Request):
        """Show the welcome page.

        Arguments:
            view {masonite.view.View} -- The Masonite view class.
            request {masonite.request.Request} -- The Masonite request class.

        Returns:
            masonite.view.View -- The Masonite view class.
        """
        return view.render('welcome')

    def eth(self, view: View, request: Request):
        """Show the welcome page.

        Arguments:
            view {masonite.view.View} -- The Masonite view class.
            request {masonite.request.Request} -- The Masonite request class.

        Returns:
            masonite.view.View -- The Masonite view class.
        """
        title = '2019 Impact in Ethiopia'
        return view.render('ethiopia', compact(title))

    def volunteer(self, view: View):
        """Show the welcome page.

        Arguments:
            view {masonite.view.View} -- The Masonite view class.
            request {masonite.request.Request} -- The Masonite request class.

        Returns:
            masonite.view.View -- The Masonite view class.
        """
        return view.render('volunteer')

    def add_volunteer(self, notify: Notify, view: View, request: Request):
        team_member = request.input('full_name')
        notify.mail(VolunteerNotification,
                    to='leul.woldeab@gmail.com', name=team_member)
        return view.render('form_success', compact(team_member))

    def donate(self, view: View):
        return view.render('donate')

    def training(self, view: View):
        title = 'Training cardiac professionals in Ethiopia'
        return view.render('ethiopia-training', compact(title))

    def contact(self, view: View):
        return view.render('contact.html')

    def letter(self, view: View):
        title = 'Letter from the director'
        return view.render('letter-director.html', compact(title))

    def overview(self, view: View):
        title = 'World Cardiac Vision Cardiac Sonography Program Overview'
        return view.render('overview.html', compact(title))

    # def strapi(self, view: View):
    #     title = 'Strapi playground'
    #     return view.render('strapi.html', compact(title))

    def fe(self, view: View):
        title = 'Fetal Echocardiography'
        return view.render('echo-cardio.html', compact(title))
