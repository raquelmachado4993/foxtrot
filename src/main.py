#-*- coding: utf-8 -*-
"""SPDX-License-Identifier: GPL-3.0-or-later"""
""" Tutorial Dois - Brincando de git,

.. codeauthor:: Raquel Fernandes <raquelmachado4993@gmail.com>

- Como criar um repositório no github
- Como clonar usando o comando git
- Como comitar usando o comando git

- classes neste módulo:

    :py:class: 'Main' Exemplo de classe.

Changelog
---------
.. versionadded::    20.07
        Código da Aula 2.
"""

class Main:
    """Classe exemplo.

       :param versao: versão deste exemplo.

    """

    def __init__(self,versao):
        print("classe exemplo, versao {}".format(versao))


if __name__ =="__main__":
    Main(1)