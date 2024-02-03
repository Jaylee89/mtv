import re

class M3U:
    def is_m3u(self, input) -> bool:
        return '#EXTM3U' in input or '#EXTINF' in input
    
    def parse(self, content):
        object_list = []
        for line in content:
            strip_space_line = line.strip()
            if strip_space_line == '':
                continue
            if '#EXTM3U' in strip_space_line:
                continue
            if '#EXTINF' in strip_space_line:
                index = strip_space_line.find(",")
                name = strip_space_line[index:] if index != -1 else None
                pattern = re.compile(r'(?P<tvg_name>tvg-name="([^"]+)")|(?P<group_title>group-title="([^"]+)")')
                matches = pattern.findall(strip_space_line)  
                if matches:
                    for match in matches:
                        if 'tvg_name' in match:
                            tvg_name = match['tvg_name']
                            print(f"tvg-name: {tvg_name}")
                        if 'group_title' in match:
                            group_title = match['group_title']
                            print(f"group-title: {group_title}")
                    if name is None:
                        name = tvg_name

            if 'http' in strip_space_line:
                url = strip_space_line

            object_list.append((name.strip(), url.strip(), group_title))
        return object_list