from ..youtube import youtube
import json

def get_active_livestream(channel_id):
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        eventType='live',
        type='video'
    )
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        live_video = response['items'][0]
        live_video_id = live_video['id']['videoId']
        live_video_title = live_video['snippet']['title']
        return live_video_id, live_video_title
    else:
        return None, None

def get_channel_id_by_handle(handle):
    request = youtube.channels().list(
        part='snippet',
        forHandle=handle,
        pageToken="1"
    )
    response = request.execute()

    # print response as json
    print(json.dumps(response, indent=4))
    
    
    
    if 'items' in response and len(response['items']) > 0:
        channel_id = response['items'][0]['id']
        return channel_id
    else:
        return None
    
def get_live_chat_id(video_id):
    request = youtube.videos().list(
        part='liveStreamingDetails',
        id=video_id
    )
    response = request.execute()
    live_chat_id = response['items'][0]['liveStreamingDetails']['activeLiveChatId']
    return live_chat_id

def get_live_chat_messages(live_chat_id, page_token=None):
    request = youtube.liveChatMessages().list(
        liveChatId=live_chat_id,
        part='snippet',
        pageToken=page_token,
        maxResults=200
    )
    response = request.execute()
    return response


def get_channel_data(channel_id):
    request = youtube.channels().list(
        part='snippet',
        id=channel_id
    )
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        channel = response['items'][0]
        channel_name = channel['snippet']['title']
        channel_picture = channel['snippet']['thumbnails']['default']['url']
        print(channel, channel_name, channel_picture)
        return channel_name, channel_picture
    else:
        return None, None
