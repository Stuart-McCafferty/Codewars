
# DIDNT FINISH, need to go back to this. my answer is too long and hardcodey

def domain_name(url):
    domain = ""
    if url[7] == 'w':
        firstDot = url.find(".")
        secondDot = url.find('.', firstDot + 1)
        domain = url[firstDot + 1:secondDot]
        return domain
    if url[0] == 'w':
        firstDot = url.find(".")
        secondDot = url.find('.', firstDot + 1)
        domain = url[firstDot + 1:secondDot]
        return domain
    if url[6] == '/' and url[11] != "." and url[4] != "s":
        print("test")
        firstDot = url.find(".")
        domain = url[7:firstDot]
        return domain
    if url.startswith("https://"):
        firstDot = url.find(".")
        domain = url[8:firstDot]
        return domain
    if url.startswith("http://"):
        firstDot = url.find(".")
        domain = url[7:firstDot]
        return domain
    if not url.startswith("www."):
        firstDot = url.find(".")
        domain = url[0:firstDot]
        return domain




print(domain_name("youtube.com"))