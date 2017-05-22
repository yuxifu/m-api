import redis

r_server = redis.Redis('localhost')  # this line creates a new Redis object and
# connects to our redis server
r_server.set('test_key', 'test_value')  # with the created redis object we can
# submits redis commands as its methods

# the previous set key is fetched
print('previous set key %s' % r_server.get('test_key'))

'''In the previous example you saw that we introduced a redis
data type: the string, now we will set an integer and try to
increase its value using redis object built-in methods'''

r_server.set('counter', 1)  # set an integer to a key
r_server.incr('counter')  # we increase the key value by 1, has to be int
# notice that the key is increased now
print('the counter was increased! %s' % r_server.get('counter'))

r_server.decr('counter')  # we decrease the key value by 1, has to be int
# the key is back to normal
print('the counter was decreased! %s' % r_server.get('counter'))


'''Now we are ready to jump into another redis data type, the list, notice 
that they are exactly mapped to python lists once you get them'''

# we use list1 as a list and push element1 as its element
r_server.rpush('list1', 'element1')

r_server.rpush('list1', 'element2')  # assign another element to our list
r_server.rpush('list2', 'element3')  # the same

# with llen we get our redis list size right from redis
print('our redis list len is: %s' % r_server.llen('list1'))

# with lindex we query redis to tell us which element is at pos 1 of our list
print('at pos 1 of our list is: %s' % r_server.lindex('list1', 1))

'''sets perform identically to the built in Python set type. Simply, sets are lists but, can only have unique values.'''

r_server.sadd("set1", "el1")
r_server.sadd("set1", "el2")
r_server.sadd("set1", "el2")

print('the member of our set are: %s' % r_server.smembers("set1"))

'''basically our redis client can do any command supported by redis, check out redis documentation for available commands for your server'''
