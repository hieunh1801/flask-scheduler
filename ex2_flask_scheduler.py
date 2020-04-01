from flask import Flask
from flask_apscheduler import APScheduler


def job1(a, b):
    print("send mail", str(a) + ' ' + str(b))


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'ex2_flask_scheduler:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 2
        }
    ]
    SCHEDULER_API_ENABLED = True


if __name__ == '__main__':
    app = Flask(__name__)

    app.config.from_object(Config())
    scheduler = APScheduler()

    scheduler.init_app(app)
    scheduler.start()
    app.run()
