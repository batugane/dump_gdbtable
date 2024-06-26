#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# $Id$
#
# Project:  GDAL/OGR
# Purpose:  Dump FileGDB .gdbindexes content
# Author:   Even Rouault <even dot rouault at mines dash paris dot org>
#
###############################################################################
# Copyright (c) 2013, Even Rouault <even dot rouault at mines dash paris dot org>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################


import struct
import sys

if len(sys.argv) != 2:
    print('Usage: dump_gdbindexes.py some_file.gdbindexes')
    sys.exit(1)

filename = sys.argv[1]

def read_uint8(f):
    return ord(f.read(1))

def read_uint16(f):
    v = f.read(2)
    return struct.unpack('H', v)[0]

def read_int32(f):
    v = f.read(4)
    return struct.unpack('i', v)[0]

def read_utf16(f, nbcar):
    return f.read(nbcar * 2).decode("utf-16le")

f = open(filename, 'rb')
nindexes = read_int32(f)
print('nindexes = %d' % nindexes)
for i in range(nindexes):
    idx_name_length_utf16_car = read_int32(f)
    idx_name = read_utf16(f, idx_name_length_utf16_car)
    print('idx_name = %s' % idx_name)
    
    magic1 = read_uint16(f)
    magic2 = read_int32(f)
    magic3 = read_uint16(f)
    magic4 = read_int32(f)
    print('magic1 = %d' % magic1)
    print('magic2 = %d' % magic2)
    print('magic3 = %d' % magic3)
    print('magic4 = %d' % magic4)
    
    col_name_length_utf16_car = read_int32(f)
    col_name = read_utf16(f, col_name_length_utf16_car)
    print('col_name = %s' % col_name)
    
    magic5 = read_uint16(f)
    print('magic5 = %d' % magic5)

    print('')
