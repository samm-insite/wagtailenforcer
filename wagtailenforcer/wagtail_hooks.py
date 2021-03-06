from django.core.urlresolvers import reverse

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem


@hooks.register('register_settings_menu_item')
def register_blocked_users_item():
    # TODO check the reverse function
    return MenuItem('Blocked users', reverse('wagtailenforcer_blocked_users'), classnames='icon icon-locked', order=10000)
    # return MenuItem('Blocked users', 'wagtailenforcer_blocked_users', classnames='icon icon-locked', order=10000)
