import orm ,pymysql
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop,host='localhost',port=3306,user='root', password='', db='awesome')
    u = User(name='Test', email='test12333@qq.com', passwd='1234567890', image='about:blank')
    await u.save()
    await orm.destory_pool()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()

