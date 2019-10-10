import requests
from bs4 import BeautifulSoup

# Lyon cinemas id dictionary
cinema_id_list = {
    'INTERNATIONALE': '32',
    'CONFLUENCE': '36',
    'ASTORIA': '33',
    'PARTDIEU': '34'
}



def get_movies_from_cinema(watchingDate, cinema):
    """Request the html containing the movies from the specified cinema at the specified date.

        Parameters
        ----------
        watching_date : str,
            The date when the movie want to be watch
        
        cinema : str,
            The id of the cinema where to watch the movie
        """
    url = "https://www.ugc.fr/showingsCinemaAjaxAction%21getShowingsForCinemaPage.action"

    querystring = {"cinemaId":cinema, "date":watchingDate}

    headers = {
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "www.ugc.fr",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "JSESSIONID=7ED4355F99CC865C330A008390015089.tomcat02; lang=fr",
        'Content-Length': "0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, headers=headers, params=querystring)

    return response.text

def parse_movies_data(movies_data):
    """Parse all the movies from the given html

        Parameters
        ----------
        movies_data : str,
            The html data containing the movies
        """
    soup = BeautifulSoup(movies_data, "html.parser")
    movies_list = soup.find_all('article')


if __name__ == "__main__":
    response = get_movies_from_cinema('2019-10-11', cinema_id_list['ASTORIA'])
    parse_movies_data(response)
