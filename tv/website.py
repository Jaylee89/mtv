import requests

def check_website_visibility(url) -> bool:
    is_available = False
    http_code = 0
    try:
        response = requests.head(url, timeout=5)
        http_code = response.status_code
        if 200 <= http_code <= 304:
            print(f"The website {url} is visible.")
            is_available = True
        else:
            print(f"The website {url} is not visible. Status code: {response.status_code}")
            is_available = False

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        print(f"The website {url} is not visible.")
        is_available = False
    return is_available, http_code

# 例子：检查 example.com 是否可见
# check_website_visibility("http://example.com")
