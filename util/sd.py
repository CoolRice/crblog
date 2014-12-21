from util import Pager

p = Pager.Pager(pageNumber=7, total=44, limit=4)
print p.navigatePageNumbers