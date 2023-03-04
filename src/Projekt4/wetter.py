""" Kleines Tool um das lokale Wetter zu ermitteln. """

import requests
import sys
import logging
import time


class Wetter:
    """ Wetter generiert eine lokal Wettervorhersage. """

    def __init__(self):
        self.logger = logging.getLogger()

        self.weather_codes = {
            0: 'klarer Himmel',
            1: 'meist klarer Himmel',
            2: 'leicht bewölkt',
            3: 'bewölkt',
            45: 'neblig',
            48: 'sehr neblig',
            51: 'leichter Nieselregen',
            53: 'Nieselregen',
            55: 'starker Nieselregen',
            56: 'überfrierender Nieselregen',
            57: 'überfrierender dichter Nieselregen',
            61: 'leichter Regen',
            63: 'Regen',
            65: 'starker Regen',
            66: 'überfrierender Regen',
            77: 'überfrierender starker Regen',
            71: 'leichter Schneefall',
            73: 'Schneefall',
            75: 'starker Schneefall'
        }

        self.ip = None
        self.lat = None
        self.lon = None
        self.wetter_text = None
        self.update = None

    def _get_ip(self):
        r = requests.get('https://api.ipify.org?format=json')
        if r.status_code != 200:
            self.logger.error('Fehler, IP konnte nicht ermittelt werden!')
            sys.exit(1)

        json = r.json()
        self.ip = json['ip']
        self.logger.info(f"Ihre IP ist {self.ip}.")

    def _get_location(self):
        r = requests.get(
            f'https://sys.airtel.lv/ip2country/{self.ip}/?full=true')
        if r.status_code != 200:
            self.logger.error('Fehler, Ort konnte nicht ermittelt werden!')
            sys.exit(1)

        json = r.json()
        ort = f"{json['city']} ({json['country']})"
        self.lat = json['lat']
        self.lon = json['lon']
        self.logger.info(f'Sie scheinen sich in {ort} zu befinden.')

    def _generate_weather(self):
        self.logger.info(
            f'Ermittle wetter für lat: {self.lat}, lon: {self.lon}.')
        r = requests.get(
            f'https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}&current_weather=true')
        if r.status_code != 200:
            self.logger.error('Fehler, Wetter konnte nicht ermittelt werden!')
            sys.exit(1)

        json = r.json()
        wetter = json['current_weather']
        temperature = wetter['temperature']
        weather_code = wetter['weathercode']

        self.wetter_text = f'Heute hat es {temperature}°C'

        if weather_code in self.weather_codes:
            self.wetter_text += f' und es ist {self.weather_codes[weather_code]}.'
        else:
            self.wetter_text += '.'

        self.update = time.time()

    def wetter(self):
        if self.ip is None:
            self._get_ip()

        if self.lat is None or self.lon is None:
            self._get_location()

        if self.wetter_text is None or (time.time() - self.update) > 60:
            self._generate_weather()

        return self.wetter_text


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    wetter = Wetter()
    for _ in range(0, 30):
        print(wetter.wetter())
        time.sleep(10)
