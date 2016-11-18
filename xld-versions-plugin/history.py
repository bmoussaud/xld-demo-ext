print request
from org.joda.time import LocalDate

def is_deployment_task(task):
    return False if task.metadata['taskType'] == "CONTROL" else True

def is_application(task,application_name):
    return task.metadata['application'] == application_name

def is_candidate(task, application_name):
    return is_deployment_task(task) and is_application(task,application_name)

def to(archived_task):
    data = dict(archived_task.metadata)
    data['completionDate']=str(archived_task.completionDate)
    data['startDate']=str(archived_task.startDate)
    return data

begin_date = request.query['begindate']
end_date = request.query['enddate']
application_name= request.query['application_name']
logger.error( 'begindate      %s' % begin_date)
logger.error( 'enddate        %s' % end_date)
logger.error( 'application_name %s' % application_name)

begin = LocalDate(begin_date);
end = LocalDate(end_date)
tasks = taskBlockService.query(begin,end)
response.entity = [to(task) for task in tasks if is_candidate(task, application_name)]
