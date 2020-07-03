#! python3
import re, pyperclip

"""Once the document that you want to collect numbers from is open simply use Ctrl+A to highlight 
everything and then Ctrl+C to copy. Then execute this script and paste into the wordprocessor of
choice. All of the phone numbers will be extracted. If you want to include extensions just uncomment line 18 """

def getPhoneEmail():
    #TODO: Create a Regular Expression (regex) for phone numbers 
    phoneRegex = re.compile(r'''
            # 415-555-000, 555-000 , (415) 555-0000 , 555-000 ext 12345, ext. 12345, x12345
    (
        (\d{3}?|\(\d{3}\)?)    #area code (optional)
        (-|\s)    #first separator
        (\d{3})   #first 3 digits
        (-|\s)    #second seperator
        (\d{4}) # last 4 digits
        # ~ (((ext(\.)?\s)|x)(\d{2,5}))   # extension number part (optional)
    )
        ''', re.VERBOSE)

    #TODO: Create a regex for email addresses
    emailRegex = re.compile(''' 
    (
        # some.+-thing@some.+-thing.com

        ([a-zA-Z0-9-.+]+)   # name part
        (@)                     # @ symbol
        ([a-zA-Z0-9-.+]+)    #domain name part

    )
    ''', re.VERBOSE)

    #TODO: Get the text of the clipboard
    text = pyperclip.paste()

    #TODO: Extract the email/phone from this text
    extractedPhone = phoneRegex.findall(text)
    extractedEmail = emailRegex.findall(text)

    #TODO: Copy the extracted email/phone to the clipboard
    allPhoneNumbers = []
    for phoneNumber in extractedPhone:
        allPhoneNumbers.append(phoneNumber[0])
    allEmails = []

    for email in extractedEmail:
        allEmails.append(email[0])

    results = '\n'.join(allPhoneNumbers) + ' ' + '\n'.join(allEmails)
    pyperclip.copy(results)
    
getPhoneEmail()
