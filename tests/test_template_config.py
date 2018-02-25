import do.template_config
import string


def test_author_config():
    test_author = do.template_config.authors_template(
        'project', 'carlos', 'carlos@gmail.com')
    assert type(test_author) is str


def test_setup_template():
    test_setup = do.template_config.setup_template(
        setup_name='setup_name',
        setup_version='setup_version',
        setup_description='setup_description',
        setup_author='setup_author',
        setup_author_email='setup_author_email',
        setup_url='setup_url')
    assert type(test_setup) is str


def test_load_template():
    test_load = do.template_config.load_template('template_authors.txt')
    assert type(test_load) is string.Template
