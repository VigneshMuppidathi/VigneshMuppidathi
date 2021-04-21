class Movie:
    def __init__(self,movie_id,movie_name,ticket_cost):
        self.movie_id=movie_id
        self.movie_name=movie_name
        self.ticket_cost=ticket_cost
    def pricecategory(self):
        cat=["General","Silver","Gold","Platinum"]
        if self.ticket_cost in range(0,150):
            self.cost_cat=cat[0]
        elif self.ticket_cost in range(150,250):
            self.cost_cat=cat[1]
        elif self.ticket_cost in range(250,350):
            self.cost_cat=cat[2]
        elif (self.ticket_cost>=350):
            self.cost_cat=cat[3]
class MovieTicket:
    def __init__(self,custname,moviename,viewercount,totalticketcost):
        self.custname=custname
        self.moviename=moviename
        self.viewercount=viewercount
        self.totalticketcost=totalticketcost
def getcategorywisecount(movielist):
    for movie in movielist:
        movie.pricecategory()
    Dict={}
    for movie in movielist:
        cost_category=movie.cost_cat
        if cost_category not in Dict.keys():
            Dict[cost_category]=1
        else:
            Dict[cost_category]+=1
    return Dict
def bookMovieticket(movielist,custname,moviename,viewercount):
    for mov in movielist:
        if(mov.movie_name.lower()== moviename.lower()):
        
            total_ticketcost=mov.ticket_cost*viewercount
            return total_ticketcost
if '__main__':
    movielist=[]
    n=int(input())
    for i in range(n):
        movie_id=int(input())
        movie_name=input()
        ticket_cost=int(input())
        m=Movie(movie_id,movie_name,ticket_cost)
        movielist.append(m)
    custname=input()
    moviename=input()
    viewercount=int(input())
    Dict=getcategorywisecount(movielist)
    b=bookMovieticket(movielist,custname,moviename,viewercount)
    print('Category wise count:')
    for movie in Dict:
        print('{}:{}'.format(movie,Dict[movie]))
    print(custname,b)
