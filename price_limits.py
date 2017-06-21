# Set up price limit for betting items.

# Author:       obliv[io]us
# Created:      20 June 2017
# Version:      1.0

# The first row is the dollar price break points.
# The second row is the desired ratio break points.
# ratio -- current price (shows at IGXE or C5GAME) / dollar price (shows at dotamax)

# For example:
# csgo_dotamax_limit = [
#     [10., 30.],
#     [4.2, 4.3]]

# means the program will notify:

# if (dollar price (shows at dotamax) > 10 and ratio > 4.2) or
#    (dollar price (shows at dotamax) > 30 and ratio > 4.3)

csgo_dotamax_limit = [
    [10., 30.],
    [4.4, 4.5]]