''' A VolunteerNotification Notification '''
from notifications import Notifiable

class VolunteerNotification(Notifiable):

    def mail(self):
        return self.subject('New Volunteer Signup!') \
            .driver('mailgun') \
            .panel('wcv.pythonanywhere.com') \
            .heading('A new volunteer has signed up!') \
            .line('See you soon! Game on!') \
            .view('/notifications/snippets/mail/heading',
                  {'name': f'{self._name}'})