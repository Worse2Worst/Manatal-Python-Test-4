import requests


# Please insert your own token here
Bearer_token = ''


# Method required by bearer token authentication.
def bearer_oauth(r):
    r.headers['Authorization'] = f'Bearer {Bearer_token}'
    r.headers['User-Agent'] = 'ManatalTestPython'
    return r


def connect_to_endpoint(url):
    response = requests.request('GET', url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            'Request returned an error: {} {}'.format(
                response.status_code, response.text
            )
        )
    return response.json()


def create_url(user_name):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = f'usernames={user_name}'
    user_fields = 'user.fields=public_metrics,created_at'
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = 'https://api.twitter.com/2/users/by?{}&{}'.format(usernames, user_fields)
    return url


# Main function
def get_followers_count(url):
    prefix = 'https://twitter.com/'
    if not url.startswith(prefix):
        print('ERROR: Please input correct Twitter url format.')
        return
    screen_name = url.split(prefix)[1].split('/')[0]
    sending_url = create_url(screen_name)
    json_response = connect_to_endpoint(sending_url)
    followers_count = json_response.get('data', [{}])[0].get('public_metrics', {}).get('followers_count', 0)
    return followers_count
