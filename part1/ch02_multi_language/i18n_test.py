import gettext


translation_ko = gettext.translation(domain="i18n_test", localedir="./locale", languages=["ko_KR"])
translation_ko.install()

print(_("Test message 1"))
print("Test message 2")
print(_("Test message 3"))
