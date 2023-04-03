import os

PROD: str = "prod"
STAGING: str = "staging"
DEV: str = "dev"

LOCAL_TIMEZONE = "Asia/Bishkek"

# Response messages
INVALID_AUTHENTICATION_CREDENTIALS = "Could not validate credentials"
PERMISSION_DENIED_MESSAGE = 'Отказано в доступе'

LIMIT_FOR_RESENDING_CODE = 6


MEETING_APPLICATION_STATUS_UPDATE_REASONS = ['passed_first_screening']
DONE_APPLICATION_STATUS_UPDATE_REASONS = ['contract_signed']


TIMEZONE = os.getenv('TIMEZONE', 'Asia/Bishkek')

ROLLBAR_ACCESS_TOKEN = os.getenv('ROLLBAR_ACCESS_TOKEN')

EMPLOYEE_INVITATION_MESSAGE_HTML = '<p>Здравствуйте!<br><br>Вы были зарегистрированы в системе FIN.<br><br><br>Ваша почта для входа в систему: {email}<br>Ваш пароль для входа в систему: {password}<br>Ссылка: {domain_name}/dashboard/login<br><br>С уважением,<br>Команда FIN</p>'
