import logging


class DatabaseHandler(logging.Handler):
    

    def emit(self, record):
        
        try:
            from students.models.monthjournal import logentry
            import datetime

            time = record.asctime[:-4] + '.' + record.asctime[-3:]
            time2 = datetime.datetime.strptime(record.asctime, '%Y-%m-%d %H:%M:%S,%f')

            logentry = logentry(level=record.levelname,
                                asctime=time2,
                                module=record.module,
                                message=record.message)
            logentry.save()
        except Exception as e:
            print e