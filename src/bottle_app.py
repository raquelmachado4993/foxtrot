# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Um - respondendo dúvidas do SuperPython.
.. codeauthor:: Raquel <raquelmachado4993@gmail.com>
- Como associar um evento a uma imagem
- Como combinar cenas em salas diferentes
- Como capturar o teclado
Sem Classes neste modulo:
Changelog
---------
.. versionadded::    20.07
        Adiciona o gerenciador de chamadas http via bottle.
"""
from bottle import default_app, route, static_file
from main import Main

@route('/')
def hello_world():
    return static_file('index.html', root='/home/raquelmachado4993/dev/foxtrot/src/', mimetype='text/html')

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - ensaiando uma nova rota'

@route('<filename:re:.*\.py>')
def py_mundo(filename):
    return static_file(filename, root='/home/raquelmachado4993/dev/foxtrot/src/', mimetype='text/python')

@route('/doc/<filename:re:.*\.html>')
def doc_mundo(filename):
    return static_file(filename, root='/home/raquelmachado4993/dev/foxtrot/src/doc/build/html', mimetype='text/html')

@route('/doc/<filename:re:.*\.css>')
def css_mundo(filename):
    return static_file(filename, root='/home/raquelmachado4993/dev/foxtrot/src/doc/build/html', mimetype='text/css')

application = default_app()