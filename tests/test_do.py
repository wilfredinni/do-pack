import do.skeleton
import do.template_config
import string
import do.licenses


def test_skeleton():
    test_load = do.skeleton.load_structure()
    assert type(test_load) == dict


def test_templates():
    test_author = do.template_config.authors_template(
        'project', 'carlos', 'carlos@gmail.com')
    test_load = do.template_config.load_template('template_authors.txt')
    test_setup = do.template_config.setup_template(
        setup_name='setup_name',
        setup_version='setup_version',
        setup_description='setup_description',
        setup_author='setup_author',
        setup_author_email='setup_author_email',
        setup_url='setup_url')

    assert type(test_author) == str
    assert type(test_load) == string.Template
    assert type(test_setup) == str


def test_licenses():
    test_index = do.licenses.load_index_json()
    assert type(test_index) is dict
