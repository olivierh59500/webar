#!/usr/bin/python
try:
    import re
    from robobrowser import RoboBrowser
    from django.core.exceptions import ValidationError
    from django.core.validators import URLValidator
    from PIL import Image
    from urllib import request
    from optparse import OptionParser
except ImportError:
    from PIL import Image
    from urllib import request
    import re
    from robobrowser import RoboBrowser
    from django.core.exceptions import ValidationError
    from django.core.validators import URLValidator
    from optparse import OptionParser
    print(ImportError.msg)

##Captcha Bypass Tool
__version__ = '0.1.0-dev'
__banner__ = 'captmb v%s' % __version__

def run():
        description = "a tool for no one"
        usage = "usage: %prog -u [address] -t [ms] "
        parser = OptionParser(description=description, usage=usage)

        parser.add_option("-u", "--url",
                   type="string",
                   dest="address",
                   help="give me an login form address")

        parser.add_option("-t", "--time",
                  type="int",
                  dest="timeout",
                  help="time between login tries.must be int(ms)")
        (options, args) = parser.parse_args()
        address = options.address

        val = URLValidator()
        try:
                val(address)
        except ValidationError:
                print(ValidationError)
                raise "malformed url!"

        scrap(address)


def scrap(url):

        browser = RoboBrowser(user_agent='i am tool')
        browser.open(url)
        a = browser.find(class_='captcha') ##machine learning would be great for class prediction
        fullsrc = url[:-1] + a['src']
        request.urlretrieve(fullsrc, "captcha.jpg")
        ##tesseract buraya gelecek


        ##tam buraya işte aha
        form = browser.get_form(action=re.compile(r'.'))

        # Fill it out
        form['name'].value = 'namaaaeee'

        form['password'].value = 'can@can.com'
        form['password2'].value = 'teambeaver'
        form['captcha_1'].value = '1234'

        # Submit the form
        browser.submit_form(form)

        print(browser.response)


"""
mam
"""
run()
