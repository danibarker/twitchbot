import requests


def common(word):
    context = { 'accept': 'application/json', 'authority': 'woogles.io', 'origin': 'https://woogles.io', 'User-Agent': 'wordsmith-bot' }
    request = { 'lexicon': 'ECWL', 'words': [word], 'definitions': False }
    response = requests.post('https://woogles.io/twirp/word_service.WordService/DefineWords', json=request, headers=context)
    values = response.json()
    try:
        return values['results'][word]['v']
    except KeyError:
        return response.text


def equity(rack, lexicon):
    parameters = {'rack': rack, 'lexicon': lexicon}
    response = requests.get('https://cross-tables.com/leaves_values.php', headers={'User-Agent': 'wordsmith-bot'}, params=parameters)
    values = response.json()
    try:
        return (values['rack'], values['rack-value'])
    except KeyError:
        return response.text


def predict(config, name, player, opponent):
    authorization = {'Authorization': 'Bearer ' + config.api_token, 'Client-Id': config.client_id}
    parameters = {'login': name}
    response = requests.get('https://api.twitch.tv/helix/users', headers=authorization, params=parameters)
    values = response.json()
    try:
        broadcasterID = values['id']
        player = values['display_name']
    except KeyError:
        return str(values['status']) + ' ' + values['message']

    outcomes = [{'title': player}, {'title': opponent}]
    parameters = {'broadcaster_id': broadcasterID, 'title': 'Who will win?', 'outcomes': outcomes, 'prediction_window': 300}
    response = requests.get('https://api.twitch.tv/helix/predictions', headers=authorization, params=parameters)
    values = response.json()
    try:
        return values['title'] + ': ' + str(values['status'])
    except KeyError:
        return str(values['status']) + ' ' + values['message']
