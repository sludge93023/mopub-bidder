"""
    Simple epoll-based tornado server. Install tornado here:
    http://www.tornadoweb.org/
    
    Run 1 worker on port 8000 with: 
    $ python tornado_bidder
    
    We recommend running 2 tornado instances per core on your machine
"""                 

from utils.bidder_utils import make_json_response
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):            
        
        bid_request = simplejson.loads(self.request.body)  
        # !!!!!!!!!!!!!!! Add bidder logic here !!!!!!!!!!!!!!!!!
        
        
        
        
        
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        
        bid_response = make_json_response(request_id=None,
                               response_id=None,
                               not_bid_reason=None,
                               currency=None,
                               units=None,
                               impression_id=None,
                               bid_price=None,
                               ad_id=None,
                               n_url=None,
                               ad_markup=None,
                               ad_domain=None,
                               image_url=None,
                               campaign_id=None,
                               creative_id=None,
                               creative_attr=None)  
                               
        self.write(bid_response)



application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()