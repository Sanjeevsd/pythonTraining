import requests
user_url=input("enter url")
res=requests.get(user_url)
lines=res.text.split(" ")


def download_image(splittedurl):
    print(splittedurl)
    if "https" in splittedurl:
        url=splittedurl
    else:
        url = (user_url + splittedurl)
    newreq = requests.get(url)
    image = newreq.content
    name = url.split("/")
    img = open(name[-1], "wb")
    img.write(image)
    img.close()


for line in lines:
    if("png" in line ):
        splitted=line.split("\"")
        try:

            download_image(splitted[1])

        except:
            pass
