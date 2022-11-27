# Mail Sender

There are many ways you can use this skript. It looks like good start for many different ides for mailing, feel free to use. I made this one for fast sending a lot of emails for a lot of people.

## Tips

Before the start you need allow third party apps to make changes and get password-key. You can find it in privacy settings on your mail accaunt. After that create config_data.py to import email adress and the key. They have following format:

```python
email = 'email.name@somedom.com'
email_password = 'PLACE_YOUR_PASS_HERE'
```

Most likely you have to enable two-step authentification before geting the key. It's standart case.

Next step is connecting to Google Sheets for getting all information about recipients. Before that you need to create Google App on [Google Cloud API](https://cloud.google.com/apis/docs/overview). Then start connection in `ggl_sheets_con.py`, select range and dimension.

Now we are ready for prepare sending. Open `sending_file_with_html.py`. We are starting with opening our HTML letter and some formating.  Then set up the "From", "To" and "Subject" title. And start sending with loop.


## Last word 

Have a success! See you. Let's bring this world to the Horizon.
