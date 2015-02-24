from infusionsoft.library import Infusionsoft

infusionsoft = Infusionsoft('Infusionsoft Account Name', 'API Key Goes Here')

# Example 1: Add Contact
#----------------------------------------------------------------------------------------
contact = {'FirstName' : 'John', 'LastName' : 'Doe', 'Email' : 'johndoe@email.com'}
print(infusionsoft.ContactService('add', contact))

# Example 2: Merge two duplicate contacts
#----------------------------------------------------------------------------------------
contactId = 56
duplicateContactId = 57
print(infusionsoft.ContactService('merge', contactId, duplicateContactId))

# Example 3: Query a contact using data service
#----------------------------------------------------------------------------------------
table = 'Contact'
returnFields = ['Id', 'FirstName']
query = {'FirstName' : 'John'}
limit = 10
page = 0
print(infusionsoft.DataService('query', table, limit, page, query, returnFields))

# Example 4: Return a products inventory using product service
#----------------------------------------------------------------------------------------
productId = 1
print(infusionsoft.ProductService('getInventory', productId))

# Example 5: Charge an invoice using the invoice service
#----------------------------------------------------------------------------------------
invoiceId = 16
notes = 'API Upsell Payment'
creditCardId = 2
merchantAccountId = 1
bypassCommissions = False
print(infusionsoft.InvoiceService('chargeInvoice', invoiceId, notes, creditCardId, merchantAccountId, bypassCommissions))

# Example 6: Send an email using the email service
#----------------------------------------------------------------------------------------
contactList = [123, 456, 789]
fromAddress = 'john@test.com'
toAddress = '~Contact.Email~'
ccAddress = ''
bccAddress = ''
contentType = 'Text'
subject = 'This is just a test email, relax!'
htmlBody = ''
textBody = 'This is the contant for the email'
print(infusionsoft.APIEmailService('sendEmail', contactList, fromAddress, toAddress, ccAddress, bccAddress, contentType, subject, htmlBody, textBody))

# Example 7: Get all report columns using the search service
#----------------------------------------------------------------------------------------
savedSearchId = 3
userId = 1
print(infusionsoft.SearchService('getAllReportColumns', savedSearchId, userId))

# Example 8: Get all shipping options with the shipping service
#----------------------------------------------------------------------------------------
print(infusionsoft.ShippingService('getAllShippingOptions'))

# Example 9: Get affiliate payouts info using filter with the affiliate service
#----------------------------------------------------------------------------------------
from datetime import datetime
affiliateId = 2
filterStartDate = datetime(2012, 10, 18)
filterEndDate = datetime(2012, 10, 23)
print(infusionsoft.APIAffiliateService('affPayouts', affiliateId, filterStartDate, filterEndDate))

# Example 10: Get the download URL of a particular file
#----------------------------------------------------------------------------------------
fileId = 23
print(infusionsoft.FileService('getDownloadUrl', fileId))

# Example 11: Using the library server method to access the API : Create a contact
#----------------------------------------------------------------------------------------
contact = {'FirstName' : 'John', 'LastName' : 'Doe', 'Email' : 'johndoe@email.com'}
print(infusionsoft.server().ContactService.add(infusionsoft.key, contact))
