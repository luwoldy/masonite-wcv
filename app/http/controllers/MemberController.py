"""A MemberController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Member import Member
from masonite.helpers import compact


class MemberController(Controller):
    """MemberController Controller Class."""

    def __init__(self, request: Request):
        """MemberController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        members = Member.all()
        return view.render('team', compact(members))

