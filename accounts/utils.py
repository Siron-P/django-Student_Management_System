def redirect_after_login(user):
    if user.is_admin():
        return "accounts:admin_dashboard"
    if user.is_teacher():
        return "teachers:teacher_dashboard"
    return "students:student_dashboard"