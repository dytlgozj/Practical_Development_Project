import gettext


translation_ko = gettext.translation(domain="i18n_multilang", localedir="./locale", languages=["ko_KR"])
translation_zh = gettext.translation(domain="i18n_multilang", localedir="./locale", languages=["zh_CN"])
translation_ja = gettext.translation(domain="i18n_multilang", localedir="./locale", languages=["ja_JP"])

translation_ko.install()
translation_zh.install()
translation_ja.install()

print(_("Test message 1"))
print("Test message 2")
print(_("Test message 3"))
