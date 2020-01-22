from user_account.models import Contact_admin


def add_variable_to_context(request):
    message_count = Contact_admin.objects.filter(active=False)
    m_count = 0
    if message_count is not None:
        m_count = message_count.count()
    # print(m_count)
    return {
        'm_count': m_count
    }