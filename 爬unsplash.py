import requests, json

def get_url(url):
	kv={'user-agent':'Mozilla/5.0'}
	f = requests.get(url,headers=kv)
	json_obj=f.text
	
	j=json.loads(json_obj)

	print(j[9]['links']['download'])
		
if __name__ == '__main__':
	url='https://unsplash.com/napi/collections/3348849/photos?page=4&per_page=10&order_by=latest&share_key=2840e7785986af3c0372f6f603e45b39'   
	get_url(url)