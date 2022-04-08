#!/usr/bin/env python3
import connexion


def post_greeting_ascii(**kwargs):
    """ Convert and return a JSON response containing a
    list of integers based on the provided
    list of characters (any ASCII alphabet character)  """
    list_data = kwargs['body']
    list_data = [0 if x in ('h', 'H') else x for x in list_data]
    list_data = [0 if x != 0 and x.lower() > 'h' else x for x in list_data]
    list_data = [int(ord(x)) * 10 if x != 0 else x for x in list_data]
    return (list_data), 200


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='openapi/')
    app.add_api('ascii-data-api.yaml', arguments={'title': 'Getting list of ascii alphabet characters'})
    app.run()
