
class Genre:
    def is_genre_text(self, input):
        return '#genre#' in input
    
    def parse(self, content):
        object_list = []
        for line in content:
            strip_space_line = line.strip()
            if strip_space_line == '':
                continue
            if ',' not in strip_space_line:
                continue
            line_split = strip_space_line.split(',')
            if len(line_split) != 2:
                continue
            name, url = line_split
            if not url.startswith("http"):
                continue

            object_list.append((name.strip(), url.strip()))
        return object_list