import os
import sqlite3
class History:
    def __init__(self,kill_exe,browser_path):
        try:
            os.system(kill_exe) # sqlite database will be locked when chrome is running
        except:
            pass
        self.browser_path = browser_path
        self.connect()     
    
    def connect(self):
        assert os.path.exists(
            os.path.join(self.browser_path,
                         'History')), "can't found 'History' file,or path isn't a right browser cache path!"
        self.conn = sqlite3.connect(os.path.join(self.browser_path,'History'))
        self.cousor = self.conn.cursor()
        
    def close(self):
        self.conn.close()
        
    def set_browser_path(self,browser_path):
        self.close()
        self.browser_path = browser_path
        self.connect()
    
    def get_history_urls(self):
        self.his_urls = []
        cursor = self.conn.execute("SELECT url from urls")
        for row in cursor:
            url = row[0]
            if url not in self.his_urls:
                self.his_urls.append(url)
        return self.his_urls
            
    def get_downloads(self):
        self.dow_urls = []
        self.target_path = []
        cursor = self.conn.execute("SELECT target_path,tab_url from downloads")
        for target_path, tab_url in cursor:
            if target_path not in self.target_path:
                self.target_path.append(target_path)
            if tab_url not in self.dow_urls:
                self.dow_urls.append(tab_url)
        return self.dow_urls,self.target_path
if __name__=='__main__':
    CHROME_PATH = "C:/Users/czx/AppData/Local/Google/Chrome/User Data/Default"
    EDGE_PATH = "C:/Users/czx/AppData/Local/Microsoft/Edge/User Data/Default"
    EDGE_KILL = "taskkill /f /t /im msedge.exe"
    CHROME_KILL = "taskkill /f /t /im chrome.exe"
    
    his = History(CHROME_KILL, CHROME_PATH)
    
    his_urls = his.get_history_urls()
    print("history urls in chrome:")
    for url in his_urls:
        print(url)
    
    # dow_urls,file_target_path= his.get_downloads()
    # for url in dow_urls:
    #     print(url)