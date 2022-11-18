import os,json,traceback
import utils
class BookMark:
    
    def __init__(self,browser_path):
        self.browser_path = browser_path
        # refresh bookmarks
        self.bookmarks = self.get_bookmarks()
        
    def get_bookmarks(self):
        'update browser bookmark data from browser path'
        # parse bookmarks
        assert os.path.exists(
            os.path.join(self.browser_path,
                         'Bookmarks')), "can't found 'Bookmarks' file,or path isn't a right browser cache path!"
        with open(os.path.join(self.browser_path, 'Bookmarks'), encoding='utf-8') as f:
            return json.loads(f.read())
        
    def get_folder_urls(self):
        """获取收藏夹所有的文件夹内容，合并后保存"""
        self.fav_urls = []
        for mark_name, mark_folder in self.bookmarks["roots"].items():
            try:
                utils.get_folder_urls(mark_folder,self.fav_urls)
            except Exception:
                traceback.print_exc()
                print(mark_name)
        for url in self.fav_urls:
            print(url)
        
        
if __name__=='__main__': 
    CHROME_PATH = 'C:/Users/czx/AppData/Local/Google/Chrome/User Data/Default'
    EDGE_PATH = "C:/Users/czx/AppData/Local/Microsoft/Edge/User Data/Default"
    # bm = BookMark(EDGE_PATH)
    bm = BookMark(CHROME_PATH)
    bm.get_folder_urls()
    