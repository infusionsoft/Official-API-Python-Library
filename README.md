# Infusionsoft API Python Wrapper
Allows for quick setup and usage of the Infusionsoft XML-RPC API  using Python's native XML-RPC support. Find more info at http://help.infusionsoft.com/developers/api-basics/

## Installation

clone and run: ``python setup.py install``

or

``pip install git+https://github.com/infusionsoft/Official-API-Python-Library.git``


## Usage
First, make sure you import the Infusionsoft class:

	from infusionsoft.library import Infusionsoft

Now set your Infusionsoft account name and API key:

	infusionsoft = Infusionsoft(name, api_key)

You can make requests to Infusionsoft services by calling that service as a function and passing the service method as the first argument, with that method's required arguments as the second Python argument:

	infusionsoft.service(method, args)

You can accomplish the same thing using the server library method to access the API:

	infusionsoft.server().service.method(infusionsoft.key, args)

#### OAuth Usage

If you are using OAuth, you can instantiate the library using the InfusionsoftOAuth class. The only
usage difference is that initialization only requires 1 argument (the OAuth access_token).

```python
from infusionsoft.library import InfusionsoftOAuth

infusionsoft = InfusionsoftOAuth(access_token)
```

For more information on OAuth, see the Infusionsoft docs:

https://developer.infusionsoft.com/docs/read/Getting_Started_With_OAuth2

## Examples

### Example 1: Add a Contact
Using the primary service method:

	contact = {'FirstName' : 'John', 'LastName' : 'Doe', 'Email' : 'johndoe@email.com'}
	print infusionsoft.ContactService('add', contact)

Using the server library method:

	contact = {'FirstName' : 'John', 'LastName' : 'Doe', 'Email' : 'johndoe@email.com'}
	print infusionsoft.server().ContactService.add(infusionsoft.key, contact)

### Example 2: Send an Email
	contactList = [123, 456, 789]
	fromAddress = 'john@test.com'
	toAddress = '~Contact.Email~'
	ccAddress = ''
	bccAddress = ''
	contentType = 'Text'
	subject = 'This is just a test email, relax!'
	htmlBody = ''
	textBody = 'This is the contant for the email'
	print infusionsoft.APIEmailService('sendEmail', contactList, fromAddress, toAddress, ccAddress, bccAddress, contentType, subject, htmlBody, textBody)

See examples.py for more examples