"""Mail Settings."""

from masonite import env
import os

"""From Address
This value will be used for the default address when sending emails from
your application.
"""

FROM = {
    'address': env('MAIL_FROM_ADDRESS', 'hello@example.com'),
    'name': env('MAIL_FROM_NAME', 'Masonite')
}

"""Mail Driver
The default driver you will like to use for sending emails. You may add
additional drivers as you need or pip install additional drivers.

Supported: 'smtp', 'mailgun'
"""

DRIVER = 'mailgun'

"""Mail Drivers
Different drivers you can use for sending email.
"""

DRIVERS = {
    'smtp': {
        'host': env('MAIL_HOST', 'smtp.mailtrap.io'),
        'port': env('MAIL_PORT', '465'),
        'username': env('MAIL_USERNAME', 'username'),
        'password': env('MAIL_PASSWORD', 'password'),
        'ssl': True
    },
    'mailgun': {
        'secret': os.getenv('MAILGUN_SECRET', 'key-XX'),
        'domain': os.getenv('MAILGUN_DOMAIN', 'sandboxXX.mailgun.org')
    }
}
