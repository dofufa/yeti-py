#!/usr/bin/env python3

import yeti

for v in vdo:
    print (vdo[v]['id'])
    print (vdo[v]['title'])
    mkqr(vdo[v]['id'])
    mkyt(vdo[v]['id'])
    mkytqr_bw(vdo[v]['id'], vdo[v]['title'])
