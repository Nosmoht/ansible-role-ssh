#!/usr/bin/python


class FilterModule(object):
    def filters(self):
        return {
            'listen_addresses': self.listen_addresses,
        }

    def listen_addresses(self, ip_addresses):
        result = []
        for ip in ip_addresses:
            result.append({
                'name': 'ListenAddress',
                'value': ip
            })
        return result
