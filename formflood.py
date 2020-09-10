import requests
import os
import random
import string
import json
import time

# chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://www.associate4you.com/'

# passwordfield = 'field id'
personfield = 'form_fields[name]'
emailfield = 'form_fields[email]'
messagefield = 'form_fields[message]'

# calling all Json Files
firstnames = json.loads(open('names.json').read())
lastnames = json.loads(open('lastnames.json').read())
emaildomains = json.loads(open('emaildomains.json').read())
messages = json.loads(open('messages.json').read())

print('Finding a unique person...')

# for loop could be better, but it works for now...
for name in range(1000):
    # generating some variables to be used later
    name_extra = ''.join(random.choice(string.digits) for i in range(4))
    lastname = random.choice(lastnames)
    firstname = random.choice(firstnames)
    emaildomain = random.choice(emaildomains)
    message = random.choice(messages)

    email = firstname.lower() + lastname.lower() + name_extra + emaildomain
    # password = ''.join(random.choice(chars) for i in range(22))
    person = firstname + ' ' + lastname
    time.sleep(5)
    print(person + ' found!')


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
        print(person + ' is interested in buying a cat!')
        time.sleep(5)
        print('Request sent!')
        time.sleep(5)
    except:
        print('He doesnt like cats, trying again')
        time.sleep(60)

    # need to wait some time or the server thinks you are DOS'ing them
    # added some stuff to read while we wait, added time to different prints
    print(firstname + ('s email is: ' + email))
    time.sleep(5)
    print(firstname + (' said: ' + message))
    time.sleep(5)
    print('Looking for another person.')
    time.sleep(5)

print('Man these people love cats!')
