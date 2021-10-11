api_url = 'https://api.chucknorris.io/jokes/random'

fetch(api_url)
.then(response => {
	console.log(response.json())})