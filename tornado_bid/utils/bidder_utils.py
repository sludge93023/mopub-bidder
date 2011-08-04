import simplejson  
    
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

    response_dict = {'id': request_id,
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

    response_dict = _remove_nonetype_values(response_dict)
    response_dict['seatbid'][0] = _remove_nonetype_values(response_dict['seatbid'][0])
    response_dict['seatbid'][0]['bid'][0] = _remove_nonetype_values(response_dict['seatbid'][0]['bid'][0])

    response_dicts = simplejson.dumps(response_dict)
    return response_dicts

def _remove_nonetype_values(dirty_dict):
    """ We don't want our json to be full of 'None' responses, so we omit them
        entirely. """
    clean_dict = {}
    for key, value in dirty_dict.iteritems():
        if value is not None:
            clean_dict[key] = value
    return clean_dict