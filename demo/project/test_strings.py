from string_utils import kebab_to_camel

def test_kebab_to_camel():
    assert kebab_to_camel("hello-world") == "helloWorld"
    assert kebab_to_camel("my-super-app") == "mySuperApp"
    assert kebab_to_camel("api") == "api"
    assert kebab_to_camel("") == ""
