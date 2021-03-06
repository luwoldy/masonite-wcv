"""Base Database Seeder Module."""

from orator.seeds import Seeder
from .user_table_seeder import UserTableSeeder
from .member_table_seeder import MemberTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)
        self.call(MemberTableSeeder)
