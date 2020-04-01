# flask-scheduler
- Flask integrate scheduler
- Tích hợp scheduler vào vào trong flask
- Thư viện https://apscheduler.readthedocs.io/en/stable/index.html
- Example https://github.com/agronholm/apscheduler/tree/master/examples/?at=master
- `FlaskScheduler example` https://github.com/viniciuschiele/flask-apscheduler/tree/master/examples

### script
```bash
# create venv
virtualenv venv

# install lib
pip install -r requirement.txt

# run 
python app.py
```

### Hướng dẫn
- Basic concepts:
    - `triggers`: trả lời cho câu hỏi lập lịch khi nào. Mỗi `job` thì có 1 `trigger` để xác định nó chạy lúc nào
    - `job stores`: là nơi lưu trữ các công việc cần làm ( `job` trả lời cho câu hỏi làm việc gì). Có thể lưu trong memory hoặc database cho phù hợp mục đích. các `job stores` thì không bao giờ được share các `scheduler`
    - `executors`: kiểm soát việc running của `job`. Khi bắt đầu thì làm gì (start một thread hoặc process nào đó). Sau khi kết thúc `executors` sẽ thông báo cho `scheduler` là done và emit ra một event thích hợp (như log vào db)
    - `schedulers`: sheduler bao 3 thằng trên lại. Nó là đối tượng mà ta cần làm việc. Từ việc cấu hình tới run
- Pick up: lựa chọn scheduler, executor, job stores, triggers phù hợp với công việc
    - Scheduler: 
        - `BlockingScheduler`: use when the scheduler is the only thing running in your process
        - `BackgroundScheduler`: use when you’re not using any of the frameworks below, and want the scheduler to run in the background inside your application
        - `AsyncIOScheduler`: use if your application uses the asyncio module
        - `GeventScheduler`: use if your application uses gevent
        - `TornadoScheduler`: use if you’re building a Tornado application
        - `TwistedScheduler`: use if you’re building a Twisted application
        - `QtScheduler`: use if you’re building a Qt application
    - Job stores: 
        - `MemoryJobStore` - __default__: if you always recreate your jobs at the start of your application.
        - `SQLAlchemyJobStore`: store lại công việc đã làm
    - Executor:
        - `ThreadPoolExecutor` - __default__: đáp ứng đầy hầu hết các công việc
        - `ProcessPoolExecutor`: nếu muốn chọc sâu vào CPU
    - Trigger:
        - date: thực hiện công việc 1 lần tại 1 thời điểm nhất định
        - interval: thực hiện công việc lặp lại sau một lượng thời gian cố định (cứ sau 3h thì làm)
        - cron: thực hiện công việc cố định trong ngày
        - combinding triggers: cũng có thể kết hợp các công việc trên lại