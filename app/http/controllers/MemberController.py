"""A MemberController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Member import Member
from masonite.helpers import compact, config
from masonite import Upload


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

    def add(self,upload: Upload, view: View, request: Request):
        team_member = request.input('full_name')


        id = Member.insert_get_id({
            'full_name': team_member,
            'position': request.input('position'),
            'image_url': upload.driver('disk').store(request.input('file_upload')),
            'company': request.input('company')
        })
        return view.render('form_success', compact(team_member))

    def add_form(self, view: View):
        return view.render('add_member')
