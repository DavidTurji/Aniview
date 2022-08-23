import vimeo

TOKEN = 'replace me'
KEY = 'replace me'
SECRET = 'replace me'


def comment(url=input("Enter url "),
            content=input("Enter content ")):
    if 'https://vimeo.com/' in url:
        video_id: str = str(url).replace('https://vimeo.com/', '').replace('/', '')

    client = vimeo.VimeoClient(token=TOKEN,
                               key= KEY,
                               secret=SECRET)
    res = client.post('https://api.vimeo.com/videos/'+str(video_id)+'/comments',
                      data={
                          "text": ""+content
                      }
                      )
    res_body = res.json()
    comment_uri = res_body.get('uri')
    if comment_uri is None or type(comment_uri) != str\
            or res.status_code != 201:
        return print("The posted comment couldn't be found")

    comment_id = comment_uri.split('/')[-1]
    check_res = client.get(f'https://api.vimeo.com/videos/{video_id}/comments/{comment_id}')
    if check_res.status_code != 200:
        return print('could not find comment')

    print("comment posted")


comment()
