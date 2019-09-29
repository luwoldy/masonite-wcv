from orator.migrations import Migration


class CreateMembersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('members') as table:
            table.increments('id')
            table.char('full_name',50)
            table.char('position',255)
            table.char('image_url',255)
            table.char('company', 60)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('members')
