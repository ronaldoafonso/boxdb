
"""
    The main module for the boxdb-api.
"""

import api


if __name__ == '__main__':
    api.app.run(host='0.0.0.0', port=5000)
