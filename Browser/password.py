import os,json,shutil,base64,win32crypt,sqlite3
import pandas as pd
from AES import AES
class Password:
    """
    https://blog.csdn.net/Demonslzh/article/details/125062240
    浏览器密码解密
    """
    def __init__(self,path):
        """
        self.path: the path of User Data
        """
        self.path = path
        
    def get_encryption_key(self):
        local_state_path = os.path.join(os.path.split(self.path)[0], "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_password(self, password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                import traceback
                traceback.print_exc()
                return ""
            
    def parse_password(self):
        key = self.get_encryption_key()
        db_path = os.path.join(EDGE_PATH, "Login Data")
        # 复制一份数据库文件出来
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute(
            "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        rows = []
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = self.decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]
            item = {}
            if username or password:
                item["origin_url"] = origin_url
                item["action_url"] = action_url
                item["username"] = username
                item["password"] = password
            rows.append(item)
            
        cursor.close()
        db.close()
        try:
            # try to remove the copied db file
            os.remove(filename)
            pd.DataFrame(rows).to_csv("passwords.csv")
        except:
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    CHROME_PATH = "C:/Users/czx/AppData/Local/Google/Chrome/User Data/Default"
    EDGE_PATH = "C:/Users/czx/AppData/Local/Microsoft/Edge/User Data/Default"
    EDGE_KILL = "taskkill /f /t /im msedge.exe"
    CHROME_KILL = "taskkill /f /t /im chrome.exe"
    Password(CHROME_PATH).parse_password()