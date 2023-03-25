from datetime import datetime

now = datetime.today().utcnow().strftime("""%Y
%m
%d""")
print(now)