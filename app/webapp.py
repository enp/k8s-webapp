import os, aioboto3, botocore

from aiohttp import web

session = aioboto3.Session()

async def handle(request):
    try:
        config = botocore.client.Config(connect_timeout=3, read_timeout=3, retries={'max_attempts': 1})
        async with session.resource(service_name='s3', config=config, endpoint_url=os.environ['S3_ENDPOINT']) as s3:
            s3_objects = []
            bucket = await s3.Bucket(os.environ['S3_BUCKET'])
            async for s3_object in bucket.objects.all():
                s3_objects.append(s3_object)
        return web.Response(text='Success: total {} objects in {} bucket\n'.format(len(s3_objects),os.environ['S3_BUCKET']))
    except Exception as e:
        return web.Response(text='Error: {}\n'.format(e))

app = web.Application()
app.add_routes([web.get('/', handle)])
web.run_app(app)
