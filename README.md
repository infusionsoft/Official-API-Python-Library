# Infusionsoft API Python Wrapper
Allows for quick setup and usage of the Infusionsoft XML-RPC API  using Python's native XML-RPC support. Find more info at http://help.infusionsoft.com/developers/api-basics/

## Usage
First, make sure you import the Infusionsoft class:

	from InfusionsoftLibrary import Infusionsoft

Now set your Infusionsoft account name and API key:

	infusionsoft = Infusionsoft(name, api_key)

You can make requests to Infusionsoft services by calling that service as a function and passing the service method as the first argument, with that method's required arguments as the second Python argument:

	infusionsoft.service(method, args)

You can accomplish the same thing using the server library method to access the API:

	infusionsoft.server().service.method(infusionsoft.key, args)

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