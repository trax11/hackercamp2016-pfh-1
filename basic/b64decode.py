import base64

s = "Vm0wd2QyVkZOVWRXV0doVFYwZDRWRll3Wkc5V1ZsbDNXa1JTVjFKdGVEQmFWVll3VmpGS2MySkVUbGhoTVVwVVZqQmFTMlJIVmtWUmJGWlhZa1Z3VlZacVNqUlpWMDE0Vkc1T2FWSXdXbFJXYWtaTFUxWmFjbHBFVWxSTmJFcEpWbGQwVjFaWFNraFZiRkpWVmtWYVRGWkdXbXRYUjFKSVVteHdWMkpJUWxsV1ZFa3hVekZrU0ZOclpHcFRSVXBYV1d4b1UwMHhXa2RYYlVaWFZtczFlRlpYZUZOaFZscHlWMVJHVjJFeVVYZFpla1p6VmpGT1dWcEdhR2xTTW1oWFZtMDFkMVl5VW5OV2JrNVlZbGhTV0ZSV1pGTk5SbkJHVjIxR1ZXSkdiRFJWTW5oelZqSkZlVlJZYUZkV1JYQklWV3BHVDFkV2NFZGhSMnhUWVROQ1dGWnRNVFJaVjFGNVZteGthbEpzY0ZsWmJHaFRWMFpTVjFwR1RrNVNiRVkwVjJ0U1EyRkdXbkppZWtwYVYwaENTRlpxUm1GU2JHUjFWMnh3YkdFelFrMVdWM0JIVkRGa1dGUnJhR2hTYkVwVVZtdGFZVmRzV25STlNHaFBVbXRzTTFSVmFHOVdiR1JJWVVaU1YyRXlVVEJXVjNoaFZqRldXVnBHUWxaV1JFRTE="
while True:
    s = base64.b64decode(s)
    if "2016" in s:
        break
print s
