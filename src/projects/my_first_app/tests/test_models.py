from django.test import TestCase

from projects.my_first_app.models import Child, Parent


class MultiTableInheritanceTests(TestCase):
    def test_child_has_a_parent(self):
        child = Child.objects.create()
        self.assertTrue(Parent.objects.exists())
