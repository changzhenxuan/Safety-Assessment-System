def get_folder_urls(dic,url_list):
    if dic.get('type')=='folder':
        for d in dic["children"]:
            if d.get('type')=='url' and d.get('url') not in url_list:
                url_list.append(d['url'])
            if d.get('type')=='folder':
                get_folder_urls(d,url_list)
