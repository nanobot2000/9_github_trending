# Github Trends

Script get top repositories (by stars) from github.com and printed with number of stars and opened issues.

# Quickstart

The script requires the installed Python interpreter version 3.x.

You have to run the script with an optional `-n`, `--number` argument (default=20) with the number of top repositories
and `-d`, `--days` argument (default=7) with the number of days from the current date in which the repositories were created.

To call the help, run the script with the `-h` or `--help` option.

```bash
$ python3 github_trending.py --help
usage: github_trending.py [-h] [-d DAYS] [-n NUMBER]

optional arguments:
  -h, --help            show this help message and exit
  -d DAYS, --days DAYS  repositories created in the last number days
  -n NUMBER, --number NUMBER
                        number of top repositories

```

# Example 

```bash
$ python3 github_trending.py --number 10 --days 30
10 most popular repositories in the last 30 days:
---------------------------------------------------
url: https://github.com/DovAmir/awesome-design-patterns; stars count: 5017; open issues count: 0;
url: https://github.com/upend/IF_MS_BUYS_GITHUB_IMMA_OUT; stars count: 4405; open issues count: 50;
url: https://github.com/wangshub/Douyin-Bot; stars count: 3895; open issues count: 18;
url: https://github.com/Netflix/pollyjs; stars count: 3131; open issues count: 7;
url: https://github.com/me-shaon/GLWTPL; stars count: 3057; open issues count: 4;
url: https://github.com/reach/router; stars count: 2798; open issues count: 5;
url: https://github.com/martenbjork/github-xp; stars count: 2649; open issues count: 6;
url: https://github.com/kitze/JSUI; stars count: 2435; open issues count: 54;
url: https://github.com/vipshop/vjtools; stars count: 2192; open issues count: 11;
url: https://github.com/stereobooster/react-ideal-image; stars count: 1966; open issues count: 10;
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
