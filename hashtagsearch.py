from info import getCreds, makeApiCall
import sys

def getHashtagInfo( params ) :
	endpointParams = dict()
	endpointParams['user_id'] = params['instagram_account_id']
	endpointParams['q'] = params['hashtag_name']
	endpointParams['fields'] = 'id,name'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + 'ig_hashtag_search'

	return makeApiCall( url, endpointParams, params['debug'] )

def getHashtagMedia( params ) :
	endpointParams = dict()
	endpointParams['user_id'] = params['instagram_account_id']
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type']

	return makeApiCall( url, endpointParams, params['debug'] )

hashtag = 'coding'

params = getCreds()
params['hashtag_name'] = hashtag
hashtagInfoResponse = getHashtagInfo( params )
params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id'];

params['type'] = 'top_media'
hashtagTopMediaResponse = getHashtagMedia( params )

for post in hashtagTopMediaResponse['json_data']['data'] :
	print ("\n\n---------- POST ----------\n")
	print ("Link to post:")
	print (post['permalink'])
	print ("\nPost caption:")
	print (post['caption'])
	print ("\nMedia type:")
	print (post['media_type'])
	break
