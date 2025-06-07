from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='Kafka Messages',
        docs_url='/api/docs',
        description='',
        debug=True
    )
