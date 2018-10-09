import logging

def get_user_info(username=None):
    logging.info("punto user info")
    return {"user_info": username}


def get_commits_info(username=None, time_range=None):
    logging.info("punto de commit_info")
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]


def get_health():
    logging.info("punto health")
    return {"message": "ok"}
