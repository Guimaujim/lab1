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

    def search_book(self, html):
        # buscar dades
        bs = bs4.BeautifulSoup(html, "lxml")
        caixa = bs.find("div", "dotd-title")
        # llimpiar string
        item = str(caixa.find("h2")).strip('<h2></h2>')
        itemClean = item.strip()
        return itemClean


    def main(self):
        webpag = self.get_webpage('https://www.packtpub.com/packt/offers/free-learning')
        results = self.search_book(webpag)
        # imprimir resultats
        print results

if __name__ == "__main__":
    cw = Client()
    cw.main()
