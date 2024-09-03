
def is_admin_user(user):
    """
    Checks if the user has Admin permissions
    """
    return user.is_staff or user.is_superuser