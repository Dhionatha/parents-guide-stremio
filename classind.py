import requests
from convertrating import converter_certificacao
import os
# Função para obter o ID TMDb de uma série pelo ID IMDb
TMDB_API = os.getenv('TMDB_API')

def get_tmdb_id_series(imdb_id):
    url = f'https://api.themoviedb.org/3/find/{imdb_id}'
    params = {
        'api_key': TMDB_API,
        'external_source': 'imdb_id'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        tv_results = data.get('tv_results', [])
        if tv_results:
            return tv_results[0]['id']
    return None

# Função para obter o ID TMDb de um filme pelo ID IMDb
def get_tmdb_id_movie(imdb_id):
    url = f'https://api.themoviedb.org/3/find/{imdb_id}'
    params = {
        'api_key': TMDB_API,
        'external_source': 'imdb_id'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        movie_results = data.get('movie_results', [])
        if movie_results:
            return movie_results[0]['id']
    return None

# Função para obter as classificações indicativas de uma série pelo ID TMDb
def get_series_content_ratings(tmdb_id):
    url = f'https://api.themoviedb.org/3/tv/{tmdb_id}/content_ratings'
    params = {
        'api_key': TMDB_API
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        return results
    return None

# Função para obter as classificações indicativas de um filme pelo ID TMDb
def get_movie_content_ratings(tmdb_id):
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}/release_dates'
    params = {
        'api_key': TMDB_API
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        return results
    return None

def get_rating(id):
    # Obtendo o ID TMDb da série ou filme
    imdb_id = id
    imdb_id_parts = imdb_id.split(':')
    final_id = imdb_id_parts[0]
    tmdb_id_series = get_tmdb_id_series(final_id)
    tmdb_id_movie = get_tmdb_id_movie(final_id)
    
    if tmdb_id_series:
        # Obtendo as classificações indicativas da série
        content_ratings = get_series_content_ratings(tmdb_id_series)
        country = 'BR'
        if content_ratings:
            certification = None
            for result in content_ratings:
                if result['iso_3166_1'] == country:
                    certification = result['rating']
                    break
    
            if certification:
                cert = f"{country} {certification}"
            else:
                country = 'US'
                for result in content_ratings:
                    if result['iso_3166_1'] == country:
                        certification = result['rating']
                        break
    
                if certification:
                    cert = f"{country} {certification}"
                else:
                    country = 'GB'
                    for result in content_ratings:
                        if result['iso_3166_1'] == country:
                            certification = result['rating']
                            break
                
                if certification:
                    cert = f"{country} {certification}"
                else:
                    country = 'KR'
                    for result in content_ratings:
                        if result['iso_3166_1'] == country:
                            certification = result['rating']
                            break
    
                    if certification:
                        cert = f"{country} {certification}"
                    else:
                        print("Não foram encontradas classificações indicativas para os países BR, US, GB e KR")
        else:
            print("Não foi possível obter as classificações indicativas da série")
    
    if tmdb_id_movie:
        # Obtendo as classificações indicativas do filme
        content_ratings = get_movie_content_ratings(tmdb_id_movie)
        country = 'BR'
        if content_ratings:
            certification = None
            for result in content_ratings:
                if result['iso_3166_1'] == country:
                    certification = result['release_dates'][0]['certification']
                    break
    
            if certification:
                cert = f"{country} {certification}"
            else:
                country = 'US'
                for result in content_ratings:
                    if result['iso_3166_1'] == country:
                        certification = result['release_dates'][0]['certification']
                        break
    
                if certification:
                    cert = f"{country} {certification}"
                else:
                    country = 'GB'
                    for result in content_ratings:
                        if result['iso_3166_1'] == country:
                            certification = result['release_dates'][0]['certification']
                            break
                
                if certification:
                    cert = f"{country} {certification}"
                else:
                    country = 'KR'
                    for result in content_ratings:
                        if result['iso_3166_1'] == country:
                            certification = result['release_dates'][0]['certification']
                            break
    
                    if certification:
                        cert = f"{country} {certification}"
                    else:
                        print("Não foram encontradas classificações indicativas para os países BR, US, GB e KR")
        else:
            print("Não foi possível obter as classificações indicativas do filme")
    
    cert_br = converter_certificacao(cert)
    return cert_br
