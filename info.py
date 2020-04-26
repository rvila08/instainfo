import requests
import json

def getCreds() :
	creds = dict()
	creds['access_token'] = 'EAAqGOFGvl4IBACmWz8DEC9UqEpdo1PeeMgiZA8OmgWKYaRIxpLygldZBslv5GLLTIZBeURRRYwvbCvUt6T5N9XKPTNzD5NCRZBVr4v5y1OC36v5eOCCrSpNirOI6PNNxZADZAzj4c7Sm7W9h8PnGXtrmQp9oFs1WdZBSaZAm1kELjyaZBiJCESMW9' # access token for use with all api calls
	creds['client_id'] = '2962326213859202'
	creds['client_secret'] = '1fae34aa52201054578d7f57588c9493'
	creds['graph_domain'] = 'https://graph.facebook.com/'
	creds['graph_version'] = 'v6.0'
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
	creds['debug'] = 'no'
	creds['page_id'] = '105222784489353'
	creds['instagram_account_id'] = '17841433658923786'
	creds['ig_username'] = 'cpsc353project_theboys'
	
	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :
	data = requests.get( url, endpointParams )

	response = dict()
	response['url'] = url
	response['endpoint_params'] = endpointParams
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 )
	response['json_data'] = json.loads( data.content )
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 )

	if ( 'yes' == debug ) :
		displayApiCallData( response )

	return response
