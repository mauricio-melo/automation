import bet 
import sys

url = sys.argv[1]
isEqual = sys.argv[2]
isPlus = sys.argv[3]
isFirstHalf = sys.argv[4]
isHome = sys.argv[5]


bet.open_chrome(url)
bet.login("F#carioca7")
bet.corner_tab()
bet.select_bet(isEqual, isPlus, isFirstHalf, isHome)
bet.make_bet("1")