import argparse
import requests
from datetime import datetime, timedelta


def get_trending_repositories(created_after, top_size):
    search_params = {'q': 'created:>{}'.format(created_after),
                     'type': 'Repositories',
                     'sort': 'stars',
                     'order': 'desc',
                     'per_page': str(top_size)
                     }
    search_response = requests.get(
        'https://api.github.com/search/repositories',
        params=search_params
    )
    return search_response.json().get('items')


def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--days',
        help='repositories created in the last number days',
        default=7,
        type=int,
    )
    parser.add_argument(
        '-n',
        '--number',
        help='number of top repositories',
        default=20,
        type=int,
    )
    return parser


if __name__ == '__main__':
    argparser = create_argparser()
    args = argparser.parse_args()
    today = datetime.now().date()
    n_days_ago = today - timedelta(days=args.days)
    items = get_trending_repositories(
        created_after=n_days_ago,
        top_size=args.number
    )
    print(
        '{} most popular repositories in the last {} days:'.format(
            args.number,
            args.days,
        )
    )
    print('---------------------------------------------------')
    for item in items:
        print(
            'url: {}; stars count: {}; open issues count: {};'.format(
                item.get('html_url'),
                item.get('stargazers_count'),
                item.get('open_issues_count'),
            )
        )
