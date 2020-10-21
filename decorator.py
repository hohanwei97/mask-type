from functools import wraps

from flask import request
from flask import Response


USERNAME = 'username'
PASSWORD = 'passw0rd'


def check_auth(username, password):
  return username == USERNAME and password == PASSWORD


def authenticate():
  return Response(
      'You have to login with proper credentials', 401,
      {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
      return authenticate()
    return f(*args, **kwargs)
  return decorated