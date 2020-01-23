import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend


def configure():
    result_backend = RedisBackend(port=63791)

    rabbitmq_broker = RabbitmqBroker(port=56721)
    rabbitmq_broker.add_middleware(Results(backend=result_backend))

    dramatiq.set_broker(rabbitmq_broker)
