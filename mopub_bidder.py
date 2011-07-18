from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import simplejson
import logging

class MopubBidder(webapp.RequestHandler):
    def post(self):
        """ After registering with mopub marketplace, this method will be 
            called each time the auction is run. The mopub server expects
            a response within 70ms. """
        bid_request = simplejson.loads(self.request.body)
        bid_responses = make_json_response(request_id="39flvja3", response_id="dv09gn3k", currency="USD", units=0, impression_id="eigu203f", 
                                           bid_price=float(self.request.get("price", default_value=24.)), ad_id="adfo3btnt", ad_markup="<html><b>hiii</b></html>", 
                                           ad_domain="http://www.mopubbidder.com", image_url="http://www.mopubbidderimageurl.com", campaign_id="afhjk234", 
                                           creative_id="ajfwep420", n_url="http://www.mopub_response_url.com")
        
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

    tl_dict = {'id': request_id,
                    'bidid': response_id,
                    'nbr': not_bid_reason,
                    'cur': currency, 
                    'units': units,
                    'seatbid': [{'bid': [{'impid': impression_id, 
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

    tl_dict = _remove_nonetype_values(tl_dict)
    tl_dict['seatbid'][0] = _remove_nonetype_values(tl_dict['seatbid'][0])
    tl_dict['seatbid'][0]['bid'][0] = _remove_nonetype_values(tl_dict['seatbid'][0]['bid'][0])

    tl_dicts = simplejson.dumps(tl_dict)
    return tl_dicts

def _remove_nonetype_values(dirty_dict):
    """ We don't want our json to be full of 'None' responses, so we omit them
        entirely. """
    clean_dict = {}
    for key, value in dirty_dict.iteritems():
        if value is not None:
            clean_dict[key] = value
    return clean_dict
