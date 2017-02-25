#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 -
'''
Simple client web per descarregar de udl.cat

@author: guimaujim@gmail.com
'''
import urllib2
import bs4


class Client(object):
    def get_webpage(self, page):
        """obtenir la plana web"""
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage

    def search_date(self, html):
        # buscar dades
        bs = bs4.BeautifulSoup(html, "lxml")
        caixa = bs.find("div", "sg-featuredlink")
        items = caixa.find_all("div", "featured-links-item")
        results = []
        for i in items:
            time = i.find('time')["datetime"]
            text = i.find('span', 'flink-title').text
            results.append((time, text))
        return results


    def main(self):
        webpag = self.get_webpage('http://www.udl.cat')
        results = self.search_date(webpag)
        # imprimir resultats
        print results
        print len(results)

if __name__ == "__main__":
    cw = Client()
    cw.main()
