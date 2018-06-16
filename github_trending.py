import argparse
import requests
from datetime import datetime, timedelta


def get_trending_repositories(created_after, top_size):
    created_after_filter = 'created:>{}'.format(created_after)
    search_params = {'q': created_after_filter,
                     'type': 'Repositories',
                     'sort': 'stars',
                     'order': 'desc',
                     'per_page': top_size
                     }
    search_response = requests.get(
        'https://api.github.com/search/repositories',
        params=search_params
    )
    return search_response.json().get('items')


def count_open_issues(repository):
    repository_name = repository.get('full_name')
    issues_url = 'https://api.github.com/repos/{}/issues'\
        .format(repository_name)
    issues_response = requests.get(issues_url)
    open_issues = [issue for issue
                   in issues_response.json()
                   if issue.get('state') == 'open'
                   ]
    return len(open_issues)



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


def print_repositories(repositories):
    print('-'*50)
    for repository in repositories:
        print(
            'url: {}; stars count: {}; open issues count: {};'.format(
                repository.get('html_url'),
                repository.get('stargazers_count'),
                count_open_issues(repository),
            )
        )


if __name__ == '__main__':
    argparser = create_argparser()
    args = argparser.parse_args()
    today = datetime.now().date()
    n_days_ago = today - timedelta(days=args.days)
    trending_repositories = get_trending_repositories(
        created_after=n_days_ago,
        top_size=args.number
    )
    print(
        '{} most popular repositories in the last {} days:'.format(
            args.number,
            args.days,
        )
    )
    print_repositories(trending_repositories)

