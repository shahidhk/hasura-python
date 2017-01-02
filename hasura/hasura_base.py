from __future__ import absolute_import, division, print_function, unicode_literals
import requests
import json

class Hasura:
    '''
    Base class for Hasura APIs
    hasura = Hasura(domain[, token[, scheme]])
    '''
    def __init__(self, domain, token='', scheme='https'):
        self.domain = domain
        self.token = token
        self.scheme = scheme
        self.headers = {
            'Content-Type': 'application/json',
        }
        self.data = _Data(self)
        self.auth = _Auth(self)

class _Auth:
    '''
    Base class for Hasura Auth APIs
    '''
    def __init__(self, hasura):
        self.auth_url = hasura.scheme + '://auth.' + hasura.domain
    
    def login(self):
        ''' Login method '''
        pass

    def logout(self):
        ''' Logout method '''
        pass

class _Data:
    '''
    Base class for Hasura Data APIs
    '''
    def __init__(self, hasura):
        self.data_url = hasura.scheme + '://data.' + hasura.domain 
        self.query_url = self.data_url + '/v1/query'
        self.headers = hasura.headers
        if hasura.token:
            self.headers['Authorization'] = 'Bearer ' + hasura.token

    def query(self, req_type, req_args):
        ''' Generic query data method '''
        res = requests.post(
                self.query_url,
                data=json.dumps({
                    'type': req_type,
                    'args': req_args
                }),
                headers = self.headers
            )
        return res

    def insert(self, table, objects, returning=[]):
        ''' Insert data method '''
        args = locals()
        del args['self']
        res = self.query('insert', {key : value for key, value in args.items() if value})
        return res.json()

    def update(self, table, where, _set={}, _inc={}, _mul={}, _default={}, returning=[]):
        ''' Update data method '''
        args = locals()
        del args['self']
        res = self.query('update', {'$' + key[1:] if key[0] == '_' else key : value for key, value in args.items() if value})
        return res.json()

    def delete(self, table, where, returning=[]):
        ''' Delete data method '''
        args = locals()
        del args['self']
        res = self.query('delete', {key : value for key, value in args.items() if value})
        return res.json()

    def select(self, table, columns, where={}, order_by={}, limit=10, offset=0):
        ''' Select data method '''
        args = locals()
        del args['self']
        res = self.query('select', {key : value for key, value in args.items() if value})
        return res.json()

    def count(self, table, where={}, distinct=[]):
        ''' Count method ''' 
        args = locals()
        del args['self']
        res = self.query('count', {key : value for key, value in args.items() if value})
        return res.json()['count']
