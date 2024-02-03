import model
import database
import ipv4v6
import website
from m3u import M3U
from genre import Genre

class TV:
    __file_list: list
    def __init__(self, file_list: list):
        self.__file_list = file_list

    def execute_batch(self):
        for file_name in self.__file_list:
            self.__execute(file_name=file_name)

    def __execute(self, file_name: str):
        object_list = []
        # read file
        with open(f'{file_name}', mode='r', encoding='utf8') as f:
            all_lines = f.readlines()
            all_lines_with_space = filter(lambda x: x.strip(), all_lines)
            m3u = M3U()
            genre1 = Genre()
            if m3u.is_m3u(all_lines_with_space[0]) or m3u.is_m3u(all_lines_with_space[1]):
                object_list = m3u.parse(all_lines_with_space)
            elif genre1.is_genre_text(all_lines_with_space[0]):
                object_list = genre1.parse(all_lines_with_space)

        # model.TVModel(name=name.strip(), url=url.strip())
        
        object_list_renew = []
        for data in object_list:
            available, http_code = website.check_website_visibility(data.url)
            ipv4_result = 9
            available_result = 10
            if available:
                ipv4_result = 0 if ipv4v6.is_ipv6(data.url) else 1
                available_result = 11
            data_renew = model.TVModel(name=name, url=url, http_code=http_code, ipv4=ipv4_result, valid=available_result)
            print(data_renew.__dict__)
            object_list_renew.append(data_renew.to_tuple())

        # store in memory

        # db = database.DB()
        # db.init_table()
        # db.start()
        # db.insert_many(object_list)

        # merge to object list
        # init database
        # insert data into database