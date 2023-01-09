from selene.support.shared import browser
import os
import test


def create_path(selector, path):
    browser.element(selector).set_value(
        os.path.abspath(os.path.join(os.path.dirname(test.__file__), path))
    )
