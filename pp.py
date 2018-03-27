# encoding=utf8
# https://eksisozluk.com/sabire-meltem-banko--5483631
import mechanize
import sys
import json
import time

class Configuration:
    def __init__(self):
        with open(str(sys.argv[1])) as config:
            data = json.load(config)
            self.username = data['username']
            self.password = data['password']
            self.entry = data['entry']
            self.baslik = data['baslik']
        # pprint(data)


def main():
    print("-------------------------------")
    print("Ran on" + str(time.strftime('%X %x %Z')))
    user_data = Configuration()
    print(user_data.entry)
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.set_handle_refresh(False)

    url = 'https://www.eksisozluk.com/giris'
    browser.open(url)

    browser.form = list(browser.forms())[2]  # get the login form
    browser.form['UserName'] = user_data.username
    browser.form['Password'] = user_data.password
    response = browser.submit()

    html_file = response.read()
    html_file = str(html_file)
    # print(html_file.find("eauthor"))
    __index = html_file.find("eauthor")

    nick_limit = 42  # set the nick limit !(nick limit for eksisozluk is 40)

    user_name = html_file[__index+11:__index + nick_limit + 11]

    user_name = user_name.split(',')[0]
    user_name = user_name[:len(user_name)-1]
    user_name = user_name.replace(" ","-")
    if len(user_name) is 0:
        print('Login failed !\nCheck your credientials !(or maybe there is a captcha check ?)')
        browser.close()
        sys.exit(1) # this should ensure that login was not succesful
    print('Welcome '+user_name+'\nLogin was succesful')
    header_name = user_data.baslik
    find_header = browser.open("https://eksisozluk.com/")
    browser.form = list(browser.forms())[0]
    browser.form['q'] = header_name
    _found = browser.submit()
    _url = _found.geturl()
    # print("https://eksisozluk.com/"+header_name)
    r = browser.open(_url)
    if (r.code == 404):
        print("Page not found.")
        browser.close()
        sys.exit(1)
    html_of_header = str(r.read())
    html_of_header = html_of_header.decode('utf-8')
    page_count = html_of_header.find('data-pagecount')
    if page_count is -1:
        # entry adding occurs here
        check_first_entry(html_of_header)
        check_if_entry_is_given(html_of_header, user_data)
        print('Adding the entry.')
        create_entry(user_data, browser,r)
    else:
        print('No entry deletion occurred. Exiting...')
        browser.close()
        sys.exit(-1)
#    html_of_header = html_of_header[page_count:]
#    _id = re.findall('pagecount="(.*?)"', html_of_header)
#    page_count = int(_id[0])
#    if page_count > 1:
#        createEntry(user_data,browser)
#        print('page count is bigger than 1')


def check_if_entry_is_given(response_html, user_data):
    found_id = response_html.find(user_data.entry)
    if found_id is not -1:
        browser.close()
        print('Already entered an entry')
        sys.exit(1)
        


def check_first_entry(response_html):
    found_entry = response_html.find(('bu başlıkta yer alan içeriklere erişimin engellenmesine karar verilmiştir.').decode('utf-8'))
    if found_entry is -1:
        print('There has not been any entry deletion. Exiting...')
        browser.close()
        sys.exit(1)
    print('Entries were deleted from this header.')
    # we can also check all the entries in case someone deletes the previous entry
    # and restores it, so that the first entry is not the deletion entry
    # seems redundant for now ?


def create_entry(user_data, browser,r):
    try:
        browser.form = list(browser.forms())[3]#get the entry adder form
    except IndexError:
        print('Login Somehow Failed !\nCheck your credentials ! (Maybe the site did not exist ?'
            ' \'cause script could not find the entry adder form)')
        browser.close()
        sys.exit(1)  # if there is no 4'th form, that means that login has failed
                         # exit immediately(somehow it skips the first sys.exit,highly unlikely)
    browser.form['Content'] = user_data.entry
    response = browser.submit()
    __code = int(response.code)
    browser.close()
    if __code is 200:
        print('Successfully added the entry.')
        sys.exit(0)
    else:
        print('Failed to add the entry.')
        sys.exit(1)


if __name__ == '__main__':
    main()
