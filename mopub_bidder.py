from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import json
import logging

class MopubBidder(webapp.RequestHandler):
    def post(self):
        """ After registering with mopub marketplace, this method will be 
            called each time the auction is run. The mopub server expects
            a response within 70ms. """
        bid_request = json.loads(self.request.body)
        if bid_request.get('imp').get('interstitial'):
            bid_responses = make_json_response(request_id="1234abcd", 
                                               response_id="5678efgh", 
                                               bidder_seat="seat123", 
                                               impression_id="something", 
                                               bid_price=20)
        else:
            bid_responses = make_json_response(request_id="1234abcd", 
                                               response_id="5678efgh", 
                                               bidder_seat="seat123")

        #logging.info("HERHEHEHEHE: %s"%bid_responses)
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(bid_responses)

application = webapp.WSGIApplication(
                                     [('/', MopubBidder)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    
def make_json_response(request_id=None,
                       response_id=None,
                       not_bid_reason=None,
                       currency=None,
                       units=None,
                       bidder_seat=None,
                       group=None,
                       impression_id=None,
                       bid_price=None,
                       ad_id=None,
                       n_url=None,
                       ad_markup=None,
                       ad_domain=None,
                       image_url=None,
                       campaign_id=None,
                       creative_id=None,
                       creative_attr=None):

    bid_response = {'id': request_id,
                    'bidid': response_id,
                    'nbr': not_bid_reason,
                    'cur': currency, 
                    'units': units,
                    'seatbid': [{'seat': bidder_seat, 
                                 'group': group, 
                                 'bid': [{'impid': impression_id, 
                                          'price': bid_price, 
                                          'adid': ad_id,
                                          'nurl': n_url, 
                                          'adm': ad_markup, 
                                          'adomain': ad_domain, 
                                          'iurl': image_url, 
                                          'cid': campaign_id, 
                                          'crid': creative_id, 
                                          'attr': creative_attr}]
                               }]
                    }
    bid_responses = json.dumps(bid_response)
    return bid_responses

#bid_response = {"id":"1234abcd","bidid":"5678efgh","seatbid":[{"seat": "seat123","bid":[{"impid": "something","price": 20,}]}]}
#bid_response = {"id":"1234abcd","bidid":"5678efgh","seatbid":[{"seat": "seat123","bid":[]}]}
