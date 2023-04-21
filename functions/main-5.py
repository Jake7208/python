#!/usr/bin/env python3



def main():
    tempF = float(input('Tempature: '))
    windspeed = float(input('wind speed: '))

    chill = windChill(tempF, windspeed)

    print('the tempature with wind :', chill)

def windChill(temp, speed):
    wc = 35.74 + 0.6215 * temp - 35.75 * (speed ** 0.16) + 0.4275 * temp * (speed ** 0.16)
    return wc


if __name__ == '__main__': main()