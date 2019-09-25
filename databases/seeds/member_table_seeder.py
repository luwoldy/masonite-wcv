from orator.seeds import Seeder
from app.Member import Member
from config.factories import factory

class MemberTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        factory(Member, 10).create()

