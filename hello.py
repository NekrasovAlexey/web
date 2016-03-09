def application(env, start_response):
	body = env['QUERY_STRING'].replace('&', '\r\n');
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [body]