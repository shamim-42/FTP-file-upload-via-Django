## Simple code snippet to upload file in ftp server via django

### Sample `.env` file
```
FTP_SERVER_HOST="192.140.252.57"
FTP_SERVER_USER=ftpshamim
FTP_SERVER_PASSWORD=ftpshamim123
```

**File upload API endpoint:**
`http://YOUR_DOMAIN.com/file-upload/image/`

**Field Name**:
`file`

### How to run
1. Clone / Download the project in your local pc
2. Create a virtual environment (optional) inside the project dir or the parent directory
3. Run `pip install -r requirements.txt` inside project directory
4. Create a file named `.env`
5. Put the ftp credentials in that file like the mentioned demo `.env`
4. Run `python manage.py runserver`
7. Thats it ! Upload your file via the specified api endpoint (`/file-upload/image/`)