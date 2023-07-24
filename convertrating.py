def converter_certificacao(certificacao):
    certificacoes = {
        'US G': 'Livre',
        'US PG': '10 anos',
        'US PG-13': '12 anos',
        'US R': '16 anos',
        'US NC-17': '18 anos',
        'US NR': '18 anos',
        'US Unrated': '18 anos',
        'US TV-Y': 'Livre',
        'US TV-Y7': 'Livre',
        'US TV-G': 'Livre',
        'US TV-PG': '10 anos',
        'US TV-14': '14 anos',
        'US TV-MA': '18 anos',
        'KR ALL': 'Livre',
        'KR 7': 'Livre',
        'KR 12': '14 anos',
        'KR 15': '16 anos',
        'KR 18': '18 anos',
        'KR Restricted screening': '18 anos',
        'KR 9': '18 anos',
        'GB U': 'Livre',
        'GB PG': '10 anos',
        'GB 12A': '12 anos',
        'GB 12': '14 anos',
        'GB 15': '16 anos',
        'GB 18': '18 anos',
        'GB R18': '18 anos',
        'BR Livre': 'Livre',
        'BR 10': '10 anos',
        'BR 12': '12 anos',
        'BR 14': '14 anos',
        'BR 16': '16 anos',
        'BR 18': '18 anos'
    }
    return certificacoes.get(certificacao, 'Não Disponível')
      
