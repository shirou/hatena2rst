# -*- coding: utf-8 -*-

# for Python 2.5
from __future__ import with_statement, print_function, unicode_literals

# 3rd party module
from lxml import etree

# standard module
import re
import sys

if sys.version_info[0] == 2:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
else:
    from io import StringIO

codec = "utf-8"

def main(filename):
    with open(filename, 'rb') as f:
        data = StringIO(f.read().decode(codec))
        tree = etree.parse(data, etree.XMLParser())
        parse_hatena_xml(tree)

def parse_hatena_xml(tree):
    """
    parse element tree of Hatena diary archived XML tree
    """
    pass


def parse_day(day):
    """
    parse <day> tag
    """
    pass


def parse_body(body):
    """
    parse <body> tag
    """
    pass

hyperlink_notation = re.compile("\[(.+)\]")

def convert_link(notation):
    """
    convert hyperlink notation into external link directive
    """
    matched = hyperlink_notation.search(notation)
    if matched:
        content = matched.group(1)
        elements = content.split(":")
        url = ":".join(elements[0:1])
        bookmark = "bookmark" in elements[2:]
        image = "image" in elements[2:]
        title = False
        for e in elements[2:]:
            if e[:5] == "title":
                if e[5] == "=" and len(e) > 6:
                    title = e[6:]
                else len(e) == 5:
                    title = ""
                break
    else:
        url, title, bookmark, image = None, None, None, None
    
    if url and title:
        return "`%s <%s>`_" % (title, url)
    elif url and not title:
        return "`%s`_" % (url,)
    else:
        return notation


def convert_list():
    pass


def convert_img():
    pass


def convert_super_pre():
    """
    convert super pre notation into code-block directive
    """
    pass
    

if __name__ == '__main__':
    from argparse import ArgumentParser

    prog = "hatena2rst"
    description = "Hatena diary XML to reST converter"
    argparse = ArgumentParser(prog=prog, description=description)

    parser.add_argument("filename", type=str)
    args = vars(parser.parse_args())

    main(args.filename)
