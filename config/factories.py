from orator.orm import Factory
from app.User import User
from app.Member import Member

factory = Factory()


def users_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': '$2b$12$WMgb5Re1NqUr.uSRfQmPQeeGWudk/8/aNbVMpD1dR.Et83vfL8WAu',  # == 'secret'
    }


def members_factory(faker):
    return {
        'full_name': faker.name(),
        'position': faker.job(),
        'image_url': 'uploads/temp_team.jpg'
        }

factory.register(User, users_factory)
factory.register(Member, members_factory)
